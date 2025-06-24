-- Tâche 9 : Afficher toutes les villes avec leur état associé, triées par cities.id

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
