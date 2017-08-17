from app import app
from flask import render_template
from app.models import Post

@app.route('/')
def index():
    return render_template(
        'welcome.html',
        title = 'Welcome'
    )

@app.route('/home')
def home():
    return render_template(
        'base.html',
        title = 'Home'
    )


@app.route('/post/<string:title>')
def read_more(title):
    post = Post.objects.get_or_404(title=title)
    return render_template('read_more.html', title="Post", post=post)

@app.route('/archive')
def archive():
    posts = Post.objects.all()
    return render_template('archive.html', title='Archive', posts=posts)