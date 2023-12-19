from flask import Flask, render_template, request, redirect, url_for, send_file
from flask_bootstrap import Bootstrap5
from io import BytesIO
import qrcode
import os

app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    title="Home || QrCode Generatopr"
    qr_message = "QRCode generated will be Saved to your Computer"
    return render_template('home.html', title=title, qr_message=qr_message)

@app.route('/makeQR', methods=['GET', 'POST'])
def makeQr():
    if request.method == 'POST':
        url_link = request.form['link']
        name = request.form['name']
        img=qrcode.make(url_link)
        saved_qr=name+'.png'
        img_bytes_io = BytesIO()
        img.save(img_bytes_io)
        img_bytes_io.seek(0)
        return send_file(img_bytes_io, mimetype='image/png', as_attachment=True, download_name=saved_qr)


if __name__ == '__main__':
    app.run(debug=True)