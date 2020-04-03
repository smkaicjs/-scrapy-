import requests
class Proxy_helper(object):
    def __init__(self):
        self.proxy = self.get_proxy_from_xxx()
    def get_proxy(self):
        return self.proxy
    def update_proixy(self,proxy):
        if proxy == self.proxy:
            print('获取了一个新代理')
            self.proxy = self.get_proxy_from_xxx()
    def get_proxy_from_xxx(self):
        url = ''
        response = requests.get(url)
        return 'http://' + response.text.strip()