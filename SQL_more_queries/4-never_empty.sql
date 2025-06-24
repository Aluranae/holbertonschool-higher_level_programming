-- Tâche 4 : Créer la table id_not_null avec une valeur par défaut de 1 pour la colonne id

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
