-- Tâche 1 : Créer l'utilisateur user_0d_1 avec tous les privilèges sur le serveur

-- Créer l'utilisateur seulement s'il n'existe pas déjà
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Donner tous les privilèges à user_0d_1 sur toutes les bases et tables du serveur
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
