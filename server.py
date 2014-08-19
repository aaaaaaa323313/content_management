from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib

def python_logo(ts):
    #with open("dream_000.ts", "rb") as handle:
    #    return xmlrpclib.Binary(handle.read())
    return ts

server = SimpleXMLRPCServer(("localhost", 10002))
print "Listening on port 8000..."
server.register_function(python_logo, 'python_logo')
server.serve_forever()
