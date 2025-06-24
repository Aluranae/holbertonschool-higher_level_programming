-- Tâche 8 : Afficher les villes de l'état "California" en utilisant une sous-requête

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
