-- this is comment 
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show JOIN tv_show ON tv_show_genres.genre_id = tv_show.name ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;