# batch-analytics-platform
GitHub Event Analytics Platform built with Python, PostgreSQL, Docker, and Grafana


GitHub Events API
        ↓
Python ETL (ingest.py)
        ↓
PostgreSQL (github_events)
        ↓
Aggregated Analytics Table
(daily_event_summary)
        ↓
Grafana Dashboards
