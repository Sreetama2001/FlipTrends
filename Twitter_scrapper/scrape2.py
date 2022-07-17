import json
import csv
import requests,shutil
from os import path
from operator import itemgetter

def remove_duplicates(test_list):
    res_list = []
    for i in range(len(test_list)):
        if test_list[i] not in test_list[i + 1:]:
            res_list.append(test_list[i])

    return res_list

def write_json_file(dict,name):
    
    if path.isfile(f"{name}.json") is False:
        json_object = json.dumps(dict, indent=3)
        with open (f"{name}.json","w") as file:
            file.write(json_object)
    else:
        # remove_duplicates(dict)
        with open(f"{name}.json") as fp:
            listObj = json.load(fp)
            listObj.append(dict)
        remove_duplicates(listObj)
        with open(f"{name}.json", 'w') as json_file:
            json.dump(listObj, json_file, 
                        indent=4,  
                        separators=(',',': '))


def download_img(url,file_name):
    res=requests.get(url,stream=True)
    if res.status_code==200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw,f)
        print('Image sucessfully Downloaded',file_name)
    else:
        print("image couldnt be retrieved")

def in_csv():
    # with open('hashtags.csv', 'w') as f:
    pass

# sort
# after sorting in descending order on basis of trends download the image url and save it in drive in folders
# create functions for  Grocery, Fashion, Mobile, Electronics, Appliances, Beauty, Baby and toys, Furniture, sports and more
def sort__(list_to_be_sorted,name):
    newlist = sorted(list_to_be_sorted, key=itemgetter(f'{name}'), reverse=True) 
    return newlist




   










