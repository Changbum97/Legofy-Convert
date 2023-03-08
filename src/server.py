import legofy
import os
import uuid
from flask import Flask, request
from flask_cors import CORS

from src import palettes

app = Flask(__name__)
CORS(app, resources={r'*': {'origins': '*'}})

@app.route('/convert', methods=['POST', 'GET'])
def convert():
    print("==========start==========")
    file = request.files.get('imageFile', False)
    size = int(request.form['size'])

    ext = os.path.splitext(file.filename)[1]
    uuid_filename = str(uuid.uuid4()) + ext

    file.save(uuid_filename)

    result = legofy.main(uuid_filename, size= size, palette_mode= 'px-master')

    # 변환 끝난 원본 이미지 제거
    if os.path.exists(uuid_filename):
        os.remove(uuid_filename)
    else:
        print("The file does not exist")

    print("==========end==========")
    print(result.replace(".png", ""))
    return result.replace(".png", "")

#    return legofy.main("../assets/images/주먹밥.jpeg", size= 100, palette_mode= 'px-master')

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5002)