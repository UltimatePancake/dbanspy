import requests

class DBans(object):

    def __init__(self, **kwargs):
        if "token" not in kwargs:
            raise RuntimeError("Token not provided")

        self.token = kwargs['token']

    def lookup(self, **kwargs):
        if "id" not in kwargs:
            raise RuntimeError("User ID not provided")
        token = self.token
        payload = {
            "token": token,
            "userid": kwargs['id']
        }
        resp = requests.post("https://bans.discordlist.net/api", data=payload)
        final = resp.text
        resp.close()
        if "No token specified!" in final:
        	raise RuntimeError("Token is not provided, please create a new instance or use the Update method")
        elif "Invalid token." in final:
        	raise LookupError("The provided token is invalid, please create a new instance or use the Update method")
        else:
        	return final.lower() in ("true")


    def update(self, **kwargs):
        if "token" not in kwargs:
            raise RuntimeError("Token not provided")
        self.token = kwargs['token']