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

cursor = conn.cursor()
cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'40pw1t\')')
cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'40xe4d\')')
cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'40xfnv\')')
cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'40xi7l\')')
cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'40xips\')')
cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'40xzwf\')')
cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'40zdrc\')')
cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'40zsr7\')')
cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'40zx3w\')')
cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'410ccx\')')
cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'410o60\')')
cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'4114li\')')
cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'411n1e\')')
cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'411nbv\')')
cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'411le9\')')
cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'411trz\')')
cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'4128zu\')')
cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'412byh\')')
cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'412k9r\')')
cursor.execute('INSERT INTO "Responded" (ID) VALUES (\'4130m7\')')

conn.commit()
cursor.close()

conn.close()
