from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/index.html')

@app.route('/index.html')
def home():
    return render_template("index.html")

@app.route('/works.html')
def works():
    return render_template("works.html")

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
