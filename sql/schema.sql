CREATE TABLE github_events (
    id BIGINT PRIMARY KEY,
    event_type VARCHAR(100),
    actor VARCHAR(255),
    repo VARCHAR(255),
    created_at TIMESTAMP,
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE daily_event_summary (
    day DATE,
    event_type VARCHAR(100),
    total_events BIGINT
);
