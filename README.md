# OpenVPN SQLite Authentication

openvpn-sqlite-auth is a set of Python scripts to enable and manage OpenVPN user authentication,
using SQLite to store credentials.

## Setup:

- Clone `openvpn-sqlite-auth` into your OpenVPN configuration folder:

    git clone https://github.com/mattoufoutu/openvpn-sqlite-auth.git /etc/openvpn/openvpn-sqlite-auth

- Edit the `config.py` file and set the appropriates values
    - `DB_PATH`: Path where the SQLite database should be stored.
    - `PASSWORD_LENGTH_MIN`: Minimum length passwords should be.
    - `HASH_ALGORITHM`: Algorithm to use when hashing passwords. Can be one of:
        - md5
        - sha1
        - sha224
        - sha256
        - sha384
        - sha512
        - or any other algorithm supported by the OpenSSL library used by your Python installation.

- Edit your OpenVPN server configuration file and add this line:

    auth-user-pass-verify /etc/openvpn/openvpn-sqlite-auth/user-auth.py via-env

- Edit your OpenVPN user configuration file and add this line:

    auth-user-pass

- Create the users database using the provided script:

    ./createdb.py

## Utilities:

  - `./user-add.py <username>`: Add a new user to the database.
  - `./user-del.py <username>`: Remove an user from the database.
  - `./user-list.py`: List registered users.
