#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hashlib import sha256
import os
import sqlite3
import sys

from config import DB_PATH


conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute('SELECT * FROM users WHERE username = ?', (os.environ['username'],))
result = cursor.fetchone()
if result is None:
    sys.exit(1)
username, password = result
if sha256(os.environ['password']).hexdigest() != password:
    sys.exit(1)
sys.exit(0)
