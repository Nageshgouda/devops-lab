import os
from http.server import BaseHTTPRequestHandler, HTTPServer

message = os.getenv("APP_MESSAGE", "Hello from DevOps backend")
port = int(os.getenv("APP_PORT", "5000"))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = message.encode()

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

server = HTTPServer(("0.0.0.0", port), Handler)

print(f"Backend listening on port {port}")

server.serve_forever()
