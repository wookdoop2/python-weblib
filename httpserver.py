from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

port = 9999


class MyHttpRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        result = urlparse(self.path)
        print(result)
        self.send_response(200)
        self.send_header("content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("<h1>안녕하세요</h1>".encode("utf-8"))


httpd = HTTPServer(("0.0.0.0", port), MyHttpRequestHandler)
print(f"Server running on port : " + str(port))
httpd.serve_forever()
