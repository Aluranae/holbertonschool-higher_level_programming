-- Script to list all Comedy shows from the hbtn_0d_tvshows database

-- Select the title of each show linked to the "Comedy" genre
SELECT tv_shows.title
FROM tv_shows
-- Link shows to genres through the association table
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
-- Filter to keep only shows linked to the "Comedy" genre
WHERE tv_genres.name = 'Comedy'
-- Sort titles in ascending order
ORDER BY tv_shows.title ASC;
