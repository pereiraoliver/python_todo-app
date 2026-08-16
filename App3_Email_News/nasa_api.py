import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

NASA_API = os.getenv("NASA_API")

url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API}"

response = requests.get(url)

data = response.json()

st.title(data["title"])
st.image(data["url"])
st.write(data["explanation"])
