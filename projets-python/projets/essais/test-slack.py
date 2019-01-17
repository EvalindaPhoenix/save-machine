#!/usr/bin/env python3
# -*- coding: utf8 -*-

from slackclient import SlackClient
import time
import os

# export SLACK_API_TOKEN="xoxp-..."
slack_token = os.environ["SLACK_API_TOKEN"]
channel="CF1BJLBEK"
message="Hello from Python! :tada:"

sc = SlackClient(slack_token)

#
def send_slack_message(channel, message):
    """
    Simple wrapper for sending a Slack message
    """
    return sc.api_call(
        "chat.postMessage",
        channel=channel,
        text=message
     )

# Make the API call and save results to `response`
response = send_slack_message(channel, message)

# Check to see if the message sent successfully.
# If the message succeeded, `response["ok"]`` will be `True`
if response["ok"]:
    print("Message posted successfully: " + response["message"]["ts"])
    # If the message failed, check for rate limit headers in the response
elif response["ok"] is False and response["headers"]["Retry-After"]:
    # The `Retry-After` header will tell you how long to wait before retrying
    delay = int(response["headers"]["Retry-After"])
    print("Rate limited. Retrying in " + str(delay) + " seconds")
    time.sleep(delay)
    send_slack_message(message, channel)
