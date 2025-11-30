-- this is comment 
SELECT tv_shows.title as genre tv_show_genres.genre_id as number_of_shows
FROM tv_shows   
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY  tv_shows.title, tv_show_genres.genre_id DESC;