import os
from classifier import predict
from flask import Flask, flash, request, render_template, redirect, url_for
from werkzeug import secure_filename

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/send', methods=['POST', 'GET'])
def send():
    if request.method == 'POST':
        pic = request.files['pic']
        weight = request.form['weight']
        file_name = secure_filename(pic.filename)
        pic.save(file_name)
        output = predict.main(file_name, weight)
        os.remove(file_name)
        if output == 'okay':
            output = '\U0001F44C'
        elif output == 'thumbs_up':
            output = '\U0001f44d'
        elif output == 'fingers_crossed':
            output = '\U0001F91E'
        elif output == 'hand_palm':
            output = '\u270B'
        elif output == 'peace':
            output = '\u270C'
        return render_template('prediction.html', prediction=output)

@app.route('/pretty', methods=['POST', 'GET'])
def pretty():
    if request.method == 'POST':
        pic = request.files['pic']
        weight = request.form['weight']
        file_name = secure_filename(pic.filename)
        pic.save(file_name)
        output = predict.main(file_name, weight)
        os.remove(file_name)
        if output == 'okay':
            output = '\U0001F44C'
        elif output == 'thumbs_up':
            output = '\U0001f44d'
        elif output == 'fingers_crossed':
            output = '\U0001F91E'
        elif output == 'hand_palm':
            output = '\u270B'
        elif output == 'peace':
            output = '\u270C'
        return render_template('pprediction.html', prediction=output)

    return render_template('pretty.html')

if(__name__):
    app.run(debug=True)
