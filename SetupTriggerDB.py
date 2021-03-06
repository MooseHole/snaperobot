""""
First time setup for database
"""

import os
import praw
import requests
import psycopg2
import urlparse
from random import randint
import xml.etree.ElementTree

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

cursor = conn.cursor()

cursor.execute('DROP TABLE "Triggers"')
conn.commit()

cursor.execute('CREATE TABLE "Triggers" (id BIGSERIAL PRIMARY KEY, Trigger varchar(255) not null, Response varchar(255) not null)')
conn.commit()

cursor.close()

conn.close()
