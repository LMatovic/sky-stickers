import os
import re

import requests # to get image from the web
import shutil # to save it locally

input_file = 'html_li.txt'

out_dir = os.path.dirname(__file__) + '\\' + 'stickers' + '\\'

file1 = open(os.path.dirname(__file__) + '\\' + input_file, 'r')
Lines = file1.readlines()

for line in Lines:
    res = re.findall("(?P<url>https?://[^\s]+)\"", line)
    for link in res:
        # print(link)
        filename = link.split("/")[-1].split('?v=1')[0]

        # Open the url image, set stream to True, this will return the stream content.
        r = requests.get(link, stream = True)

        # Check if the image was retrieved successfully
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True
            
            # Open a local file with wb ( write binary ) permission.
            with open(out_dir + filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
                
            print('Image sucessfully Downloaded: ',filename)
        else:
            print('Image Couldn\'t be retreived')