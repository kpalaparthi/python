import os,os.path,time
from flask import Flask,render_template,request,send_file
from werkzeug import secure_filename
app=Flask(__name__)
UPLOAD_FOLDER = '/home/krishna/PycharmProjects/untitled/python/upload'
ALLOWED_EXTENSIONS = set(['zip','gz'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def upload_file():
    return render_template('upload.html')

def execute(month,year):
    dir='/home/krishna/PycharmProjects/untitled/python/outputs/csv'
    days=len([name for name in os.listdir(dir) if (os.path.join(dir, name))])
    os.system('pwd')
    print(days)
    os.system('./proxyreport.sh {} {} {}'.format(days,month,year))

@app.route('/uploader',methods=["GET","POST"])
def uploader():
    if request.method=='POST':
        f=request.files['file[]']
        if f and allowed_file(f.filename):
            filename=secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            os.system('rm -rf outputs/csv/*')
            os.system('unzip upload/{} -d outputs/csv'.format(filename))
            month=request.form.get('Month')
            year=request.form.get('Year')
            if month == "January":
                execute(1,year)

            elif month == "February":
                execute(2, year)

            elif month == "March":
                execute(3, year)

            elif month == "April":
                execute(4, year)

            elif month == "May":
                execute(5, year)

            elif month == "June":
                execute(6, year)

            elif month == "July":
                execute(7, year)

            elif month == "August":
                execute(8,year)

            elif month == "September":
                execute(9, year)

            elif month == "October":
                execute(10, year)

            elif month == "November":
                execute(11, year)

            elif month == "December":
                execute(12, year)

            return render_template('upcom.html',ext="zip",month=month,year=year)
        else:
            return render_template('upcom.html',ext="nzip")
@app.route('/proxyreport')
def download_csv():
    time.sleep(30)
    return send_file('outputs/csv/latest.csv',
                     mimetype='text/csv',
                     attachment_filename='proxyreport.csv',
                     as_attachment=True)

if __name__=='__main__':
    app.run()