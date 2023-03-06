# pip install flask
import legofy
import os
from flask import Flask, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/convert')
def convert():
    file = request.files['image']
    filename = file.filename
    file.save(filename)

    size = int(request.form['size'])

    result = legofy.main(filename, size= size, palette_mode= 'px-master')

    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist")

    return result

#    return legofy.main("../assets/images/주먹밥.jpeg", size= 100, palette_mode= 'px-master')

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5002)