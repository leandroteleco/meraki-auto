from flask import Flask, render_template, request
from decouple import config
import pandas as pd

app = Flask(__name__)

@app.route('/')
def upload():
    return render_template('upload-excel.html')

@app.route('/view', methods=['POST'])
def view():
    file = request.files['file']
    file.save(file.filename)
    data = pd.read_excel(file)
    return data.to_html()

if __name__ == '__main__':
    app.run(debug=True)
