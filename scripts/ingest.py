import requests
import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    port=5433,
    dbname="analytics",
    user="admin",
    password="password"
)

cursor = conn.cursor()

total_loaded = 0

for page in range(1, 6):

    print(f"Fetching page {page}")

    response = requests.get(
        f"https://api.github.com/events?page={page}"
    )

    data = response.json()

    for item in data:

        cursor.execute(
            """
            INSERT INTO github_events
            (id, event_type, actor, repo, created_at)
            VALUES (%s,%s,%s,%s,%s)
            ON CONFLICT (id) DO NOTHING
            """,
            (
                int(item["id"]),
                item["type"],
                item["actor"]["login"],
                item["repo"]["name"],
                item["created_at"]
            )
        )

    total_loaded += len(data)

conn.commit()

print(f"Processed {total_loaded} records")

cursor.close()
conn.close()
