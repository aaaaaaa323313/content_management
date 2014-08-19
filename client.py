import datetime
import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:10002/")
print "okey -1"
with open("dream_000.ts", "rb") as handle:
    ts = xmlrpclib.Binary(handle.read())
    print "okey -2"

with open("dream_000_test.ts", "wb") as handle:
    handle.write(proxy.python_logo(ts).data)
