"""
模拟账号密码登陆豆瓣

"""
import requests

class LoginDouban(object):

    def __init__(self):
        self.login_url = "https://accounts.douban.com/j/mobile/login/basic"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }

        self.login_form_data = {
            "ck": "EIXM",
            "name": "your login name",
            "password": "your password",
            "remember": "false",
            "ticket": ""
        }
        self.session = requests.session()

    def login(self):
        self.session.post(self.login_url, headers=self.headers, data=self.login_form_data)

    def visit_person_center(self):
        per_center_url = "https://www.douban.com/"
        person_center_data = self.session.get(per_center_url, headers=self.headers).content
        return person_center_data

    def save_data(self, data):

        with open("douban.html", "wb")as f:
            f.write(data)

    def run(self):
        self.login()
        center_data = self.visit_person_center()
        self.save_data(center_data)

LoginDouban().run()
