from flask import render_template
from webapp import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', context={
        'title': 'TITLE',
        'user': 'kamerican',
    })