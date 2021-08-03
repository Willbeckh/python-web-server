import http.server
import socketserver

#the port at which the server will be listening to requests
HOST = ""
PORT = 8000

#handler for http requests
Handler = http.server.SimpleHTTPRequestHandler

#run the server
with socketserver.TCPServer((HOST, PORT), Handler) as http:
  print("Server running at port: ", PORT)
  print("Open at: 'localhost:8000' ")
  http.serve_forever()
  