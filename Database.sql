-- phpMyAdmin SQL Dump

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS `moodplayer`;
use `moodplayer`;

DROP TABLE IF EXISTS `songs`;
DROP TABLE IF EXISTS `users`;
DROP TABLE IF EXISTS `moods`;
DROP TABLE IF EXISTS `mapmoods`;

create table `songs` (
    song_id int AUTO_INCREMENT,
    songname varchar(100),
    PRIMARY KEY(song_id)
);

CREATE TABLE `users` (
    user_id int AUTO_INCREMENT,
    name varchar(100),
    username varchar(100) UNIQUE,
    password varchar(100),
    email varchar(100),
    PRIMARY KEY(user_id)
);

CREATE TABLE  `moods` (
    mood_id int AUTO_INCREMENT,
    moodname varchar(100),
    PRIMARY KEY(mood_id)
);

CREATE TABLE `mapmoods` (
    user_id int,
    song_id int,
    mood_id int
);

INSERT INTO `moods` VALUES (1, 'Neutral');
INSERT INTO `moods` VALUES (2, 'Happy');
INSERT INTO `moods` VALUES (3, 'Surprise');
INSERT INTO `moods` VALUES (4, 'Sad');
INSERT INTO `moods` VALUES (5, 'Fear');
INSERT INTO `moods` VALUES (6, 'Disgust');
INSERT INTO `moods` VALUES (7, 'Surprise');

INSERT INTO `songs` VALUES (1, 'Club Cant Handle Me');
INSERT INTO `songs` VALUES (2, 'Hips Dont Lie');
INSERT INTO `songs` VALUES (3, 'Hey Soul Sister');
INSERT INTO `songs` VALUES (4, 'Senorita');
INSERT INTO `songs` VALUES (5, 'Believer - Imagine Dragons');
INSERT INTO `songs` VALUES (6, 'Fix You');
INSERT INTO `songs` VALUES (7, 'Fix You - Piano');
INSERT INTO `songs` VALUES (8, 'Boulevard of Broken Dreams Live');