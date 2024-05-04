from http.server import BaseHTTPRequestHandler, HTTPServer
import time


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                bytes(
                    "<html><head><title>https://pythonbasics.org</title></head>"
                    f"<p>Bienvenido {self.path}</p>"
                    "<body><p>Como estas??<p></body></html>",
                    "utf-8",
                )
            )
        elif self.path == "/test":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                bytes(
                    "<html><head><title>https://pythonbasics.org</title></head>"
                    f"<p>Bienvenido: {self.path}</p>"
                    "<body><p>Esto es una paginad e prueba </p></body></html>",
                    "utf-8",
                )
            )

        elif self.path == "/users":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                bytes(
                    "<html><head><title>https://pythonbasics.org</title></head>"
                    f"<p>Request: {self.path}</p>"
                    "<body><p>Users de la pagina del curso de python</p></body></html>",
                    "utf-8",
                )
            )
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                bytes(
                    "<html><head><title>404 Not Found</title></head>"
                    "<body><h1>404 Not Found</h1></body></html>",
                    "utf-8",
                )
            )


if __name__ == "__main__":
    hostName = "localhost"
    serverPort = 8080

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")