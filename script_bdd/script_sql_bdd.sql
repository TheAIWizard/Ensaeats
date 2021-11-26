CREATE TABLE ensaeats.Restaurant (
id_restaurant text PRIMARY KEY );

CREATE TABLE ensaeats.Avis (
id_avis SERIAL PRIMARY KEY,
avis text,
date text,
nom_auteur text,
id_restaurant text,
FOREIGN KEY(id_restaurant) REFERENCES ensaeats.Restaurant(id_restaurant)
);

CREATE TABLE ensaeats.Restaurateur (
id_restaurateur SERIAL PRIMARY KEY,
nom text,
prenom text,
identifiant text,
mot_de_passe text,
id_restaurant text,
FOREIGN KEY (id_restaurant) REFERENCES ensaeats.Restaurant(id_restaurant)
) ;


CREATE TABLE ensaeats.Menu(
id_menu SERIAL PRIMARY KEY,
nom text,
prix INT
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

CREATE TABLE ensaeats.Table_restaurant_menu(
id SERIAL PRIMARY KEY,
id_menu INT,
id_restaurant text,
FOREIGN KEY (id_menu) REFERENCES ensaeats.Menu(id_menu),
FOREIGN KEY (id_restaurant) REFERENCES ensaeats.Restaurant(id_restaurant)
) ;

CREATE TABLE ensaeats.Commande(
id_commande SERIAL PRIMARY KEY,
date date ,
prix_total INT,
statut_commande text,
id_restaurant text,
FOREIGN KEY (id_restaurant) REFERENCES ensaeats.Restaurant(id_restaurant)
) ;

CREATE TABLE ensaeats.Table_menu_commande(
id SERIAL PRIMARY KEY,
id_menu INT,
id_commande INT,
quantite INT,
FOREIGN KEY (id_menu) REFERENCES ensaeats.Menu(id_menu),
FOREIGN KEY (id_commande) REFERENCES ensaeats.Commande(id_commande)
) ;


CREATE TABLE ensaeats.Client(
id_client SERIAL PRIMARY KEY,
nom text,
prenom text,
identifiant text,
mot_de_passe text,
adresse text,
telephone text
) ;

CREATE TABLE ensaeats.Table_client_commande(
id SERIAL PRIMARY KEY,
id_commande INT,
id_client INT,
FOREIGN KEY (id_commande) REFERENCES ensaeats.Commande(id_commande),
FOREIGN KEY (id_client) REFERENCES ensaeats.Client(id_client)
);

INSERT INTO ensaeats.restaurant(id_restaurant) VALUES
('NL0ROvACBWrwYv1BZxBWtQ'),
('Rye9AjT3ZKXex8UKG7GU_g'),
('phyz886BDOKEMBhPgfr1VQ'),
('ihhIbISGmRBy06tfwQVYow'),
('LTy9AUgMnLn8YS21KfFZ8g'),
('npMGUHZuf4MUMZ7MFM9FlA'),
('bHZH8zuXdKtXAg9QJ9lLHw'),
('oUdvXPdM3sItZ1zhh8Cjgw'),
('Ud_ayHS1QXhi8ULDwGiGmA'),
('EaNYafmtrZ1qK7DJ3M5zkQ'),
('a7OxWe8DkyKQoqcnfOSxkw'),
('VlKrxdwwx0xm6ByUiHGAqQ'),
('a3gokbfEKALx_1xGvXfL4A'),
('We7SZrq2Lz_xbXQpCzr6FQ'),
('ZJqNk7xPR5EB0EBoenUFPg'),
('PuHakGIiBcpe9unsi8rYaw'),
('VMI6765jxSukB4yFKp1cow'),
('YI6c9mEylXOX4AskuNUTgA'),
('3_bu8pb5q-ko59COXFaG6A'),
('2199oKF5T3rJHD9STnOypQ'),
('-4ab-o_Uyns7V6IksmUHQg'),
('pVwQhBprOvyGP8m7ERUCEA'),
('kFHkpnV7JI_P--xORaIazw'),
('n3aWOSrEnRjv2-twiJlrfA'),
('VDgzPNJYBYZMYuhrSlFUeQ'),
('3tI261qLlVQuq_5jli_faw'),
('L-0yJu9znTlyAzIPCJnVoQ'),
('XUJT9JtGZv5bHwNDIuiM1A'),
('mimozDo17nFdJE3UWRasgw'),
('Mmu33jhnOSFFYPOYbHPD2A'),
('S7nZ9zvCMwjBp7GfjVp6Hw'),
('y5Yj0dwdgUAYG1TWW8TFqA'),
('p7998mHpApwYVLOmS6fJLg'),
('MY-9E94WDYNSCe6hfbkH-g'),
('Lmkh5Qyz5wOOvUyLueN8WA'),
('abdl6J6tJG32-fuV5sx6EQ'),
('ydtNw7uo2XKOsIgn8IK4CA'),
('_J_KQc9vrJhrieANuPpkOQ'),
('ir7t2NjJ7dCyUq1tlG4Nkg'),
('jt004n0B9QmEMCBbQ4pP7g'),
('eJ1j8AawyhVzsA4zE8u8Fg'),
('Z8zRlUJkt7HP7r7KdBrn6w'),
('HkaPxBxgJUiaE-FXyUi-Dw'),
('tD_di2IBefUAH4X3jd-XyA'),
('T8KPtQb04DXr5A5riyUHyQ'),
('AdDVKcyQxd6ZI6PzadQbSA'),
('Syik65xz-7jdXR_WrF4sRw'),
('48jdR8R0655eESF0Z4jb0g'),
('Uj4kWFtdg9h-I_9j0IlJ_w'),
('zVrkHcAEx26rtkH8Op8EZA')
;
INSERT INTO ensaeats.avis(avis,nom_auteur,date,id_restaurant) VALUES
('One of the best creperies in Rennes, and it''s very upscale compared to your tradition crepe place. Of course, that means the prices are upscale too. But the...','Patrick', ' 2021-07-25', 'NL0ROvACBWrwYv1BZxBWtQ'),
('The headline for my review of La Saint George is "This is a super place for fancy crepes!".  I am cleaning up some review drafts I started before COVID hit....','Patrick', ' 2021-07-25', 'NL0ROvACBWrwYv1BZxBWtQ'),
('The name comes up often when asking locals about the best crêperie in Rennes. To be honest, the place is a little too trendy-looking for me. Lots of velvet...','Patrick', ' 2021-07-25', 'NL0ROvACBWrwYv1BZxBWtQ'),
('Food was excellent.. the little things like a chocolate at the end was great.. went for the smoked duck crepe with goat cheese. Tasty but make sure u like...', 'Patrick', ' 2021-07-25', 'Rye9AjT3ZKXex8UKG7GU_g'),
('This place is solid. The special crêpe on the day we dined was a lasagna made of galette instead of your typical lasagna noodles. It was covered in cheese,...','Patrick', ' 2021-07-25', 'Rye9AjT3ZKXex8UKG7GU_g'),
('This is one of my favorite creperies in the Rennes area. They expanded last year and added a nice patio and extra building. It still gets exceptionally...','Patrick', ' 2021-07-25', 'bHZH8zuXdKtXAg9QJ9lLHw'),
('Excellent Galletes! I had the complete and the caramel salt desert gallete (on a gallete instead of a crepe, gluten allergy).  Good cider too! Nice...', 'Patrick', ' 2021-07-25', 'bHZH8zuXdKtXAg9QJ9lLHw'),
('Great place with friendly waiters and a creative menu. You''ll hardly eat twice the same thing. Menus are remade everyday from fresh products. The owner is...', 'Patrick', ' 2021-07-25', 'oUdvXPdM3sItZ1zhh8Cjgw'),
('Not sure why such high reviews.  My gazpacho was green and in dire need of salt, although the falafel in the Lebanese special was excellent with its super...','Patrick', ' 2021-07-25', 'oUdvXPdM3sItZ1zhh8Cjgw'),
('Very Bad Experience\nI would not suggest anyone who is in town for a few days to go to this famous restaurant in Rennes. We did but the way they conducted...','Patrick', ' 2021-07-25', 'oUdvXPdM3sItZ1zhh8Cjgw'),
('I like the restaurant because wow the price is so low and the quality quite decent! Their pancake is about 5-8€ each and I tried a flambé (too bad that I...', 'Patrick', ' 2021-07-25', 'Ud_ayHS1QXhi8ULDwGiGmA'),
('Delicious galette with salmon, chives, and crème fraîche. I could wax poetic about the galette, but it was quite similar to others I''ve had. Of note: the...', 'Patrick', ' 2021-07-25', 'Ud_ayHS1QXhi8ULDwGiGmA'),
('Delicious crepes and galettes, and an atmosphere super-bien! I would certainly come back.','Patrick', ' 2021-07-25', 'Ud_ayHS1QXhi8ULDwGiGmA'),
('This place sounded good so we thought we''d give it a try. Be aware that this restaurant is in the historic area of Rennes, where tables are packed and...','Patrick', ' 2021-07-25', 'a7OxWe8DkyKQoqcnfOSxkw'),
('Wonderful creperie! I love this place and am dreaming about when the next time I can make time to go back is. They''re located very close to the Parc du...', 'Patrick', ' 2021-07-25', 'a3gokbfEKALx_1xGvXfL4A'),
('My Father and I frequented this wonderful restaurant while traveling in Rennes. The waitress that served us was so friendly and welcoming we had to return....', 'Patrick', ' 2021-07-25', 'a3gokbfEKALx_1xGvXfL4A'),
('Really amazing crepes and crazy homemade savory ice cream. Get Le Terrible for dessert!','Patrick', ' 2021-07-25', 'a3gokbfEKALx_1xGvXfL4A'),
('This place is great. Cold beer calm attitude and even Boulevard IPA. Wow. Kansas city represented. Love it.','Patrick', ' 2021-07-25', 'PuHakGIiBcpe9unsi8rYaw'),
('If you are new to Rennes maybe one you ease into.  Clientele seems a bit rough.  That being said beer is good and served colder than UK beers.  Bartender...','Patrick', ' 2021-07-25', 'PuHakGIiBcpe9unsi8rYaw'),
('Délicieux et original. \n\nLa carte des vins est aussi surprenante que la carte elle même.', 'Patrick', ' 2021-07-25', 'VMI6765jxSukB4yFKp1cow'),
('Outstanding restaurant!\n\nExtraordinary service and fantastic food \n\nPortions were perfect for dinner.\n\nAppetizer of crab, salmon and sea bass was delicious...', 'Patrick', ' 2021-07-25', '3_bu8pb5q-ko59COXFaG6A'),
('I had a really great meal at Le Galopin on a recent trip to Rennes.  I will go with a well deserved round-up 5-star rating for Le Galopin.  The restaurant...', 'Patrick', ' 2021-07-25', '3_bu8pb5q-ko59COXFaG6A'),
('This restaurant has a nice mix of seafood and meat dishes. We had only seafood dishes so I can not speak to the meat dishes. The service was excellent and...', 'Patrick', ' 2021-07-25', '3_bu8pb5q-ko59COXFaG6A'),
('This Togo restaurant provided a nice break to French meals, on a street not far from Parc du Thabor. Sitting outside, I had the poulet yassi, which was very...', 'Patrick', ' 2021-07-25', '-4ab-o_Uyns7V6IksmUHQg'),
('Simple but nice restaurant and date spot. Most if not all items are meat dishes, but the host was able to have a legume dish prepared for my vegan request....','Patrick', ' 2021-07-25', '-4ab-o_Uyns7V6IksmUHQg'),
('Really good tajine and vegetarian mezzes. Not sure what to add. Go and taste','Patrick', ' 2021-07-25', 'pVwQhBprOvyGP8m7ERUCEA'),
('This review will be a short one! Amazing! Amazing! Amazing!! The food is soooo good (currently in a food coma, but my oh my did the flavours amaze me)....', 'Patrick', ' 2021-07-25', 'pVwQhBprOvyGP8m7ERUCEA'),
('My god! What a GEM! This was a highly recommended restaurant by a local and everything about the experience was simply perfect. Michelin 1 star restaurant...', 'Patrick', ' 2021-07-25', 'kFHkpnV7JI_P--xORaIazw'),
('Ambiance was good, food was ok. Nothing really jumping out. creme brûlée was so so. Pork was a bit dry and too diffuse with the lentils. a friend had the...', 'Patrick', ' 2021-07-25', 'kFHkpnV7JI_P--xORaIazw'),
('Good, typical french Café & Bar in the City of Rennes. I remember the good coffee and the american cookies. Young service team, that was always polite and...','Patrick', ' 2021-07-25', 'L-0yJu9znTlyAzIPCJnVoQ'),
('Probably my favorite restaurant in Rennes. Classic bistro fare but here we have a high quality chef. Although it''s called Breton I don''t find too much...', 'Patrick', ' 2021-07-25', 'mimozDo17nFdJE3UWRasgw'),
('Very good food and nice ambience. The dishes were very interesting and tasty. Service was friendly and quick.', 'Patrick', ' 2021-07-25', 'S7nZ9zvCMwjBp7GfjVp6Hw'),
('Love the decor and the service is excellent but the food was very mediocre. The burgers are served on a greasy potato rosti - such a shame because the meat...', 'Patrick', ' 2021-07-25', 'S7nZ9zvCMwjBp7GfjVp6Hw'),
('Came here on a whim after seeing the Formule Midi.\n\n9.90 for the Plat du Jour\n12.90 for E + P or P + D\n15.90 for Entree + Plat + Dessert\n\nI came around...', 'Patrick', ' 2021-07-25', 'abdl6J6tJG32-fuV5sx6EQ'),
('Wandered into this restaurant while perusing downtown Rennes. Very nice place to eat. Our server was so friendly. I loved the atmosphere, perfect for a...', 'Patrick', ' 2021-07-25', 'abdl6J6tJG32-fuV5sx6EQ'),
('7 people on a business trip on a quiet Monday night. We stopped here for dinner because the front courtyard looked nice. Absolutely terrible service. The...', 'Patrick', ' 2021-07-25', 'abdl6J6tJG32-fuV5sx6EQ'),
('Nice mixture of cafe and restaurant right next to the Rennes train station.  You can sit against the window and enjoy a view while you eat.  The menu is...','Patrick', ' 2021-07-25', 'ydtNw7uo2XKOsIgn8IK4CA'),
('A nice local bistro. Not far from the train station. Service was warm. Huitres were cold and tasty. Wine list bigger than the menu, had a nice Chinon....', 'Patrick', ' 2021-07-25', 'ydtNw7uo2XKOsIgn8IK4CA'),
('A nice little brasserie in the center of Rennes. The interior is nice and because of little wall in the front part, you can find some cozy private tables...','Patrick', ' 2021-07-25', 'ydtNw7uo2XKOsIgn8IK4CA'),
('While looking for a place to have dinner on a Monday evening I found this wonderful restaurant in the old town. The staff was very friendly and welcoming. I...', 'Patrick', ' 2021-07-25', 'eJ1j8AawyhVzsA4zE8u8Fg'),
('Amazing atmosphere and very fresh food.  The pad thai was amazing and the spring rolls.  Very fairly priced and I will return', 'Patrick', ' 2021-07-25', 'Z8zRlUJkt7HP7r7KdBrn6w'),
('Didn''t expect it to be authentic or anything for obvious reason. \nBut, please do examine your drink before consumption. I ordered one Yuzu mojito it came...','Patrick', ' 2021-07-25', 'Z8zRlUJkt7HP7r7KdBrn6w'),
('Don''t come here if you want authentic Asian food. One of the waitress is also rude as hell.', 'Patrick', ' 2021-07-25', 'Z8zRlUJkt7HP7r7KdBrn6w'),
('We went to Le Saison recently to celebrate a friend''s birthday. It is a wonderful restaurant and the food was excellent. The service was also attentive. It...','Patrick', ' 2021-07-25', 'HkaPxBxgJUiaE-FXyUi-Dw'),
('I have to go with 5 stars for my review.  There is no reason for me to rate this place lower and drag down their current stellar average.  I LOVE crepes and...','Patrick', ' 2021-07-25', 'tD_di2IBefUAH4X3jd-XyA'),
('We had the best salted caramel crêpe ever here!  Nothing fancy about the location, but it is well visited and extremely convent to the central train...', 'Patrick', ' 2021-07-25', 'tD_di2IBefUAH4X3jd-XyA'),
('Just fantastic crepes. I had the chocolate, ice-cream and almond one. The chocolate is really good stuff. Service was excellent even though we were there...','Patrick', ' 2021-07-25', 'tD_di2IBefUAH4X3jd-XyA'),
('A classy gourmet place with a casual atmosphere and friendly attitude. none of the menus are in English and no one speaks English but they try to translate....', 'Patrick', ' 2021-07-25', 'T8KPtQb04DXr5A5riyUHyQ'),
('Good lunch prix fixe menu. For about 10€, you get pizza, coffee, and a dessert. They restrict which pizzas you can get (I got the Diva), but they are tasty...', 'Patrick', ' 2021-07-25', 'AdDVKcyQxd6ZI6PzadQbSA')
;
INSERT INTO ensaeats.menu(id_menu,nom,prix) VALUES
(1,'Menu retour du marché du 26 au 30 Octobre 2021', 34),
(2,'Menu légumes', 54),
(3,'Menu plaisir', 51),
(4,'Menu au rythme des saisons', 71),
(5,'Menu épicurien', 89)
;

INSERT INTO ensaeats.article(id_article,nom,type_article,composition) VALUES
(2,'Cannelloni de courge', 'entrée', 'Butternut, farce boudin, pommes et vinaigrette au jus de viande'),
(3,'Aile de raie', 'plat', 'Rôtie au beurre noisette, chou-fleur et choux de Bruxelles, sauce crémeuse au chorizo'),
(4,'Le tout caramel', 'dessert', 'Biscuit streusel noisette, pâte à choux et glace caramel '),
(5,'Carpaccio de betterave', 'entrée', 'Mariné soja et gingembre, betterave, framboise et café'),
(6,'Les champignons', 'plat', 'Gâteau de girolles, cèpe rôti, artichaut poivrade et jus de viande truffé'),
(7,'L’agrume', 'dessert', 'Crème diplomate au citron, chocolat blanc, pomelos et sorbet mandarine/estragon'),
(8,'Radis colorés', 'entrée', 'Cuits, crus en pickles, navets glacés, lentilles Beluga, vinaigrette au jus de blue meat'),
(9,'Coquilles Saint Jacques', 'plat', 'Cuites au bouillon, anguille fumée, pak choï et poivre des mers'),
(10,'Gourmandise chocolatée', 'dessert', 'Confiture de lait, crémeux et écume chocolat 67%, cookie et gavotte'),
(11,'Foie gras', 'entrée', 'Comme une part de gâteau, compotée de coing, orange et pain d’épices'),
(12,'Le cerf', 'plat', 'Grillé, betterave crapaudine et jus au vieux balsamique'),
(13,'Sélection de 3 Fromages\xa0de la Maison Bordier', 'dessert', 'Citron vert et crème glacée au poivre Andaliman '),
(14,'Les huîtres', 'entrée', 'Cuisinées en trois façons : épinard/fruits de la passion, calamansi/sancho, poudre des Indes/poire'),
(15,'Le flétan', 'plat', 'Radis colorés de notre maraîcher, lentilles Beluga et fumet corsé au vin rouge'),
(16,'Le kaki', 'dessert', 'Confiture de lait, crémeux et écume chocolat 67%, cookie et gavotte'),
(17,'Le bar', 'entrée', 'Confit au beurre, artichaut poivrade, shiso et écume citronnée'),
(18,'Homard breton (supplément 19€)', 'plat', 'Entier, rôti au beurre, sucrine du Berry, condiment butternut et bisque mousseuse au parfum Vadouvan')
;

INSERT INTO ensaeats.table_restaurant_menu(id_restaurant,id_menu) VALUES
('LTy9AUgMnLn8YS21KfFZ8g', 1),
('LTy9AUgMnLn8YS21KfFZ8g', 2),
('LTy9AUgMnLn8YS21KfFZ8g', 3),
('LTy9AUgMnLn8YS21KfFZ8g', 4),
('LTy9AUgMnLn8YS21KfFZ8g', 5)
;

INSERT INTO ensaeats.table_menu_article(id_menu,id_article) VALUES
(1, 2),
(1, 3),
(1, 4),
(2, 5),
(2, 6),
(2, 7),
(3, 8),
(3, 9),
(3, 10),
(4, 11),
(4, 12),
(4, 13),
(5, 14),
(5, 15),
(5, 16)
;

