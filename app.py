from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return render_template("/index.html")


@app.route("/about")
def about() -> str:
    # return render_template("/about.html", company_name="beep beep mcgee inc")
    return render_template("about.html")


@app.route("/stocks/")
def stocks() -> str:
    return "<h2>Stonkssss</h2>"


@app.route("/hello/<message>")
def hello_message(message):
    return f"<h1>Welcome {escape(message)}!</h1>"


@app.route("/blog_posts/<int:post_id>")
def blog_post(post_id):
    return f"<h2>Hey look it's blog post #{post_id}</h2>"
