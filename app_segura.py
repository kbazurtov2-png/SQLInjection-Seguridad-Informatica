from flask import Flask, render_template_string, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'

# Inicializar base de datos SQLite segura
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute("SELECT * FROM users WHERE username = 'admin'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
    conn.commit()
    conn.close()

# Plantilla HTML reutilizada para el login seguro
HTML_LOGIN = '''
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <title>Login Seguro - UNEMI</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f9; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); width: 300px; }
        h2 { text-align: center; color: #333; }
        label { display: block; margin-bottom: 5px; color: #666; }
        input[type="text"], input[type="password"] { width: 100%; padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        button { width: 100%; padding: 10px; background-color: #5cb85c; border: none; color: white; font-size: 16px; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #4cae4c; }
        .error { color: #d9534f; text-align: center; font-size: 14px; }
    </style>
</head>
<body>
    <div class="login-card">
        <h2>Login Seguro</h2>
        {% if error %}
            <p class="error">{{ error }}</p>
        {% endif %}
        <form method="POST">
            <label for="username">Usuario:</label>
            <input type="text" id="username" name="username" required>
            <label for="password">Contraseña:</label>
            <input type="password" id="password" name="password" required>
            <button type="submit">Ingresar</button>
        </form>
    </div>
</body>
</html>
'''

HTML_WELCOME = '''
<!doctype html>
<html lang="es">
<head><meta charset="utf-8"><title>Bienvenido</title></head>
<body style="font-family: Arial; text-align: center; margin-top: 50px;">
    <h1 style="color: #5cb85c;">¡Bienvenido, {{ username }}!</h1>
    <p>Autenticación segura completada con éxito.</p>
    <a href="{{ url_for('logout') }}">Cerrar Sesión</a>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        #  MITIGACIÓN: Uso de consultas parametrizadas (sentencias preparadas con '?')
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        
        try:
            # Los parámetros se pasan como tupla en el segundo argumento de execute()
            cursor.execute(query, (username, password))
            user = cursor.fetchone()
        except sqlite3.Error as e:
            user = None
            error = f"Error en la base de datos: {e}"
            
        conn.close()
        
        if user:
            session['username'] = user[1]
            return render_template_string(HTML_WELCOME, username=user[1])
        else:
            error = "Usuario o contraseña incorrectos."
            
    return render_template_string(HTML_LOGIN, error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)