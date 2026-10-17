# Stock Portfolio Tracker

A Flask web app for recording stock purchases. Users enter a stock symbol, number of shares, and purchase price through a form, the input is validated on the server, and the entry is saved in the user's session and shown on the stocks page. **[Live Demo](https://hooman-stocks.onrender.com/)**

The demo runs on a free Render instance, so the first load after a period of inactivity can take about a minute while the server wakes up.

<!-- Add a screenshot: save it as screenshot.png in the repo root, then uncomment the line below -->
<!-- ![Screenshot of the app](screenshot.png) -->

## Features

- Add a stock purchase with a symbol, share count, and purchase price
- Server-side validation with Pydantic (symbols must be 1-5 letters and are stored in uppercase; shares must be a whole number; price must be a number)
- Entries stored in the Flask session, so no database or account is needed
- Multiple pages built with Jinja templates: Home, About, Add Stock, and Stocks

## Built With

- Python
- Flask
- Pydantic (form validation)
- Jinja2 templates
- HTML/CSS
- Deployed on Render with Gunicorn

## Project Structure

```
Stocks-Portfolio/
├── app.py              # Flask app: routes, validation model, session handling
├── requirements.txt    # Python dependencies
├── templates/          # Jinja HTML templates
└── static/images/      # Images used by the templates
```

## Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/hoomanv3xo/Stocks-Portfolio.git
   cd Stocks-Portfolio
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   On macOS or Linux, use `source venv/bin/activate` instead.

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the app:

   ```bash
   python -m flask run
   ```

5. Open `http://127.0.0.1:5000` in your browser.

The app reads its session secret from the `SECRET_KEY` environment variable. If it isn't set, it falls back to a development-only key, so set a real value for any deployment:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

## Deployment

The app is deployed on Render as a web service:

- **Build command:** `pip install -r requirements.txt`
- **Start command:** `gunicorn app:app`
- **Environment variable:** `SECRET_KEY`

## How It Works

The `/add_stock` route accepts the form submission and passes the values to a `StockModel` Pydantic class. The model checks the symbol format and converts the share count and price to the right types, and invalid input raises a validation error instead of being saved. Valid data is stored in the Flask session and displayed on the `/stocks/` page.

## Limitations and Next Steps

This is an early version. Current limitations and planned improvements:

- Only the most recent purchase is stored per visitor
- Store multiple purchases and show them in a table
- Add edit and delete actions
- Persist data in SQLite instead of the session
- Look up live prices and calculate total portfolio value

<!-- If this project follows the TestDriven.io Flask tutorial, credit it here, e.g.:
## Acknowledgments
Built while following the TestDriven.io Flask tutorial series. -->

## Author

**Hooman Vahdat**
[LinkedIn](https://linkedin.com/in/hoomanvahdat) | [Portfolio](https://hooman-codes.ca) | [GitHub](https://github.com/hoomanv3xo)

