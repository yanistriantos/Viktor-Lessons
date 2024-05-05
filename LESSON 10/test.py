import requests

# write the content of the response to the file as bytes. Currently it does not work! Look at the error message.
res = requests.get("https://www.google.com")
if res.status_code == 200:
    with open("google.html", "w") as file:
        file.write(res.content)
