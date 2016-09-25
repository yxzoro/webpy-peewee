# ---------------------------------------http://webpy.org/------------------------------------------ #

import web

urls = (
    '/(.*)', 'Test',
)

app = web.application(urls, globals())


class Test:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name


if __name__ == "__main__":
    app.run()
