import web
import json

urls = (
    '/(.*)', 'Hello',  # (.*) is parameter in regular expression url.
)


# web.input() == a dict(), you can get any GET/POST parameter data from it.
class Hello:
    def GET(self, para_from_url):
        print para_from_url
        print web.input()    # get parameter from  url?id=1
        return json.dumps({"hello": 'get'})

    def POST(self):
        print web.input()    # get parameter from  post data
        return json.dumps({"hello": 'post'})

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
