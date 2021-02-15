import requests
from requests import exceptions


class CorrectUrl:
    def __init__(self, url):
        self.url = url
        self.headers = {'user-agent': 'my-app/0.0.1'}

    def check_url(self):
        try:
            r = requests.head(self.url, headers=self.headers)
            r.raise_for_status()
            print('Successful connection!', self.url)
        except exceptions.HTTPError:
            raise exceptions.HTTPError('Something went wrong.Incorrect URL or check your internet connection!'
                                       '\nCheck if the address is correct')

        except exceptions.ConnectionError:
            raise exceptions.ConnectionError(f"Something went wrong. Server Error!\nCan't find {self.url}!"
                                             f"\nCheck if the address is correct")
        except exceptions.MissingSchema:
            raise exceptions.MissingSchema(f"Something went wrong. Invalid url!\nTry https://{self.url}!"
                                           f"\n'Check if the address is correct'")

        except exceptions.InvalidSchema:
            raise exceptions.InvalidSchema(f"Something went wrong. Invalid url {self.url}!"
                                           f"\nCheck if the address is correct")