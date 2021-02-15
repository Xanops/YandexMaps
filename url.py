import requests
from url_params import server, params

server = server
params = params


def url():
    global server, params

    bytes_dannie = requests.get(server, params).content
    return bytes_dannie
