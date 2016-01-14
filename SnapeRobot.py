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

cursor = conn.cursor()

# Login
r = praw.Reddit('python:moosehole.Ghost_Of_Snape:v0.0.1 (by /u/Moose_Hole)'
                'Url: https://github.com/MooseHole/SnapeRobot')
r.login(os.environ['REDDIT_USER'], os.environ['REDDIT_PASS'])
comments = r.get_comments('Slytherin')

# Main loop
for comment in comments:
	response = ""
	replied = false
	replies = r.get_submission(comment.permalink).comments
	for reply in replies:
		if reply.author == os.environ['REDDIT_USER']:
			replied = true;

	if replied:
		continue


	if "James Potter" in comment.body and :
		response += "That swine.  "

	if len(response) > 0:
		comment.reply(response)
