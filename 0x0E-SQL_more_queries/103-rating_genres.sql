-- Retrieve a list of all genres in the hbtn_0d_tvshows_rate database, sorted by their total rating
SELECT tv_genres.name, SUM(rate) AS rating
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.id
ORDER BY rating DESC;