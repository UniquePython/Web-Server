from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('thankyou.html')
    else:
        return redirect('/')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n\nEmail: {email} \nSubject: {subject} \nMessage: {message}")

if __name__ == '__main__':
    app.run(debug=True)
