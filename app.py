from flask import Flask
from flask import jsonify

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/api', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello, world!'})

if __name__ == '__main__':
    app.run(debug=True)