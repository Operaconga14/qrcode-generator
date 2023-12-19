from flask import Flask, render_template, request, redirect, url_for, send_file
from flask_bootstrap import Bootstrap5
from io import BytesIO
import segno

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
        box_size = request.form['box_size']
        fill_color = request.form['fill_color']
        back_color = request.form['back_color']
        save_file = name + '.png'
        qr = segno.make(url_link)
        byte_io = BytesIO()
        qr.save(byte_io, dark=fill_color, light=back_color, scale=box_size, kind='png')
        byte_io.seek(0)
        return send_file(byte_io, mimetype='image/png', as_attachment=True, download_name=save_file)


if __name__ == '__main__':
    app.run(debug=True)