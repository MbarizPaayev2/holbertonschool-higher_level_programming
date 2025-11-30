-- this is commnet 
SELECT tv_shows.title FROM tv_shows 
JOIN tv_genres ON tv_shows.title = tv_genres.name
WHERE tv_shows.title = Dexter
ORDER BY tv_shows.title;
