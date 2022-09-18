from flask import Flask, render_template

app = Flask(__name__)


@app.route("/blog")
def hello_world1():
    return render_template('blog.html')

@app.route("/single/<name>")
def hello_world7(name):
    return render_template('single.html', name=name)



if __name__ == '__main__':
    app.run()