import requests
import os
import random
from urllib import request
import pandas as pd
from PIL import Image
from IPython.display import display

# Read the list of image URLs from an Excel sheet
df = pd.read_excel('images.xlsx')
#Excel  colon name
url_list = df['IMAGE URL'].tolist()


filename_list = ["lotto1.png",
                 "lotto2.png",
                 "lotto3.png",
                 "lotto4.png",
                 "lotto5.png",
                 "lotto6.png",
                 "lotto7.png",
                 "lotto8.png",
                 "lotto9.png",
                 "lotto10.png",
                 "lotto11.png",
                 "lotto12.png",
                 "lotto13.png",
                 "lotto14.png",
                 "lotto15.png",
                 "lotto16.png",
                 "lotto17.png",
                 "lotto18.png",
                 "lotto19.png",
                 "lotto20.png",
                 "lotto21.png",
                 "lotto22.png",
                 "lotto23.png",
                 "lotto24.png",
                 "lotto25.png",
                 "lotto26.png",
                 "lotto27.png",
                 "lotto28.png",
                 "lotto29.png",
                 "lotto30.png",
                 "lotto31.png",
                 "lotto32.png",
                 "lotto33.png",
                 "lotto34.png",
                 "lotto35.png",
                 "lotto36.png",
                 "lotto37.png",
                 "lotto38.png",
                 "lotto39.png",
                 "lotto40.png",
                 "lotto41.png",
                 "lotto42.png",
                 "lotto43.png",
                 "lotto44.png",
                 "lotto45.png",
                 "lotto46.png",
                 "lotto47.png",
                 "lotto48.png",
                 "lotto49.png",
                 "lotto50.png",
                 "lotto51.png",
                 "lotto52.png",
                 "lotto53.png",
                 "lotto54.png",

                 ]

for url, filename in zip(url_list, filename_list):
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print("Image downloaded and saved as", filename)
    else:
        print("Failed to download image from", url)
