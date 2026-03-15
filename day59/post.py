import requests

class Post:
    def __init__(self):
        self.url='https://api.npoint.io/c790b4d5cab58020d391'
        
    def request(self):
        posts=requests.get(url=self.url).json()
        return posts
