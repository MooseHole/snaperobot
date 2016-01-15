""""
Snape Robot Program
Snape program for Reddit
See https://github.com/MooseHole/SnapeRobot
"""

import os
import praw
import requests
import psycopg2
from random import randint
import xml.etree.ElementTree

triggerfile = "triggers.xml"
#subreddit = "Ghost_Of_Snape"
subreddit = "HarryPotter"

username = "Ghost_Of_Snape"
password = "fucker"
debug = True



# Logs in
r = praw.Reddit('python:moosehole.Ghost_Of_Snape:v0.0.1 (by /u/Moose_Hole)'
                'Url: https://github.com/MooseHole/SnapeRobo t')

# Loads comments and triggers
r.login(username, password)
comments = r.get_comments(subreddit)
triggerRoot = xml.etree.ElementTree.parse(triggerfile).getroot()
triggers = triggerRoot.findall('trigger')

# Prints a message if the debug flag is true
def printdebug(message):
	if (debug):
		print(message)

# Responds to a comment
def respond(response):
#	comment.reply(response)
	printdebug(response)


response = ""
ID = None

# Main loop
for comment in comments:
	printdebug(comment.author)

	if username == comment.author:
		continue

	# Skip if I already replied
	# Build responses to triggers
	for trigger in triggers:
		if trigger.get('string') in comment.body:
			printdebug(trigger.get('string'))
			responses = trigger.findall('response')
			responseIndex = randint(0, len(responses)-1)
			response += responses[responseIndex].text + "  "
			ID = comment.id
			printdebug(comment.submission.id)
			printdebug(comment.permalink)


	if ID is not None:
		break



