""""
Snape Robot Program
Snape program for Reddit
See https://github.com/MooseHole/SnapeRobot
"""

import os
import praw
import requests

# Login
r = praw.Reddit('python:moosehole.Ghost_Of_Snape:v0.0.1 (by /u/Moose_Hole)'
                'Url: https://github.com/MooseHole/SnapeRobot')
r.login(os.environ['REDDIT_USER'], os.environ['REDDIT_PASS'])
comments = r.get_comments('Slytherin')

# Main loop
for comment in comments:
	response = ""

	# Build responses to triggers
	if "James Potter" in comment.body:
		response += "That swine.  "


	# If any response
	if len(response) > 0:
		# Skip if I already replied
		replied = 0
		replies = r.get_submission(comment.permalink).comments
		for reply in replies:
			if reply.author == os.environ['REDDIT_USER']:
				replied = 1
				break
		if replied:
			continue

		# Reply to the comment
		comment.reply(response)
