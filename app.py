# app.py
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

class MyHandler(SimpleHTTPRequestHandler):
 def do_GET(self):
  self.send_response(200)
  self.send_header('Context-type', 'text/html')
  self.end_headers()
  self.wfile.write(b'Hello, World! This is my python web application bro')

httpd = HTTPServer(('', PORT), MyHandler)
print(f'Serving on port {PORT}...')
httpd.serve_forever()
