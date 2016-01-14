#!/usr/bin/env python
import os
import socket
import SimpleHTTPServer
import SocketServer

try:
    PORT = int(os.environ.get('PORT', '80'))
except Exception:
    PORT = 80

if __name__ == "__main__":
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("0.0.0.0", PORT), Handler)

    with open('index.html', 'w') as index:
        index.write(u"""
           <h1 style="text-align: center">Hello World!!!</h1>
           <h2 style="text-align: center">My IP address is %s</h2>
           <h3 style="text-align: center">Running on port %s</h3>
           """ % (
             socket.gethostbyname(socket.gethostname()), PORT
         ))

    print "Serving at 0.0.0.0:%s" % PORT
    httpd.serve_forever()
