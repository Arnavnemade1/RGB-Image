import numpy as np

import pandas as pd

from PIL import Image

%pip install openpyxl

 

#load an image

#image must be in the notebooks folder to be able to call

#img = Image.open('/drive/notebooks/tiger_lily_for_edge_detection.jpg')

img = Image.open('tiger_lily_for_edge_detection.jpg')

 

img = img.convert('RGB')

 

img = np.asarray(img)

 

#print(img)

 

print(img[1][1][1])

print(len(img))

print(len(img[1]))

 

 

reds = np.zeros((533,800))

greens = np.zeros((533,800))

blues = np.zeros((533,800))

 

for i in range(len(img)):

    for j in range(len(img[1])):

        reds[i][j] = img[i][j][0]

 

print(reds)

 

for i in range(len(img)):

    for j in range(len(img[1])):

        greens[i][j] = img[i][j][1]

 

print(greens)

 

for i in range(len(img)):

    for j in range(len(img[1])):

        blues[i][j] = img[i][j][2]

 

print(blues)

 

dr = pd.DataFrame(reds)

dg = pd.DataFrame(greens)

db = pd.DataFrame(blues)

 

# 3. Export the DataFrame to an Excel (.xlsx) file

output_reds = "red_data.xlsx"

print(f"Writing data to {output_reds}...")

output_greens = "green_data.xlsx"

print(f"Writing data to {output_greens}...")

output_blues = "blue_data.xlsx"

print(f"Writing data to {output_blues}...")

 

# index=False prevents writing the row numbers into the first column

dr.to_excel(output_reds, index=False, engine='openpyxl')

dr.to_excel(output_greens, index=False, engine='openpyxl')

dr.to_excel(output_blues, index=False, engine='openpyxl')

 

print("Done! Excel files successfully created.")

