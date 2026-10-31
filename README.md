# Práctica Nº 4 — Seguridad en Redes LAN, Inalámbricas y Bases de Datos (SQL Injection)

**Asignatura:** Seguridad Informática  
**Docente:** Alex Armando Avila Coello  
**Carrera:** Tecnologías de la Información en Línea  
**Institución:** Universidad Estatal de Milagro (UNEMI)  
**Año:** 2026  

---

##  Descripción del Proyecto
Este repositorio contiene una simulación práctica y controlada desarrollada en **Python + Flask + SQLite** para evaluar la vulnerabilidad crítica de **Inyección SQL (SQL Injection)** catalogada en la lista OWASP Top 10. Además, incluye módulos de mitigación mediante **consultas parametrizadas** (sentencias preparadas) y un script básico de **escaneo de red (TCP port scanner)**.

---

##  Estructura del Repositorio
- `app_vulnerable.py`: Servidor web Flask expuesto a Inyección SQL por concatenación de cadenas.
- `app_segura.py`: Servidor web Flask refactorizado con sentencias preparadas.
- `ataque_sql_i.py`: Script automatizado de pruebas de penetración (Bypass de autenticación).
- `escaneo_red.py`: Módulo de escaneo de puertos y descubrimiento de servicios activos.
- `README.md`: Descripción general del proyecto.
- `MANUAL_USO.md`: Guía detallada de instalación, despliegue local y ejecución de pruebas.

---

##  Consideraciones Éticas y Declaración de Uso de IA
Este proyecto ha sido desarrollado exclusivamente con fines académicos bajo los estándares de la UNEMI. El uso de Inteligencia Artificial como apoyo se declara formalmente al final de la documentación del proyecto conforme a las directrices institucionales.