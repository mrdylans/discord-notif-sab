#!/usr/bin/python3

import sys
from discord import Webhook, RequestsWebhookAdapter


webhookUrl = ''
avatarUrl = ''
username = 'SABnzbd'
message = "{} ({}) - {}".format(sys.argv[2], sys.argv[1], sys.argv[3])

webhook = Webhook.from_url(webhookUrl, adapter=RequestsWebhookAdapter())
webhook.send(content=message, username=username, avatar_url=avatarUrl)
