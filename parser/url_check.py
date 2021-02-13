import requests
from requests import exceptions


class CorrectUrl:
    def __init__(self, url):
        self.url = url
        self.headers = {'user-agent': 'my-app/0.0.1'}

    def check_url(self):
        try:
            r = requests.get(self.url, headers=self.headers)
            r.raise_for_status()
            print('Successful connection!', self.url)
        except exceptions.HTTPError:
            print('Something went wrong.Incorrect URL or check your internet connection!')
            quit('Check if the address is correct')
        except exceptions.ConnectionError:
            print(f"Something went wrong. Server Error!\nCan't find {self.url}!")
            quit('Check if the address is correct')
        except exceptions.MissingSchema:
            print(f"Something went wrong. Invalid url!\nTry https://{self.url}!")
            quit('Check if the address is correct')
        except exceptions.InvalidSchema:
            print(f"Something went wrong. Invalid url {self.url}!")
            quit('Check if the address is correct')