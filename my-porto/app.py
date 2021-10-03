from flask import Flask, render_template, request, redirect, url_for,send_file
import csv

app= Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']
        message=request.form['message']
        with open('db.csv', 'w', newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow({name},{email},{message})
        return redirect(url_for('thanks'))
    else:
        return "Something went wrong"

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/download')
def download_file():
	path = "resume.pdf"
	return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)


