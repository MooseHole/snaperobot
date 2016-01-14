""""
Snape Robot Program
Snape program for Reddit
See https://github.com/MooseHole/SnapeRobot
"""

import os
import praw
import requests
from random import randint
import xml.etree.ElementTree

username = os.environ['REDDIT_USER']
password = os.environ['REDDIT_PASS']
subreddit = "Ghost_Of_Snape"
#subreddit = "HarryPotter"
triggerfile = "triggers.xml"
debug = False

# Logs in
r = praw.Reddit('python:moosehole.Ghost_Of_Snape:v0.0.1 (by /u/Moose_Hole)'
                'Url: https://github.com/MooseHole/SnapeRobo t')
r.login(username, password)

# Loads comments and triggers
comments = r.get_comments(subreddit)
triggers = xml.etree.ElementTree.parse(triggerfile).getroot()


# Prints a message if the debug flag is true
def printdebug(message):
	if (debug):
		print(message)

# Responds to a comment
def respond(response):
	comment.reply(response)
	printdebug(response)

# Main loop
for comment in comments:
	printdebug(comment.author)
	response = ""
	# Build responses to triggers
	for trigger in triggers.findall('trigger'):
		if trigger.get('string') in comment.body:
			responses = trigger.findall('response')
			responseIndex = randint(0, len(responses)-1)
			response += responses[responseIndex].text + "  "

	# If any response
	if len(response) > 0:
		# Skip if I already replied
		replied = False
		replies = r.get_submission(comment.permalink).comments
		for reply in replies:
			if reply.author == username:
				replied = True
				break
		if replied:
			continue

		# Reply to the comment
		respond(response)

	