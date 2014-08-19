import os
import web
import base64

urls = (
    '/\S+\.ts',     'handle_ts',
    '/\S+\.m3u8',   'handle_m3u8',
    )



def get_trans_params(full_path):
    [path, name]        = os.path.split(full_path)
    [prefix, suffix]    = name.split('.')
    [vid, width, height, br, sid] = prefix.split('_')
    orig_file = vid + '_' + sid + '.' + suffix
    return [width, height, br, sid, orig_file]


class handle_ts:
    def GET(self):
        request_file = web.ctx.path
        path = '/home/guanyu/Public/me/static' + request_file
        if os.path.exists(path):
            raise web.seeother('/static' + request_file)
        else:
            [width, height, br, sid, orig_file] = get_trans_params(request_file)
            orig_file = '/home/guanyu/Public/me/static' + '/' + orig_file
            print 'requested file:' + request_file
            print 'original file:'  + orig_file
            print 'segment id:'     + sid
            print 'width:'   + width
            print 'height:'  + height
            print 'bitrate:' + br

            cmd = "ffmpeg -i " + orig_file + " -s " \
                + width + "x" + height + " " + path
            os.system(cmd)
            raise web.seeother('/static' + request_file)
            #raise web.notfound()

class handle_m3u8:
    def GET(self):
        request_file = web.ctx.path
        path = '/home/guanyu/Public/me/static' + request_file
        if os.path.exists(path):
            raise web.seeother('/static' + request_file)
        else:
            raise web.notfound()


application = web.application(urls, globals()).wsgifunc()



