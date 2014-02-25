#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import os
import sqlite3
import sys

from config import DB_PATH, HASH_ALGORITHM


hash_func = getattr(hashlib, HASH_ALGORITHM)
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute('SELECT * FROM users WHERE username = ?;', (os.environ['username'],))
result = cursor.fetchone()
if result is None:
    sys.exit(1)
username, password = result
if hash_func(os.environ['password'].encode("utf-8")).hexdigest() != password:
    sys.exit(1)
sys.exit(0)
