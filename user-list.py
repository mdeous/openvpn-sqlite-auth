#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sqlite3
import sys

from config import DB_PATH


if not os.path.exists(DB_PATH):
    print("ERROR: Database not found: %s" % DB_PATH)
    sys.exit(2)

db = sqlite3.connect(DB_PATH)
cursor = db.cursor()

cursor.execute("SELECT username FROM users;")
users = cursor.fetchall()

print("* OpenVPN access list:")
for user in users:
    print("  - %s" % user)
