#TODO 

#Oisko et voi olla 20 merkkisii käyttäjänimiä max 
#Myös et ei saa olla tyhjiä
#En ole vielä testannut toimiiko mut kaiken järjen mukaan pitäisi toimia
CREATE TABLE users (
	user_id SERIAL PRIMARY KEY,
	username VARCHAR (20) UNIQUE NOT NULL CHECK (username <> ''),
	password TEXT NOT NULL CHECK (password <> '')
);
