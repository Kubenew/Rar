import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/archive', methods=['POST'])
def archive():
    archive_path = request.form['archive_path']
    file_path = request.form['file_path']
    password1 = request.form['password1']
    password2 = request.form['password2']
    
    if archive_path and file_path and password1 and password2:
        os.system(f'rar a -p{password1} -hp{password2} {archive_path} {file_path}')
        return render_template('result.html', result='File archived successfully.')
    else:
        return render_template('result.html', result='Please fill all fields.')

@app.route('/extract', methods=['POST'])
def extract():
    archive_path = request.form['archive_path']
    extract_path = request.form['extract_path']
    password1 = request.form['password1']
    password2 = request.form['password2']
    
    if archive_path and extract_path and password1 and password2:
        os.system(f'unrar x -p{password1} -hp{password2} {archive_path} {extract_path}')
        return render_template('result.html', result='File extracted successfully.')
    else:
        return render_template('result.html', result='Please fill all fields.')

if __name__ == '__main__':
    app.run(debug=True)
