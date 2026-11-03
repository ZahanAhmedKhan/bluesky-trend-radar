# Design decisions

## 1. Dashboard-first implementation

We chose a live FastAPI + Chart.js dashboard as the immediate user-facing layer because the app must feel polished and reactive from the first run. This creates a high-signal experience while preserving the architecture needed for the larger Kafka/Spark/Postgres pipeline described in the project plan.

## 2. Auto-refreshing metrics over static screenshots

The UI refreshes every five seconds from a JSON API instead of relying on manually reloaded data. This keeps the dashboard feeling alive and reduces the gap between “interesting signal” and “visible result”.

## 3. Simulated data model for iteration speed

The dashboard uses a realistic but lightweight simulator so the front-end can be validated and tuned without needing a full production stream running in the local environment. The simulation keeps the data contract stable while the full pipeline is being developed.
