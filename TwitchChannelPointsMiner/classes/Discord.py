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
                    "username": "Kurumi",
                    "avatar_url": "https://media.discordapp.net/attachments/1233839193445372055/1249136858777124957/EBE8C940-757F-41A3-8A4A-A57B233069E0.jpg?ex=666634da&is=6664e35a&hm=35301dd880e0f32984fdd895d74c7fb3a8acdfeec509303f2634ddec55890f98&",
                },
            )
