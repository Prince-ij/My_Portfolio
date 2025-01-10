from flask import Flask, render_template
import requests

app = Flask(__name__)

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

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)

