import requests
from requests_html import HTMLSession


def creer_session():
    url = "https://www.frenchlearner.com/expressions/"
    try:
        session = HTMLSession()
        global reponse
        reponse = session.get(url)
        return reponse
    except requests.exceptions.RequestException as e:
        print(e)
        return None