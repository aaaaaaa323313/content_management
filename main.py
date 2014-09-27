import os
import web
import time
import redis
import base64
import datetime
import xmlrpclib

urls = (
    '/\S+\.ts',     'handle_ts',
    '/\S+\.m3u8',   'handle_m3u8',
    )

def get_trans_params(full_path):
    [path, name]        = os.path.split(full_path)
    [prefix, suffix]    = name.split('.')
    [vid, width, height, br, sid] = prefix.split('_')
    orig_file = vid + '_' + sid + '.' + suffix
    return [vid, width, height, br, sid, orig_file]


class handle_ts:

    def offloading(self, orig_file, width, height, br, path):
        proxy = xmlrpclib.ServerProxy("http://155.69.55.92:10002/")
        with open(orig_file, "rb") as handle:
            segment = xmlrpclib.Binary(handle.read())
        with open(path, "wb") as handle:
            handle.write(proxy.python_logo(segment, width, height, br).data)


    def GET(self):
        vid     = ''
        width   = ''
        height  = ''
        br      = ''
        sid     = ''
        path    = ''
        orig_file = ''

        request_file = web.ctx.path
        #print request_file
        r_cache.incr(request_file)

        cnt = request_file.count('_')

        value = r_cache.incr('overall_request_number')
        print "total requests:", value

        if cnt == 4:
            [vid, width, height, br, sid, orig_file] = get_trans_params(request_file)
            path = '/home/guanyu/Public/me/static/' + vid + request_file

            if os.path.exists(path):
                raise web.seeother('/static/' + vid  + request_file)
            else:
                orig_file = '/home/guanyu/Public/me/static/' + vid + '/' + orig_file
                print 'requested file:' + request_file
                print 'original file:'  + orig_file
                print 'segment id:'     + sid
                print 'width:'   + width
                print 'height:'  + height
                print 'bitrate:' + br

                value = r_cache.get("trans_queue")
                value = int(value)
                print 'current transcoding size', value

                if value >= 2:
                    print 'offloading'
                    self.offloading(orig_file, width, height, br, path)
                else:
                    print 'online transcoding'
                    r_cache.incr("trans_queue")
                    cmd = "ffmpeg -i " + orig_file + " -s " \
                            + width + "x" + height + " " + path
                    os.system(cmd)
                    r_cache.decr("trans_queue")

                r_cache.incr('overall_transcoding_number')
                t = time.time()
                r_cache.sadd('transcoding_times', t)
                raise web.seeother('/static/' + vid + request_file)

        #the original bitrate file
        elif cnt == 1:
            vid = request_file.split('_')[0]
            path = '/home/guanyu/Public/me/static' + vid + request_file
            if os.path.exists(path):
                raise web.seeother('/static' + vid + request_file)
            else:
                raise web.notfound()
        else:
            raise web.notfound()



class handle_m3u8:
    def GET(self):
        request_file = web.ctx.path
        [orig_file, postfix] = request_file.split('.')

        path = '/home/guanyu/Public/me/static/' + orig_file + '/' + request_file
        if os.path.exists(path):
            raise web.seeother('/static/' + orig_file + '/' + request_file)
        else:
            raise web.notfound()


r_cache = redis.StrictRedis(host='localhost', port=6379, db=0)
application = web.application(urls, globals()).wsgifunc()
print 'the server has quited'


