-- 16-shows_by_genre.sql
-- Script that lists all shows and their associated genres
-- from the database hbtn_0d_tvshows.
-- If a show has no genre, NULL is shown for the genre name.
-- Results are sorted by show title and genre name (both ascending).
-- Only one SELECT statement is allowed.

SELECT
    tv_shows.title,       -- Show title to be displayed in the first column
    tv_genres.name        -- Genre name to be displayed in the second column (can be NULL)

FROM
    tv_shows              -- Base table containing all TV show records

-- First LEFT JOIN to include all shows,
-- even those not associated with any genre (ensures NULLs are shown)
LEFT JOIN
    tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id

-- Second LEFT JOIN to get the name of the genre,
-- or NULL if the genre_id in the association table is NULL
LEFT JOIN
    tv_genres
    ON tv_show_genres.genre_id = tv_genres.id

-- Sort alphabetically by show title,
-- and then by genre name (NULLs appear last)
ORDER BY
    tv_shows.title ASC,
    tv_genres.name ASC;
    