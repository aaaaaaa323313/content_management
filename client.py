import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:9000/")
with open("dream_000.ts", "rb") as handle:
    ts = xmlrpclib.Binary(handle.read())
with open("dream_000_test.ts", "wb") as handle:
        handle.write(proxy.python_logo(ts).data)
