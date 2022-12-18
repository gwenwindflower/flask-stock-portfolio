from flask import Flask, render_template, request
from markupsafe import escape
from pydantic import BaseModel, validator, ValidationError

app = Flask(__name__)


class StockModel(BaseModel):
    """Class for parsing new stock data from a form."""

    stock_symbol: str
    number_of_shares: int
    purchase_price: float

    @validator("stock_symbol")
    def stock_symbol_check(cls, field):
        if not field.isalpha() or len(field) > 5:
            raise ValueError("Stock symbol must be 1-5 alphabetical characters")
        return field.upper()


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


@app.route("/add_stock", methods=["GET", "POST"])
def add_stock():
    if request.method == "POST":
        try:
            stock_data = StockModel(
                stock_symbol=request.form["stock_symbol"],
                number_of_shares=request.form["number_of_shares"],
                purchase_price=request.form["purchase_price"],
            )
            print(stock_data)
        except ValidationError as e:
            print(e)
    return render_template("add_stock.html")
