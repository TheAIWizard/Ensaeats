CREATE TABLE ensaeats.Restaurant (
id_restaurant text PRIMARY KEY ,
nom text );

CREATE TABLE ensaeats.Avis (
id_avis SERIAL PRIMARY KEY,
avis text,
nom_auteur text,
id_restaurant text,
FOREIGN KEY(id_restaurant) REFERENCES ensaeats.Restaurant(id_restaurant)
);

CREATE TABLE ensaeats.Restaurateur (
id_restaurateur SERIAL PRIMARY KEY,
nom text,
prenom text,
id_restaurant text,
FOREIGN KEY (id_restaurant) REFERENCES ensaeats.Restaurant(id_restaurant)
) ;


CREATE TABLE ensaeats.Menu(
id_menu SERIAL PRIMARY KEY,
nom text,
prix INT,
id_restaurant text,
FOREIGN KEY (id_restaurant) REFERENCES ensaeats.Restaurant(id_restaurant)
) ;

CREATE TABLE ensaeats.Article(
id_article SERIAL PRIMARY KEY,
nom text,
type_article text,
composition text
);

CREATE TABLE ensaeats.Table_menu_article(
id SERIAL PRIMARY KEY,
id_menu INT,
id_article INT,
FOREIGN KEY (id_menu) REFERENCES ensaeats.Menu(id_menu),
FOREIGN KEY (id_article) REFERENCES ensaeats.Article(id_article)
) ;

CREATE TABLE ensaeats.Commande(
id_commande SERIAL PRIMARY KEY,
date date ,
prix_total INT,
statut_commande text
) ;

CREATE TABLE ensaeats.Table_menu_commande(
id SERIAL PRIMARY KEY,
id_menu INT,
id_commande INT,
FOREIGN KEY (id_menu) REFERENCES ensaeats.Menu(id_menu),
FOREIGN KEY (id_commande) REFERENCES ensaeats.Commande(id_commande)
) ;

CREATE TABLE ensaeats.Client(
id_client SERIAL PRIMARY KEY,
nom text,
prenom text,
adresse text,
mot_de_passe text,
telephone text
) ;

CREATE TABLE ensaeats.Table_client_commande(
id SERIAL PRIMARY KEY,
id_commande INT,
id_client INT,
FOREIGN KEY (id_commande) REFERENCES ensaeats.Commande(id_commande),
FOREIGN KEY (id_client) REFERENCES ensaeats.Client(id_client)
);