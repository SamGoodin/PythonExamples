from http.server import HTTPServer, BaseHTTPRequestHandler


class serv(BaseHTTPRequestHandler):
    
    def do_GET(self):
        print(f"'{self.address_string()}' received request for '{self.path}'")
        if self.path == '/':
            self.path = '/index.html'
        try:
            openFile = open(self.path[1:]).read()
            self.send_response(200)
        except:
            openFile = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(openFile, 'utf-8'))

# My laptop's public IP
server = HTTPServer(('149.162.133.39', 8080), serv)
server.serve_forever()