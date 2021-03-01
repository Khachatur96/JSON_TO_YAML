import json
import os
import threading
import requests


image_urls = {}

my_list = []

with open('task_urls.json','rb') as data_file:
    image_urls = json.load(data_file)


for i in image_urls['items']:
    my_list.append(i['url'])


def download_image(url, name):

    try:
        img_bytes = requests.get(url).content
    except requests.exceptions.ConnectionError:
        print('Internet connection was interrupted')
        return

    with open(name,'wb') as img_file:
        img_file.write(img_bytes)

        print(f'{name} was downloaded...')


file_dir = os.path.join('web_images')

try:
    os.mkdir(file_dir)
    os.chdir(file_dir)
    thread_list = []
    file = 1

    for url in my_list:
        name = str(file)+ ".png"
        t1 = threading.Thread(target=download_image, args=(url, name))
        thread_list.append(t1)
        t1.start()
        file += 1

    for thread in thread_list:
        thread.join()


except OSError:
    print (F"Creation of the directory {file_dir} failed")

else:
    if  os.path.exists(file_dir) and len(os.listdir(file_dir)) == 0:
            print(F'{file_dir} cannot be empty')
            os.rmdir(file_dir)
    else: 
        print (F"Successfully created the directory {file_dir}" )