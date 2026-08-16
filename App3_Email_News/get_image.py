import requests

url = "https://images.pexels.com/photos/8591716/pexels-photo-8591716.jpeg"

request = requests.get(url)

with open("cross.jpg", "wb") as file:
    file.write(request.content)
