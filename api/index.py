from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import os

app = Flask(__name__)
bootstrap = Bootstrap5(app)

home = os.path.expanduser("~")
download_path=os.path.join(home, "Downloads",)
@app.route('/', methods=['GET', 'POST'])
def home():
    title="Home || QrCode Generatopr"
    qr_message = "QRCode generated will be Saved to Filepath: "+download_path
    return render_template('home.html', title=title, qr_message=qr_message)

if __name__ == '__main__':
    app.run(debug=True)