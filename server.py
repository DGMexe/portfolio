from flask import Flask, render_template, request, redirect, send_from_directory
import csv
import os
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('./index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), '/assets/favicon.png')


@app.route('/<string:page_name>')
def html_page(page_name=''):
    return render_template(page_name)


def write_to_csv(data):
    with open("database.csv", mode="a", newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=';')
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:  #noqa
            return 'Did not save to database... :('
    else:
        return 'Something went bad...'
