# HireTrack — Job Application Management System

HireTrack is a responsive full-stack job application tracker built with **Python, Flask, SQLite, SQLAlchemy, HTML, CSS and JavaScript**.

It is designed as a portfolio project that demonstrates CRUD operations, database persistence, server-side rendering, REST API basics, filtering, responsive UI design and dashboard analytics.

## Features

- Professional responsive dashboard
- Add job applications
- Edit application status and notes
- Delete applications
- Search by company, role or location
- Filter by application status
- Automatic application statistics
- Response-rate calculation
- SQLite database persistence
- SQLAlchemy ORM
- JSON API endpoint
- Health-check endpoint
- Demo data automatically seeded on first run
- Mobile-friendly interface

## Tech Stack

**Frontend:** HTML5, CSS3, Vanilla JavaScript  
**Backend:** Python, Flask  
**Database:** SQLite  
**ORM:** Flask-SQLAlchemy

## Run locally

### 1. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

The SQLite database is created automatically.

## API

Open:

```text
GET /api/applications
```

Health check:

```text
GET /health
```

## Project structure

```text
HireTrack/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── app.js
```

## Portfolio upgrades

For a production version, add:

- User authentication
- PostgreSQL
- Interview calendar
- Email reminders
- Resume version tracking
- Job board API integrations
- Docker deployment
- Automated tests
- CI/CD
