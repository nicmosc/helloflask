from flask import Flask, render_template
app = Flask(__name__)

@app.route("/~Nicola/www/MSC-Project/CommunicationTests/helloflask/")
def hello():
    #return "Hello World!"
    return render_template('hello.html')

if __name__ == "__main__":
    app.run()