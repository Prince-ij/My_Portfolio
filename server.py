from flask import Flask, render_template, request, flash, redirect
import requests
import os
import yagmail


app = Flask(__name__)
app.secret_key = os.urandom(24)
YAGMAIL_KEY = os.environ.get('YAGMAIL_KEY')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/blogs')
def blogs():
    response = requests.get('https://api.npoint.io/d3ce57714d3de69d5424')
    blogs = response.json()
    return render_template('blogs.html', blogs=blogs)

@app.route('/blog/<int:id>')
def blog(id):
    response = requests.get('https://api.npoint.io/d3ce57714d3de69d5424')
    blogs = response.json()
    blog = next((b for b in blogs if b["id"] == id), None)
    return render_template('blog.html', blog=blog)

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact_me():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        msg = request.form['msg']

    referrer = request.referrer

    message = f"Name: {name}\nEmail: {email}\nBODY:\n{msg}"
    yag = yagmail.SMTP("baaby.dudu@gmail.com", YAGMAIL_KEY)
    yag.send("princeij56@gmail.com", "From Your Blog Contact Form", message)

    flash('Message successfully sent !', 'success')
    if referrer:
        return redirect(referrer)

    return render_template('home.html')


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
