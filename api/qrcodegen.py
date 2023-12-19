from flask import request
import qrcode
import os

home = os.path.expanduser("~")
download_path=os.path.join(home, "Downloads/")

def generate_save():
    if request.method == 'POST':
        url_link = request.form['link']
        name = request.form['name']
        img = qrcode.make(url_link)
        file_path = download_path+name+'.png'
        img.save(file_path)
        return True

