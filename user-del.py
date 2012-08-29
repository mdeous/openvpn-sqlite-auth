#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sqlite3
import sys

from config import DB_PATH


if len(sys.argv) != 2:
    print "USAGE: %s <username>" % sys.argv[0]
    sys.exit(1)
if not os.path.exists(DB_PATH):
    print "ERROR: Database not found: %s" % DB_PATH
    sys.exit(2)

username = sys.argv[1]
db = sqlite3.connect(DB_PATH)
cursor = db.cursor()
cursor.execute("DELETE FROM users WHERE username = ?", (username,))
db.commit()
print "* User '%s' successfully removed" % username
