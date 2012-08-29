#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sqlite3
import sys
from getpass import getpass
from hashlib import sha256

from config import DB_PATH, USERNAME_LENGTH_MIN, PASSWORD_LENGTH_MIN


if len(sys.argv) != 2:
    print "USAGE: %s <username>" % sys.argv[0]
    sys.exit(1)
if not os.path.exists(DB_PATH):
    print "ERROR: Database not found: %s" % DB_PATH

username = sys.argv[1]
if len(username) < USERNAME_LENGTH_MIN:
    print "ERROR: username must be at least %d characters long" % USERNAME_LENGTH_MIN
    sys.exit(2)

password_ok = False
while not password_ok:
    password = getpass()
    if len(password) < PASSWORD_LENGTH_MIN:
        print "ERROR: password must be at least %d characters long" % PASSWORD_LENGTH_MIN
        continue
    password_confirm = getpass('Confirm: ')
    if password == password_confirm:
        password_ok = True
    else:
        print "ERROR: passwords don't match"

password = sha256(password).hexdigest()

db = sqlite3.connect(DB_PATH)
cursor = db.cursor()
try:
    cursor.execute("INSERT INTO users VALUES (?, ?);", (username, password))
except sqlite3.IntegrityError:
    print "ERROR: user '%s' already exists" % username
    sys.exit(2)
db.commit()

print "* User %s successfully created" % username
