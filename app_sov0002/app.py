import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Obtener el secreto desde la variable de entorno
        secreto = os.getenv("SECRETO", "No hay secreto configurado")

        contenido = f"""
        <html>
        <head>
            <meta charset="utf-8">
            <title>Hola SOV0002</title>
        </head>
        <body style="background:#f6f6f6; display:flex; justify-content:center; align-items:center; height:100vh; margin:0;">
            <h1 style="font-family:Arial; color:#000;">
                hola SOV0002, mi secreto es: {secreto}
            </h1>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(contenido.encode("utf-8"))

if __name__ == "__main__":
    # Cambiamos aquí a 8001
    servidor = HTTPServer(("0.0.0.0", 8001), SimpleHandler)
    print("Servidor iniciado en http://localhost:8001")
    servidor.serve_forever()
