""""
Snape Robot Program
Snape program for Reddit
See https://github.com/MooseHole/SnapeRobot
"""

import os
import praw
import requests
import psycopg2
import urlparse
from random import randint
import xml.etree.ElementTree

triggerfile = "triggers.xml"
subreddit = "Ghost_Of_Snape"
#subreddit = "HarryPotter"

username = os.environ['REDDIT_USER']
password = os.environ['REDDIT_PASS']
debug = os.environ['DEBUG_MODE']

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

# Logs in
r = praw.Reddit('python:moosehole.Ghost_Of_Snape:v0.0.1 (by /u/Moose_Hole)'
                'Url: https://github.com/MooseHole/SnapeRobo t')

# Loads comments and triggers
r.login(username, password)
comments = r.get_comments(subreddit)
triggerRoot = xml.etree.ElementTree.parse(triggerfile).getroot()
triggers = triggerRoot.findall('trigger')

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

# Prints a message if the debug flag is true
def printdebug(message):
	if (debug):
		print(message)

# Responds to a comment
def respond(response):
	comment.reply(response)
	printdebug(response)


response = ""
ID = None

# Main loop
for comment in comments:
	printdebug(comment.author)

	if username == comment.author:
		continue

	cursor = conn.cursor()
	# Skip if I already replied
	cursor.execute('SELECT ID FROM "Responded" WHERE ID=\'' + comment.id + '\' LIMIT 1')
	if not cursor.rowcount:
		# Build responses to triggers
		for trigger in triggers:
			if trigger.get('string') in comment.body:
				printdebug(trigger.get('string'))
				responses = trigger.findall('response')
				responseIndex = randint(0, len(responses)-1)
				response += responses[responseIndex].text + "  "
				ID = comment.id

	cursor.close()

	if ID is not None:
		break


# If any response
if ID is not None and len(response) > 0:
	# Make sure I don't reply again
	cursor = conn.cursor()
	cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'' + ID + '\')')
	conn.commit()
	printdebug(ID)

	# Reply to the comment
	respond(response)

	cursor.close()

conn.close()
