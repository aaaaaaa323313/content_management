import datetime
import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:10002/")

with open("dream_000.ts", "rb") as handle:
    ts = xmlrpclib.Binary(handle.read())

width   = '400'
height  = '400'
br      = '1k'

with open("dream_000_test.ts", "wb") as handle:
    handle.write(proxy.python_logo(ts, width, height, br).data)
