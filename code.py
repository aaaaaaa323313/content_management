import os
import web
import base64

urls = (
    '/\S+\.ts',     'handle_ts',
    '/\S+\.m3u8',   'handle_m3u8',
    )

def get_trans_params(file_name):




class handle_ts:
    def GET(self):
        request_file = web.ctx.path
        path = '/home/guanyu/Public/me/static' + request_file
        if os.path.exists(path):
            raise web.seeother('/static' + request_file)
        else:
            raise web.notfound()

class handle_m3u8:
    def GET(self):
        request_file = web.ctx.path
        path = '/home/guanyu/Public/me/static' + request_file
        if os.path.exists(path):
            raise web.seeother('/static' + request_file)
        else:
            raise web.notfound()


application = web.application(urls, globals()).wsgifunc()
