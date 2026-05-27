# Webapp

A simple web application built with Flask and HTML/CSS/JavaScript.

## Features

- Flask backend API
- Beautiful responsive frontend
- Interactive button to fetch messages from API

## Setup

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ibrahim642/webapp.git
cd webapp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
webapp/
├── app.py              # Flask application
├── hello.py            # Sample Python script
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── templates/
    └── index.html     # HTML template
```

## API Endpoints

- `GET /` - Home page
- `GET /api/hello` - Returns a JSON message

## License

MIT
