from textwrap import dedent

import requests

from TwitchChannelPointsMiner.classes.Settings import Events


class Discord(object):
    __slots__ = ["webhook_api", "events"]

    def __init__(self, webhook_api: str, events: list):
        self.webhook_api = webhook_api
        self.events = [str(e) for e in events]

    def send(self, message: str, event: Events) -> None:
        if str(event) in self.events:
            requests.post(
                url=self.webhook_api,
                data={
                    "content": dedent(message),
                    "username": "$ui the buttler",
                    "avatar_url": "https://media.discordapp.net/attachments/1233839193445372055/1255550278833274960/IMG_3197.jpg?ex=66842151&is=6682cfd1&hm=b42b35ba452889b3dc07da88bd8d9b5fe409efa18c57b772491986aa0decd85d&=&format=webp&width=709&height=993",
                },
            )
