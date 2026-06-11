from flask import session
from flask import Flask, render_template, request
from pydantic import BaseModel, field_validator, ValidationError



class StockModel(BaseModel):
    """Class for parsing new stock data from a form."""
    stock_symbol: str
    number_of_shares: int
    purchase_price: float

    @field_validator('stock_symbol')
    def stock_symbol_check(cls, value):
        if not value.isalpha() or len(value) > 5:
            raise ValueError('Stock symbol must be 1-5 characters')
        return value.upper()

app = Flask(__name__)

app.secret_key = 'BAD_SECRET_KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', company_name='TestDriven.io')
    #return render_template('about.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/stocks/')
def list_stocks():
    return render_template('stocks.html')

from flask import redirect, url_for
@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        # Print the form data to the console
        for key, value in request.form.items():
            print(f'{key}: {value}')

        try:
            stock_data = StockModel(
                stock_symbol=request.form['stock_symbol'],
                number_of_shares=request.form['number_of_shares'],
                purchase_price=request.form['purchase_price']
            )
            print(stock_data)

            # Save the form data to the session object
            session['stock_symbol'] = stock_data.stock_symbol
            session['number_of_shares'] = stock_data.number_of_shares
            session['purchase_price'] = stock_data.purchase_price
            return redirect(url_for('list_stocks'))  # NEW!!
        except ValidationError as e:
            print(e)

    return render_template('add_stock.html')