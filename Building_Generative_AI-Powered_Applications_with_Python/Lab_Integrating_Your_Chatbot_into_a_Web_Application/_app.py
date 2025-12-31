from flask import Flask
from flask_cors import CORS     # newly added

app = Flask(__name__)
CORS(app)               # newly added

@app.route('/')
def home():
    return 'Hello, World!'

# @app.route('/bananas')
# def bananas():
#     return 'This page has bananas!'
    
# @app.route('/bread')
# def bread():
#     return 'This page has bread!'

if __name__ == '__main__':
    app.run()