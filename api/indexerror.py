from flask import Flask, render_template, request, redirect, url_for, send_file
from flask_bootstrap import Bootstrap5
from io import BytesIO
import segno
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
        img = segno.make(url_link)
        name = request.form['name']
        box_size = request.form['box_size']
        fill_color = request.form['fill_color']
        back_color = request.form['back_color']
        saved_qr = name + '.png'
        img.save(dark=fill_color, light=back_color, scale=box_size)
        return send_file(saved_qr, mimetype='image/png', as_attachment=True, download_name=saved_qr)


if __name__ == '__main__':
    app.run(debug=True)