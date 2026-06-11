
#📈 Stock Portfolio App

A simple Flask web application for tracking stock purchases. Users can add stocks by entering a symbol, number of shares, and purchase price, then view them in a portfolio table.

Features


Add stocks with symbol validation (1–5 uppercase letters)
Input validation using Pydantic
View added stock in a portfolio table
Multi-page layout with a shared base template
Dark themed UI with neon green accents


Project Structure

├── app.py                  # Flask application and routes
├── requirements.txt        # Python dependencies
└── templates/
    ├── base.html           # Shared layout (navbar, styles)
    ├── index.html          # Home page
    ├── add_stock.html      # Add stock form
    ├── stocks.html         # Stock portfolio table
    └── about.html          # About page

Prerequisites


Python 3.8+


Installation


Clone the repository


bash   git clone <your-repo-url>
   cd <your-repo-folder>


Create and activate a virtual environment (recommended)


bash   python -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows


Install dependencies


bash   pip install -r requirements.txt

Running the App

bashpython app.py

Then open your browser at http://127.0.0.1:5000.

Pages

RoutePageDescription/HomeWelcome page/add_stockAdd StockForm to submit a new stock/stocks/View StocksTable showing the last added stock/aboutAboutDeveloper info

Stock Validation Rules

Submitted stock data is validated by Pydantic before being saved:


Stock Symbol — letters only, 1–5 characters, auto-converted to uppercase
Number of Shares — must be a valid integer
Purchase Price — must be a valid float


Invalid submissions are rejected and logged to the console.

⚠️ Known Limitations


Session-based storage — only the most recently added stock is stored; data is lost when the session ends. A database (e.g. SQLite + SQLAlchemy) would be needed for persistence.
Hardcoded secret key — app.secret_key in app.py is set to a placeholder value. Before deploying, replace it with a strong random key and load it from an environment variable:


python  import os
  app.secret_key = os.environ.get('SECRET_KEY')

Dependencies

PackagePurposeFlaskWeb framework and routingPydanticForm data validation
