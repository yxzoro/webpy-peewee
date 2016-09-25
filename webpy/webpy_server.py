# ---------------------------------------http://webpy.org/------------------------------------------ #

import web
import json

urls = (
    '/(.*)', 'Test',
)

app = web.application(urls, globals())


class Test:
    def GET(self, name):
        if not name:
            name = 'World'
        return json.dumps({"hello":name})


if __name__ == "__main__":
    app.run()
