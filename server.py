import os
import random
import string
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

def random_string(length):
    return ''.join(random.choice(string.lowercase) \
            for i in range(length))

def python_logo(segment, width, height, br):
    file_in     = random_string(10) + "_in_" + ".ts"
    file_out    = random_string(10) + "_out_" + ".ts"

    with open(file_in, "wb") as handle:
        handle.write(segment.data)
    print 'width:',     width
    print 'height:',    height
    print 'bitrate:',   br

    cmd = "ffmpeg -y -i " + file_in + " -s " \
            + width + "x" + height + " " + file_out
    print cmd
    os.system(cmd)

    with open(file_out, "rb") as handle:
        trans_segment = xmlrpclib.Binary(handle.read())

    return trans_segment

server = SimpleXMLRPCServer(("localhost", 10002))
print "Listening on port 8000..."
server.register_function(python_logo, 'python_logo')
server.serve_forever()
