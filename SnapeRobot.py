""""
Snape Robot Program
Snape program for Reddit
See https://github.com/MooseHole/SnapeRobot
"""

import os
import praw
import requests
import xml.etree.ElementTree

username = os.environ['REDDIT_USER']
password = os.environ['REDDIT_PASS']
#subreddit = "HarryPotter"
subreddit = "Ghost_Of_Snape"
triggerfile = "triggers.xml"
debug = False
r = null
comments = null
triggers = null

# Logs in
def login():
	r = praw.Reddit('python:moosehole.Ghost_Of_Snape:v0.0.1 (by /u/Moose_Hole)'
	                'Url: https://github.com/MooseHole/SnapeRobot')
	r.login(username, password)

# Loads comments and triggers
def load():
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
while True:
	login()
	load()

	for comment in comments:
		printdebug(comment.author)
		response = ""

		# Build responses to triggers
		for trigger in triggers.findall('comment'):
			if trigger.get('trigger') in comment.body:
				response += trigger.get('response') + "  "

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

	