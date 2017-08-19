import aiohttp


class DBans:
    def __init__(self, **kwargs):
        if "token" not in kwargs:
            raise RuntimeError("Token not provided")
        self.token = kwargs['token']

    async def lookup(self, **kwargs):
        if "user_id" not in kwargs:
            raise RuntimeError("User ID not provided")

        payload = {
            "token": self.token,
            "userid": kwargs['user_id']
        }

        async with aiohttp.ClientSession() as session:
            async with session.post('https://bans.discordlist.net/api', data=payload) as resp:
                final = await resp.text()

        if "No token specified!" in final:
            raise RuntimeError("Token is not provided, please create a new instance or use the Update method")
        elif "Invalid token." in final:
            raise LookupError("The provided token is invalid, please create a new instance or use the Update method")
        else:
            return final.lower() in ("true")

    def update(self, token):
        if not token:
            raise RuntimeError("Token not provided")
        self.token = token
