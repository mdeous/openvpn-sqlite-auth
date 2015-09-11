# -*- coding: utf-8 -*-

# Path where users database should be stored
DB_PATH = '/tmp/openvpn-auth-test.sqlite'
# Minimum required length for passwords when creating users
PASSWORD_LENGTH_MIN = 8
# Hash algorithm to use for passwords storage. Can be one of:
# md5, sha1, sha224, sha256, sha384, sha512
HASH_ALGORITHM = 'sha256'
