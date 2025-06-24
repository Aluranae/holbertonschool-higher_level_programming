-- Tâche 2 : Créer la base hbtn_0d_2 et l'utilisateur user_0d_2 avec le privilège SELECT uniquement

-- Créer la base de données si elle n'existe pas déjà
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Créer l'utilisateur user_0d_2 avec mot de passe user_0d_2_pwd si l'utilisateur n'existe pas
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Donner le privilège SELECT à user_0d_2 uniquement sur la base hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
