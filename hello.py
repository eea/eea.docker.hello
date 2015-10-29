#!/usr/bin/env python
import socket
import SimpleHTTPServer
import SocketServer

if __name__ == "__main__":
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("0.0.0.0", 80), Handler)

    with open('index.html', 'w') as index:
        index.write(u"""
           <h1 style="text-align: center">Hello World!!!</h1>
           <h2 style="text-align: center">My IP address is %s</h2>""" % (
             socket.gethostbyname(socket.gethostname())
         ))

    print "Serving at 0.0.0.0:80"
    httpd.serve_forever()
