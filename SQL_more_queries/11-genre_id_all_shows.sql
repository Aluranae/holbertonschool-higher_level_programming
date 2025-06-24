-- Tâche 11 : Afficher toutes les séries, qu'elles aient un genre ou non, avec leur id de genre (NULL si aucun)

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;