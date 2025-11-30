-- this is commnet 
SELECT tv_shows.title FROM tv_shows 
JOIN tv_genres ON tv_show.title = tv_genres.name
ORDER BY tv_shows.title;
