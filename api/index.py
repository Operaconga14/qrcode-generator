from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from qrcodegen import generate_save
import os

app = Flask(__name__)
bootstrap = Bootstrap5(app)

home = os.path.expanduser("~")
download_path=os.path.join(home, "Downloads",)
@app.route('/', methods=['GET', 'POST'])
def home():
    if generate_save():
        success_message = "Succefully Filepath: "+download_path
        return redirect(url_for('home', success_message=success_message))
    title="Home || QrCode Generatopr"
    qr_message = "QRCode generated will be Saved to Filepath: "+download_path
    return render_template('home.html', title=title, qr_message=qr_message)

# @app.route('/about')
# def about():
#     return 'About'

if __name__ == '__main__':
    app.run(debug=True)