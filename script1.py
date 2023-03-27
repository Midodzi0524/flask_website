from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return 'Homepage content goes here'

@app.route('/about/')
def about():
    return 'about content goes here'

if __name__ == '__main__':
    app.run(debug=True)