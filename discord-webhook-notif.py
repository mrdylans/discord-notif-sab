#!/usr/bin/python3

import sys
from discord import SyncWebhook


webhookUrl = ''
avatarUrl = ''
username = 'SABnzbd'
message = "{} ({}) - {}".format(sys.argv[2], sys.argv[1], sys.argv[3])

webhook = SyncWebhook.from_url(webhookUrl)
webhook.send(content=message, username=username, avatar_url=avatarUrl)
