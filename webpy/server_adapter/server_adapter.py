import requests


class Server_Adapter():

    def call(self, path, **kwargs):
        root_url = 'http://localhost:8080/'
        response = requests.post(url=root_url + path, data=kwargs)
        return eval(response.content)

    def login(self, **kwargs):
        path = 'login'
        return self.call(path=path, **kwargs)

    def sign(self, **kwargs):
        path = 'sign'
        return self.call(path=path, **kwargs)

    def books(self, **kwargs):
        path = 'books'
        return self.call(path=path, **kwargs)

    def update_book(self, **kwargs):
        path = 'update_book'
        return self.call(path=path, **kwargs)