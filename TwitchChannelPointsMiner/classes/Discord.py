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
                    "username": "Era",
                    "avatar_url": "https://media.discordapp.net/attachments/1233839193445372055/1244473078579204167/IMG_1618.jpg?ex=66553d5f&is=6653ebdf&hm=84b4f140621174976385516212c773cd992bb56e7493f67b9117fbcd660c80d5&=&format=webp&width=749&height=936",
                },
            )
