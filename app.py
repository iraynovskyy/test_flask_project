from Flask import  Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World3!'

if __name__ == '__name__':
    app.run()