from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/my-link/')
def my_link():
    print("works")
    return 'click'

@app.route('/profile/<username>')
def profile(username):
    return username * 5

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "<h2>Post ID is %s<h2>" % post_id


if __name__ == '__main__':
    app.run(debug=True)