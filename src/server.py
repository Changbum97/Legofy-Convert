import legofy
import os
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r'*': {'origins': '*'}})

@app.route('/convert', methods=['POST', 'GET'])
def convert():
    print("==========start==========")
    print(request.form)
    print(request.files)
    #file = request.files['imageFile']
    file = request.files.get('imageFile', False)
    print(file)
    filename = file.filename
    print(filename)
    file.save(filename)

    size = int(request.form['size'])

    result = legofy.main(filename, size= size, palette_mode= 'px-master')

    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist")

    print("==========end==========")
    return result

#    return legofy.main("../assets/images/주먹밥.jpeg", size= 100, palette_mode= 'px-master')

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5002)