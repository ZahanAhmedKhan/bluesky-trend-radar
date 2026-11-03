# Bluesky Live Trend Radar

A live social-signal dashboard for tracking what is rising across the Bluesky firehose, with a fast, colorful, reactive interface designed to feel more like a product than a raw data console.

## What it does

This repo now includes a working dashboard service that simulates the real-time trend pipeline and surfaces:

- live posts-per-minute volume
- top hashtags by current activity
- biggest risers and spike ratios
- language distribution
- pipeline health indicators and operational focus signal

The experience is intentionally built to feel polished and interactive, with glass panels, chart animations, and auto-refreshing live data.

## Running locally

From the project root:

```powershell
docker compose up -d
```

Then open:

- http://localhost:8000
- http://localhost:3000 for Grafana when the full stack is started

If you want to run the dashboard alone without Docker:

```powershell
cd dashboard
python -m uvicorn dashboard.main:app --host 127.0.0.1 --port 8000
```

## Stack

- Python 3.12
- FastAPI for the dashboard API
- Jinja2 + Chart.js for the interactive UI
- Docker Compose for service orchestration
- PostgreSQL and Kafka placeholders for the full production pipeline plan

## Design notes

- The UI is built to be readable at a glance, even while data is changing every few seconds.
- Signal cards are intentionally high-contrast so the user can understand momentum without reading raw tables.
- This dashboard is a production-ready front-end foundation for the broader pipeline described in the project plan.

## Privacy and scope

The streaming-first architecture preserves the privacy rule from the project brief by keeping raw content out of the persistent storage layer and only processing derived aggregate signals.
