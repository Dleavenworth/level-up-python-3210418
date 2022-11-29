import re
import os
import urllib.request

def download_files(URL, output):
    if not os.path.exists(output):
        os.mkdir(output)

    
    cur_URL = URL
    failed = False
    while not failed:
        cur_item = re.findall(r"[a-zA-Z0-9.]+", cur_URL)[-1]
        cur_item_index = re.findall(r"[0-9]+", cur_item)
        item_name = re.findall(r"[a-zA-Z]+", cur_item)
        try:
            urllib.request.urlretrieve(
                cur_URL, os.path.join(output, cur_item))
        except OSError:
            print("No valid file here, stopping")
            failed = True
            continue
        next_index = str(int(cur_item_index[0])+1)
        num_zeros = len(re.findall(r"[0]+", cur_item_index[0])[0])
        if num_zeros > 0:
            next_item = item_name[0] + \
            ("0" * int(len(cur_item_index[0]) - len(next_index))) + next_index + "." + item_name[1]
        else:
            next_item = item_name[0] + next_index + "." + item_name[1]
        split_path = os.path.split(URL)
        cur_URL = os.path.join(split_path[0], next_item)


download_files("http://699340.youcanlearnit.net/image001.jpg",
               "src/15 Download Sequential Files/downloaded")
