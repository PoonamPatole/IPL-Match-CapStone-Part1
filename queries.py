import os
import mysql.connector
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Read database credentials
connection = mysql.connector.connect(
host = os.getenv("DB_HOST"),
user = os.getenv("DB_USER"),
password = os.getenv("DB_PASSWORD"),
database = os.getenv("DB_NAME")
)

curser=connection.cursor()
queries=[

"""
SELECT *
FROM matches
WHERE city = 'Mumbai';
""",

"""
SELECT winner, COUNT(*) AS total_wins
FROM matches
GROUP BY winner;
"""
"""
SELECT season, venue, COUNT(*) AS "Number of Seasons"
FROM matches
GROUP BY season,venue
HAVING COUNT(*) > 10;
"""
"""
SELECT batting_team,inning, COUNT(match_id) AS "Batting Team"
FROM deliveries
GROUP BY inning,batting_team
ORDER BY COUNT(match_id) DESC LIMIT 5;
"""
"""
select matches.id, matches.match_type, deliveries.bowling_team,deliveries.batting_team
from matches
inner join deliveries on matches.id=deliveries.match_id limit 10;
"""
"""
select batsman_runs from deliveries
where batsman_runs between 1 and 3 limit 10;
"""
]

for query in queries:
    print("\n" + "=" * 60)
    curser.execute(query)
    rows = curser.fetchall()

    for row in rows:
        print(row)

curser.close()
connection.close()

