from urllib.parse import urlencode
from urllib.request import urlopen, Request

# GET
http_response = urlopen("http://www.example.com?a=10&b=20")
body = http_response.read()
print(body)

# POST
data = {
    "email": "sunguk3391@gmail.com",
    "password": "1234",
    "name": "전성욱"
}
data = urlencode(data).encode("utf-8")

request = Request("http://www.example.com", data)
request.add_header("content-type", "text/html")

http_response = urlopen(request)
print(http_response.read())