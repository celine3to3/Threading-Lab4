import requests
class FileStream:
    def __init__(self, url):
        self.url = url

    def retrieve_data(self):
        data = requests.get(self.url)
        return data