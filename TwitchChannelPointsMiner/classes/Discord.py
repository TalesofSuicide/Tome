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
                    "avatar_url": "https://media.discordapp.net/attachments/1233839193445372055/1249032251635929108/image0.jpg?ex=6665d36e&is=666481ee&hm=23f37baa0ac4155773255e906d1580c9b2d32f77091e2cf0c6ed8aae244a6ccd&=&format=webp",
                },
            )
