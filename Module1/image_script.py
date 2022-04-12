#!/usr/bin/python3
"""
iterates through each file in the folder
for each file:
  rotates the image 90 deg clockwise
  resizes the image from 192X192 to 128X128
  save the image to a new folder in .jpeg format
"""
from PIL import Image
import os

os.mkdir("/opt/icons")

for image in os.listdir("images"):
    if image == ".DS_Store":
        continue
    im = Image.open("./images" + "/" + image).convert("RGB")
    new_im = im.rotate(-90).resize((128, 128))
    new_im.save("/opt/icons/" + image + ".jpg")
