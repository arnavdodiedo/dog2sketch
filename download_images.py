import os
from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

os.chdir("D:\\codes\\python\\dog2sketch\\dataset\\trainB") # download directory

arguments = {"keywords": "one dog", "limit": 100, "print_urls": False}   # change keywords according to required dataset 
paths = response.download(arguments)                                                # max limit 100 
print(paths) 
