from http.server import BaseHTTPRequestHandler
from datetime import datetime
 
class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    a="Hello"
    self.wfile.write(a.encode())
    return