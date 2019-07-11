import os
from flask import Flask,render_template,request
from werkzeug import secure_filename
app=Flask(__name__)
UPLOAD_FOLDER = '/home/krishna/PycharmProjects/untitled/python/upload'
ALLOWED_EXTENSIONS = set(['zip'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def upload_file():
    return render_template('upload.html')
@app.route('/uploader',methods=["GET","POST"])
def uploader():
    if request.method=='POST':
        f=request.files['file[]']
        if f and allowed_file(f.filename):
            filename=secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return 'file uploaded successfully'
        else:
            return 'Supports only zip formatted files'
if __name__=='__main__':
    app.run()