import socket
from datetime import datetime

# Definir el objetivo (localhost para pruebas locales seguras)
HOST_OBJETIVO = "127.0.0.1"
PUERTOS_A_ESCANEAR = [21, 22, 80, 443, 3306, 5000, 8080]

def escanear_red():
    print("-" * 60)
    print(f"[*] Iniciando escaneo de red en el host: {HOST_OBJETIVO}")
    print(f"[*] Hora de inicio: {datetime.now()}")
    print("-" * 60)
    
    try:
        for puerto in PUERTOS_A_ESCANEAR:
            # Crear un socket TCP/IP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0) # Tiempo de espera de 1 segundo
            
            # Intentar la conexión al puerto
            resultado = s.connect_ex((HOST_OBJETIVO, puerto))
            
            if resultado == 0:
                print(f"[+] Puerto {puerto}: ABIERTOS (Servicio activo)")
            else:
                print(f"[-] Puerto {puerto}: Cerrado o filtrado")
                
            s.close()
            
    except KeyboardInterrupt:
        print("\n[-] Escaneo interrumpido por el usuario.")
    except socket.gaierror:
        print("\n[-] Error: No se pudo resolver el hostname del objetivo.")
    except socket.error:
        print("\n[-] Error: No se pudo conectar al servidor.")
        
    print("-" * 60)
    print("[*] Escaneo de red finalizado.")
    print("-" * 60)

if __name__ == "__main__":
    escanear_red()