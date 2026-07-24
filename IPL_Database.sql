create database IPL_Database;
USE IPL_Database;
show tables;
describe matches;
describe deliveries;

SELECT season, venue, COUNT(*) AS "Number of Seasons"
FROM matches
GROUP BY season,venue
HAVING COUNT(*) > 10;

SELECT batting_team,inning, COUNT(match_id) AS "Batting Team"
FROM deliveries
GROUP BY inning,batting_team
ORDER BY COUNT(match_id) DESC LIMIT 5;

select matches.id, matches.match_type, deliveries.bowling_team,deliveries.batting_team
from matches
inner join deliveries on matches.id=deliveries.match_id limit 10;

select batsman_runs from deliveries
where batsman_runs between 1 and 3 limit 10;

select batsman_runs from deliveries;

SELECT *
FROM matches
WHERE city = 'Mumbai';

SELECT winner, COUNT(*) AS total_wins
FROM matches
GROUP BY winner;