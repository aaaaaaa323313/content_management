import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:9000/")
with open("dream_000_test.ts", "wb") as handle:
        handle.write(proxy.python_logo().data)
