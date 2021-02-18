import requests


def get_token_for_user(username, password):
    import base64
    client_id = "6S7BZRg2y03jdvIBFtenFEXllccN2bNHOjCUiIaO"
    secret = "9wAGl93xMclJW1Ia0nhk3gfU5NZsUNoVqUTZ8m9X6zOllnumMuXrKkfk1Fdlk89x7YWXgLufCxcrdnaEJd9z9vnfX4fhWC4eAMRYNS6N4B5FlU0UzDyCUXRkRopNK4nQ"
    credential = "{0}:{1}".format(client_id, secret)
    credential = base64.b64encode(credential.encode("utf-8"))
    header = {"Authorization": f"Basic {credential}"}
    url = "http://127.0.0.1:8000/o/token/"
    data = {"grant_type": "password", "username": username, "password": password, "client_id": client_id,
            "client_secret": secret}
    rest = requests.post(url, data=data, headers=header)
    print(rest.json())


get_token_for_user("wjqeqwsas", "wqdqwdwd")
