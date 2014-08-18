from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib

def python_logo():
    with open("dream_000.ts", "rb") as handle:
        return xmlrpclib.Binary(handle.read())

server = SimpleXMLRPCServer(("localhost", 9000))
print "Listening on port 8000..."
server.register_function(python_logo, 'python_logo')
server.serve_forever()
