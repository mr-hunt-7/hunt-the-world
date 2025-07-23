from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return {"status": "HUNT THE WORLD backend is running"}

if __name__ == '__main__':
    app.run(debug=True)
