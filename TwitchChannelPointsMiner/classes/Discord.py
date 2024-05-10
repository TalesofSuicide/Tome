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
                    "username": "Tomoe",
                    "avatar_url": "https://media.discordapp.net/attachments/1233839193445372055/1238524679514488862/jZN0Sg2.jpg?ex=663f997e&is=663e47fe&hm=45140707f8df105487e198d8bd0455b5e405d29ce460cacc9d86e31ea9253b4a&=&format=webp",
                },
            )
