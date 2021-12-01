-- drop test user if exists
use pysports;

DROP USER IF EXISTS 'pysports_user'@'localhost';

-- create pysports_user and them all the priveledges to the pysports database
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
-- grant all privileges to the pysports database to user pysport_user on local host
GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';
-- drop tables if they are present
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;

-- create the team table
CREATE TABLE team (
team_id		INT     		NOT NULL		AUTO_INCREMENT,
team_name	VARCHAR(75)     NOT NULL,
mascot 		VARCHAR(75)		NOT NULL,
PRIMARY KEY(team_id)
);

-- create the player table and set the foreign key
CREATE TABLE player(
player_id		INT     		NOT NULL		AUTO_INCREMENT,
first_name		VARCHAR(75)     NOT NULL,
last_name 		VARCHAR(75)		NOT NULL,
team_id			INT             NOT NULL,
PRIMARY KEY(player_id),
CONSTRAINT fk_team
FOREIGN KEY (team_id)
	REFERENCES team(team_id)
);

-- insert team records
INSERT INTO team(team_name,mascot)
	VALUES('Team Gandalf', 'White Wizards');

INSERT INTO team(team_name,mascot)
	VALUES('Team Warriors', 'Spartan');

-- insert player records team 1
INSERT INTO player(first_name,last_name,team_id)
	VALUES('Nelson', 'Morales',(SELECT team_id From team WHERE team_name = 'Team Gandalf'));
INSERT INTO player(first_name,last_name,team_id)
	VALUES('Cory', 'Morales', (SELECT team_id From team WHERE team_name = 'Team Gandalf'));
INSERT INTO player(first_name,last_name,team_id)
	VALUES('Max', 'Morales', (SELECT team_id From team WHERE team_name = 'Team Gandalf'));

-- insert player records team 2
	INSERT INTO player(first_name,last_name,team_id)
	VALUES('Danie', 'Carr', (SELECT team_id From team WHERE team_name = 'Team Warriors'));
INSERT INTO player(first_name,last_name,team_id)
	VALUES('Matt', 'Carr', (SELECT team_id From team WHERE team_name = 'Team Warriors'));
INSERT INTO player(first_name,last_name,team_id)
	VALUES('Steve', 'Carr',(SELECT team_id From team WHERE team_name = 'Team Warriors'));

	