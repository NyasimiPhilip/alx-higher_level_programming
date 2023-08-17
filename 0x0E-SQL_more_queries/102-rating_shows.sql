-- Retrieve a list of all shows from the hbtn_0d_tvshows_rate database, sorted by their total rating
SELECT tv_shows.title, SUM(rate) AS rating
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.id
ORDER BY rating DESC;