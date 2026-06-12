# batch-analytics-platform
GitHub Event Analytics Platform built with Python, PostgreSQL, Docker, and Grafana


# Batch Analytics Platform

## Overview

Built an end-to-end GitHub event analytics platform using Python, PostgreSQL, Docker, and Grafana.

The platform ingests GitHub event data from the public GitHub Events API, stores raw event records in PostgreSQL, transforms them into aggregated analytical datasets, and visualizes operational metrics through Grafana dashboards.

## Architecture

GitHub Events API

↓

Python ETL Pipeline

↓

PostgreSQL (github_events)

↓

Aggregated Analytics Table (daily_event_summary)

↓

Grafana Dashboards

## Technology Stack

* Python
* PostgreSQL
* Docker
* Grafana
* GitHub Events API

## Data Pipeline

1. Extract GitHub event data from the public API.
2. Load raw events into PostgreSQL.
3. Transform event records into daily aggregated summaries.
4. Visualize analytics using Grafana dashboards.

## Database Schema

### github_events

Stores raw GitHub event records.

Columns:

* id
* event_type
* actor
* repo
* created_at
* ingested_at

### daily_event_summary

Stores aggregated event counts by day and event type.

Columns:

* day
* event_type
* total_events
## Sample Analytics Query

```sql
SELECT
    DATE(created_at) AS day,
    event_type,
    COUNT(*) AS total_events
FROM github_events
GROUP BY day, event_type
ORDER BY day DESC;
```

## Dashboard Screenshots

### GitHub Events Dashboard

<img width="1902" height="856" alt="github-events-dashboard" src="https://github.com/user-attachments/assets/e6e2904c-a815-432d-a93a-13ec5ddc6bd9" />

### Event Analytics Dashboard

<img width="1820" height="372" alt="github-event-summary-dashboard" src="https://github.com/user-attachments/assets/b4ca5e74-3fe7-4fc9-88ec-ca62d639a45d" />

## Key Features

* Automated GitHub API ingestion
* PostgreSQL analytical storage
* Aggregated reporting datasets
* Grafana operational dashboards
* Dockerized deployment

## Docker Setup

PostgreSQL was deployed using Docker containers for local development and testing.
