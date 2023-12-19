from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
import qrcode
import os

app = Flask(__name__)
bootstrap = Bootstrap5(app)

home = os.path.expanduser("~")
download_path=os.path.join(home, "Downloads/",)
file_path = download_path
@app.route('/', methods=['GET', 'POST'])
def home():
    title="Home || QrCode Generatopr"
    qr_message = "QRCode generated will be Saved to Filepath: "+download_path
    return render_template('home.html', title=title, qr_message=qr_message)

@app.route('/makeQR', methods=['GET', 'POST'])
def makeQr():
    if request.method == 'POST':
        url_link = request.form['link']
        name = request.form['name']
        img=qrcode.make(url_link)
        img.save(file_path+name+'.png')
        success_message="Saves Successful"
        saved_qr=name+'.png'
        return redirect(url_for('home', success_message=success_message, saved_qr=saved_qr))


if __name__ == '__main__':
    app.run(debug=True)