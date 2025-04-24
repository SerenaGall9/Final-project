CREATE DATABASE  IF NOT EXISTS `projectdb12` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `projectdb12`;
-- MySQL dump 10.13  Distrib 8.0.40, for macos14 (x86_64)
--
-- Host: localhost    Database: projectdb3
-- ------------------------------------------------------
-- Server version	9.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cuisine`
--

DROP TABLE IF EXISTS `cuisine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cuisine` (
  `cuisine_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`cuisine_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cuisine`
--

LOCK TABLES `cuisine` WRITE;
/*!40000 ALTER TABLE `cuisine` DISABLE KEYS */;
INSERT INTO `cuisine` VALUES (2,'Indian'),(1,'Italian'),(3,'Japanese'),(4,'Lebanese'),(5,'Mediterranean');
/*!40000 ALTER TABLE `cuisine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `londonlocation`
--

DROP TABLE IF EXISTS `londonlocation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `londonlocation` (
  `location_id` int NOT NULL AUTO_INCREMENT,
  `direction` varchar(10) NOT NULL,
  PRIMARY KEY (`location_id`),
  UNIQUE KEY `direction` (`direction`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `londonlocation`
--

LOCK TABLES `londonlocation` WRITE;
/*!40000 ALTER TABLE `londonlocation` DISABLE KEYS */;
INSERT INTO `londonlocation` VALUES (3,'East'),(1,'North'),(2,'South'),(4,'West');
/*!40000 ALTER TABLE `londonlocation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `restaurants`
--

DROP TABLE IF EXISTS `restaurants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `restaurants` (
  `restaurant_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `location_id` int DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL,
  `price_range` enum('£','££','£££','££££') NOT NULL,
  `description` varchar(500) NOT NULL,
  `menu_link` varchar(255) DEFAULT NULL,
  `cuisine_id` int DEFAULT NULL,
  `vibe_id` int DEFAULT NULL,
  PRIMARY KEY (`restaurant_id`),
  KEY `cuisine_id` (`cuisine_id`),
  KEY `vibe_id` (`vibe_id`),
  KEY `location_id` (`location_id`),
  CONSTRAINT `restaurants_ibfk_1` FOREIGN KEY (`cuisine_id`) REFERENCES `cuisine` (`cuisine_id`),
  CONSTRAINT `restaurants_ibfk_2` FOREIGN KEY (`vibe_id`) REFERENCES `vibetype` (`vibe_id`),
  CONSTRAINT `restaurants_ibfk_3` FOREIGN KEY (`location_id`) REFERENCES `londonlocation` (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurants`
--

LOCK TABLES `restaurants` WRITE;
/*!40000 ALTER TABLE `restaurants` DISABLE KEYS */;
INSERT INTO `restaurants` VALUES (2,'Coco Grill & Lounge','34a Shad Thames, London, SE1 2YG',2,'+44 20 7407 7999','https://www.coco-restaurants.com/coco-index.html','££££','Coco Grill & Lounge is a stylish alcohol-free restaurant in London offering modern Anatolian cuisine with halal ingredients, all set against the iconic backdrop of Tower Bridge. Known for its elegant ambiance, Coco features a unique Redemption Bar serving crafted alcohol-free cocktails and a scenic shisha terrace for a memorable dining experience.','https://www.coco-restaurants.com/menu.html',5,3),(3,'Olives and Meze','131 Clapham High St, London SW4 7SS',2,'020 3583 7790','https://www.olivesandmeze.co.uk/','£','​Olives + Meze is a contemporary Mediterranean eatery with locations in Clapham and Soho, London, celebrated for its fresh, healthy dishes like charcoal-grilled meats, vibrant salads, and house specials such as the Mix Protein Gym Box. Recognized at the 2024 British Kebab Awards, it offers a sleek dining experience and convenient takeaway options.','https://www.olivesandmeze.co.uk/menu',5,5),(4,'Scarpetta Canary Wharf','20 Canada Square, London, E14 5NN',3,'+44 20 3649 6803','https://scarpettapasta.com/restaurant-canary-wharf/','££','​Scarpetta Canary Wharf is a modern Italian restaurant located at 20 Canada Square, London E14 5NN, offering fresh handmade pasta, Italian cocktails, and a curated selection of wines in a stylish, lively setting. It\'s an ideal spot for after-work drinks, date nights, or gatherings with friends and family. ','https://scarpettapasta.com/wp-content/uploads/2024/05/A4-Food-Menu-1.pdf',1,5),(5,'Alexander The Great Greek Restaurant','8 Plender Street, London, NW1 0JT',1,'+44 20 7388 1111','https://alexanderthegreatgreekrestaurant.co.uk/','£££','​Alexander The Great is a family-run Greek restaurant in Camden, London, offering authentic Mediterranean cuisine in a warm, traditional setting. Signature dishes like kleftiko and moussaka are prepared with locally sourced ingredients, making it a favorite for both casual meals and special occasions.','https://alexanderthegreatgreekrestaurant.co.uk/menu/',5,2),(6,'La Tagliata','80 Upper Street, Islington, London N1 0NP, UK',3,'020 73 771 551','https://www.la-tagliata.com/?404=%27','££','​La Tagliata is a family-run Italian restaurant located in Spitalfields, London, near Liverpool Street station. It offers authentic Italian cuisine in a setting reminiscent of an Italian villa, featuring themed rooms like the library and wine cellar. The restaurant specializes in traditional dishes, including its namesake tagliata steak, and provides private dining options for intimate gatherings.','https://www.la-tagliata.com/menu/',1,4),(7,'Gloria Trattoria','54–56 Great Eastern Street, Shoreditch, London EC2A 3QR',3,'020 4578 4370','https://menu.bigmammagroup.com/gloria','££','​Gloria is a vibrant 1970s Capri-style trattoria located in Shoreditch, London, operated by the Big Mamma Group. It offers a lively atmosphere with a menu of Italian classics made from ingredients sourced from 180 small producers across Italy, including dishes like Spaghetti al Tartufo and Neapolitan pizzas baked in a Marana oven','https://menu.bigmammagroup.com/gloria',1,1),(8,'Chutney Mary','73 St. James’s Street, London SW1A 1PH',4,'020 7629 6688','https://www.chutneymary.com/','££££','​Chutney Mary is a pioneering Indian fine dining restaurant located in St James’s, London, renowned for its elegant interiors and diverse regional Indian cuisine. Established in 1990, it offers an opulent dining experience complemented by the stylish Pukka Bar and private dining rooms','https://www.chutneymary.com/menu/',2,3),(9,'Dishoom Covent Garden','12 Upper St. Martin’s Lane, London WC2H 9FB',4,'020 7420 9320','https://www.dishoom.com/covent-garden/','££','​Dishoom is a celebrated Indian restaurant group in the UK, inspired by the Irani cafés of Bombay. Their all-day menu offers a diverse selection of Bombay comfort food, featuring dishes from the city\'s cafés, grills, street stalls, and homes. Guests can enjoy options ranging from small plates and grills to biryanis and curries, all served in a setting that pays homage to the vibrant culture of Bombay','https://www.dishoom.com/menu/all-day-main/',2,6),(10,'Gymkhana','42 Albemarle Street, London W1S 4JH',4,'020 3011 5900','https://gymkhanalondon.com/','££££','​Gymkhana is a two-Michelin-starred Indian restaurant in Mayfair, London, inspired by the elite clubs of colonial India. It offers refined North Indian cuisine with a focus on tandoor and chatpatta dishes, all set within opulent interiors that evoke the elegance of Raj-era mansions','https://gymkhanalondon.com/wp-content/uploads/2020/02/GYMKHANA-ALC-1.pdf',2,2),(11,'Babel grill house','40 Brick lane, London E1 6RF',3,'+44 20 7392 9675','https://www.babelgrillhouse.co.uk/','£££','Babel Grill House is a Lebanese halal restaurant located on Brick Lane in London, offering authentic Middle Eastern cuisine in a warm and inviting atmosphere. Their menu features a variety of dishes, including cold and hot mezza, grilled meats, and traditional desserts, all prepared using inherited ingredients elevated to new levels.','https://www.babelgrillhouse.co.uk/menu',4,3),(12,'Baba ghanouj','105 Gloucester Road, London, SW7 4SS',4,'02039171660','https://www.babaghanouj.co.uk/','£','Baba Ghanouj is a charming Lebanese restaurant in South Kensington, offering an array of authentic dishes like shawarma, manakeesh, and vibrant mezze. With its cozy atmosphere and diverse menu, it’s a go-to spot for both casual dining and special gatherings.','https://www.babaghanouj.co.uk/uploads/our_menu/photo_68309BABA%20GHANOUJ%202024%20MENU%20(1).pdf',4,4),(13,'Mazar','11-12 Battersea Square, Battersea, London, SW11 3RA',2,'020 7978 5374','https://mazarrestaurant.com/','£','​Mazar Restaurant in Battersea offers an authentic Lebanese dining experience, specializing in a diverse array of hot and cold mezze dishes that showcase the rich flavors of Lebanese and Mediterranean cuisine. Located in the vibrant Battersea Square, it provides both indoor and outdoor seating, fostering a welcoming atmosphere for guests to enjoy their meals.','https://mazarrestaurant.com/#menu',4,2),(14,'Beit El Zaytoun','15-17 Barrets Green Road, London, NW10 7AE',1,'+442089611166','https://beitelzaytoun.com','£££','Beit El Zaytoun is a celebrated Lebanese restaurant in London, renowned for its authentic cuisine and vibrant atmosphere. The menu features a wide array of traditional dishes, including mezze, grilled meats, and specialty items like lamb shawarma and kabse lahme, complemented by desserts such as baklava cheesecake and pistachio cake. ','https://beitelzaytoun.com/menu',4,1),(15,'NIJŪ','20 Berkeley Street, London, W1J 8EE',4,'020 98862426','https://nijulondon.com/','££££','NIJŪ is a refined Japanese restaurant in Mayfair, London, offering a contemporary take on \'katei ryōri\'—traditional Japanese home-style cooking. Led by third-generation sushi master Chef Endo Kazutoshi, the restaurant features a bespoke sushi bar, a grill serving premium Wagyu and Kobe beef, and an intimate private dining space, Nipperkin, inspired by Japanese listening bars from the 1950s','https://nijulondon.com/menus/',3,3),(16,'Inamo sukoshi','2 – 10, Bethnal Green Road, London, E1 6GY',3,'0207 186 8800','https://boxpark.co.uk/food-and-drink/inamo-sukoshi/','£','Inamo Sukoshi at BOXPARK Wembley serves a dynamic fusion of sushi and Asian street food, featuring signature dishes like Dragon Rolls, Bao Buns, and Katsu Curry. Recognized with awards such as the Golden Chopsticks Award for Best Street Food UK in 2023, it offers a vibrant dining experience in the heart of Wembley Park ','https://boxpark.co.uk/food-and-drink/inamo-sukoshi/',3,6);
/*!40000 ALTER TABLE `restaurants` ENABLE KEYS */;
UNLOCK TABLES;

select *
from restaurants;

--
-- Table structure for table `review`
--

DROP TABLE IF EXISTS `review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `review` (
  `review_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `restaurant_id` int DEFAULT NULL,
  `Rating` int DEFAULT NULL,
  `Ambience` int DEFAULT NULL,
  `Service` int DEFAULT NULL,
  `Location` int DEFAULT NULL,
  `Value_for_money` int DEFAULT NULL,
  `Overall_review` text,
  `creation_date` date NOT NULL DEFAULT (curdate()),
  PRIMARY KEY (`review_id`),
  KEY `user_id` (`user_id`),
  KEY `restaurant_id` (`restaurant_id`),
  CONSTRAINT `review_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `review_ibfk_2` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurants` (`restaurant_id`),
  CONSTRAINT `review_chk_1` CHECK (((`Rating` >= 1) and (`Rating` <= 5))),
  CONSTRAINT `review_chk_2` CHECK (((`Ambience` >= 1) and (`Ambience` <= 5))),
  CONSTRAINT `review_chk_3` CHECK (((`Service` >= 1) and (`Service` <= 5))),
  CONSTRAINT `review_chk_4` CHECK (((`Location` >= 1) and (`Location` <= 5))),
  CONSTRAINT `review_chk_5` CHECK (((`Value_for_money` >= 1) and (`Value_for_money` <= 5)))
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review`
--

INSERT INTO `review` (`user_id`, `restaurant_id`, `Rating`, `Ambience`, `Service`, `Location`, `Value_for_money`, `Overall_review`, `creation_date`) VALUES
(3, 2, 4, 4, 5, 4, 4, 'Nice food, but the shisha wasn\'t as enjoyable as expected. Still a good place for drinks.', '2012-06-15'),
(4, 2, 5, 5, 5, 5, 5, 'Great spot for a gathering with friends. Lovely outdoor seating area!', '2017-08-23'),
(5, 2, 4, 5, 4, 4, 5, 'Good place to relax, with lovely appetizers, but the main course could have been better.', '2011-01-09'),
(6, 2, 3, 4, 3, 5, 4, 'Great vibe, but it was a bit overpriced for what you get.', '2014-09-30'),

(7, 3, 5, 5, 5, 4, 4, 'Perfect protein-packed meals after a workout. Excellent options for anyone looking to eat clean!', '2019-10-04'),
(8, 3, 3, 4, 3, 5, 3, 'The food is decent, but the atmosphere is a bit too loud for me.', '2018-11-22'),
(9, 3, 4, 5, 5, 4, 5, 'Love the healthy options and the quick service. Great for lunch breaks!', '2020-03-15'),
(10, 3, 4, 4, 4, 5, 4, 'Decent food, but could have been a bit more flavorful.', '2017-02-01'),

(11, 4, 4, 5, 4, 5, 5, 'Cozy and charming. Pasta was fantastic, but it can get crowded during weekends.', '2013-07-18'),
(12, 4, 5, 5, 5, 5, 5, 'The best pasta in town! Great for a casual night out.', '2015-02-10'),
(13, 4, 4, 5, 3, 4, 4, 'Good pasta, but could have been more flavorful. The wine selection was great though.', '2022-06-23'),
(14, 4, 5, 5, 4, 5, 4, 'Nice for a cozy dinner. Great for dates!', '2019-11-16'),

(15, 5, 5, 5, 5, 5, 4, 'Fantastic atmosphere and great food. The lamb was cooked to perfection.', '2020-02-17'),
(1, 5, 4, 4, 3, 4, 4, 'The food was good but the service could have been faster. Still a lovely place for a meal.', '2019-05-06'),
(2, 5, 3, 3, 3, 3, 3, 'Nice setting, but the food was not up to par for the price.', '2016-08-30'),
(3, 5, 5, 5, 4, 5, 5, 'A fantastic meal and very warm atmosphere. Highly recommend!', '2021-04-10'),

(4, 6, 5, 5, 4, 5, 5, 'A true taste of Italy. Loved the tiramisu!', '2021-07-23'),
(5, 6, 4, 5, 5, 4, 4, 'Impressive wine list and lovely staff, though the mains were a little pricey.', '2017-12-01'),
(6, 6, 4, 5, 5, 3, 3, 'Great wine selection, but I was underwhelmed by the main course.', '2022-04-05'),
(7, 6, 5, 4, 5, 5, 5, 'Felt like I was in Italy! Great pasta dishes and wine.', '2020-08-15'),

(8, 7, 5, 5, 5, 4, 4, 'Perfect date night spot. Great food and cozy atmosphere.', '2016-03-12'),
(9, 7, 4, 4, 5, 4, 3, 'Good food, but the noise levels made it hard to relax. Still enjoyed the experience.', '2021-09-10'),
(10, 7, 3, 4, 4, 5, 3, 'Not a fan of the noise, but the pizza was pretty good.', '2022-05-04'),
(11, 7, 5, 5, 5, 5, 5, 'Best pizza and pasta combo in the area. Perfect for casual dining.', '2023-01-28'),

(12, 8, 4, 4, 5, 5, 5, 'Delicious Indian food and very attentive service. Will return soon.', '2014-06-11'),
(13, 8, 5, 5, 5, 5, 4, 'Wonderful food and exceptional service. The tasting menu was amazing!', '2019-03-27'),
(14, 8, 4, 5, 4, 5, 5, 'Sophisticated restaurant with a great menu. Perfect for special occasions.', '2021-08-18'),
(15, 8, 5, 5, 5, 5, 5, 'The most amazing Indian food I\'ve had. The tasting menu is a must-try.', '2023-06-11'),

(1, 9, 4, 4, 4, 5, 5, 'Great vibe, but I found the curry a bit too spicy for my taste.', '2020-11-06'),
(2, 9, 5, 5, 5, 5, 5, 'Love the decor, and the food is top notch. Definitely worth the wait.', '2021-01-13'),
(3, 9, 5, 5, 4, 5, 5, 'Incredible vibe and fantastic food. Worth every penny!', '2022-03-21'),
(4, 9, 3, 4, 3, 4, 4, 'The food was decent, but I found the service a bit slow.', '2019-07-12'),

(5, 10, 4, 5, 4, 5, 4, 'Good food, though the flavors weren\'t as bold as I expected.', '2012-07-23'),
(6, 10, 5, 5, 5, 5, 5, 'Opulent and flavorful. The service was impeccable, and the dishes were unforgettable!', '2023-11-30'),
(7, 10, 4, 4, 4, 4, 4, 'Nice place, but the menu could have been a little more varied.', '2020-09-17'),
(8, 10, 5, 5, 5, 5, 5, 'Incredible dining experience. Highly recommend the game dishes.', '2021-12-03'),

(9, 11, 4, 4, 4, 5, 3, 'The grilled meats were great, but I wasn\'t impressed with the sides.', '2015-09-03'),
(10, 11, 5, 5, 5, 5, 4, 'Fantastic Lebanese food, and the atmosphere is perfect for a night out.', '2018-04-19'),
(11, 11, 4, 5, 4, 4, 4, 'Great value for money. The meats were perfectly grilled, but the service was a bit slow.', '2020-07-30'),
(12, 11, 5, 5, 5, 4, 5, 'Top-notch Lebanese food and amazing service. Would definitely return!', '2022-10-10'),

(13, 12, 5, 5, 4, 5, 5, 'The mezze was fantastic and fresh. Definitely recommend the shawarma!', '2013-02-25'),
(14, 12, 4, 4, 4, 4, 3, 'Food was good, but the service was a bit slow during peak hours.', '2016-11-12'),
(15, 12, 4, 5, 5, 4, 5, 'Great for a casual dinner. Would love to return!', '2021-02-02'),
(1, 12, 5, 5, 5, 5, 5, 'Delicious Lebanese food with great service. The shawarma is a must-try!', '2019-06-05'),

(2, 13, 5, 5, 5, 5, 5, 'Outdoor seating was perfect on a summer evening. The mezza was superb!', '2022-08-02'),
(3, 13, 4, 4, 5, 5, 5, 'Lovely experience, though a bit crowded on weekends. Great food!', '2024-01-18'),
(4, 13, 3, 3, 3, 4, 3, 'The food was okay, but I wasn\'t impressed with the service.', '2019-05-16'),
(5, 13, 5, 5, 5, 5, 5, 'The outdoor seating and mezza were fantastic. Perfect spot for summer evenings!', '2021-07-11'),

(6, 14, 5, 5, 5, 5, 4, 'Amazing shawarma and incredible desserts. The staff was super friendly!', '2020-09-25'),
(7, 14, 4, 5, 4, 4, 5, 'Great food and value for money, although it was a little noisy.', '2023-10-04'),
(8, 14, 5, 5, 5, 4, 5, 'Perfect spot for a casual dinner. Amazing Lebanese dishes!', '2021-01-25'),
(9, 14, 4, 5, 4, 5, 5, 'The food was excellent, but the service could have been quicker.', '2018-02-16'),

(1, 15, 5, 5, 5, 5, 5, 'A truly exceptional dining experience. The food was exquisite, and the staff was incredibly attentive.', '2022-07-12'),
(11, 15, 3, 4, 3, 5, 4, 'Nice location but the food was a bit bland for my liking. The service was slow too.', '2021-11-15'),
(12, 15, 2, 3, 2, 4, 3, 'Disappointing experience. The food was cold, and the staff seemed disinterested. Not likely to return.', '2023-02-03'),
(2, 15, 5, 5, 5, 5, 5, 'Everything was perfect! The steak was cooked to perfection, and the dessert was out of this world. Highly recommend!', '2023-04-01'),
(14, 15, 1, 2, 1, 3, 2, 'Terrible experience. The food was undercooked, and we had to wait over an hour for our main course. Definitely not coming back.', '2024-01-11'),

(13, 16, 4, 5, 4, 4, 4, 'Great atmosphere, but the food could have been better. Worth a visit if you are in the area.', '2021-05-25'),
(14, 16, 3, 3, 3, 4, 3, 'Decent food, but the service was really slow and the waitstaff seemed a bit disorganized.', '2023-08-17'),
(15, 16, 5, 5, 5, 5, 5, 'One of the best meals I’ve had in a long time. The seafood platter was phenomenal, and the service was exceptional!', '2022-06-08'),
(15, 16, 2, 3, 2, 3, 2, 'Unfortunately, my experience was far from good. The food lacked flavor, and the service was inattentive. I won’t be returning.', '2023-11-01'),
(10, 16, 4, 2, 1, 3, 2, 'Solid option for a night out. The food was tasty, and the location was perfect for a casual dinner with friends.', '2022-02-19');




select *
from review;
--
-- Table structure for table `signup`
--

DROP TABLE IF EXISTS `signup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `signup` (
  `signup_id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `signup_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `is_verified` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`signup_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `signup`
--

LOCK TABLES `signup` WRITE;
/*!40000 ALTER TABLE `signup` DISABLE KEYS */;
/*!40000 ALTER TABLE `signup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `user_name` varchar(100) DEFAULT NULL,
  `surname` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'alice@example.com','$2b$12$upvb9/A98EMVEKw/mVk5qO0rnQJW/LIV/MU/HuvxuvnzpXlij0KKm','Alice','Charles'),
(2,'bob@example.com','securepass','Bob','McGill'),
(3,'charlie@example.com','qwerty123','Charlie','Smith'),
(4,'diana@example.com','letmein456','Diana','Peterson'),
(5,'edward@example.com','sunshine789','Edward','Brooks'),
(6,'fay@example.com', '$2b$12$upvb9/A98EMVEKw/mVk5qO0rnQJW/LIV/MU/HuvxuvnzpXlij0KKm', 'Fay', 'Davis'),
(7,'george@example.com', 'password123', 'George', 'Taylor'),
(8,'hannah@example.com', '$2b$12$upvb9/A98EMVEKw/mVk5qO0rnQJW/LIV/MU/HuvxuvnzpXlij0KKm', 'Hannah', 'Wilson'),
(9,'ian@example.com', 'letmein123', 'Ian', 'Miller'),
(10,'julia@example.com', '$2b$12$upvb9/A98EMVEKw/mVk5qO0rnQJW/LIV/MU/HuvxuvnzpXlij0KKm', 'Julia', 'Moore'),
(11,'kyle@example.com', '1234abcd', 'Kyle', 'Taylor'),
(12,'lily@example.com', '$2b$12$upvb9/A98EMVEKw/mVk5qO0rnQJW/LIV/MU/HuvxuvnzpXlij0KKm', 'Lily', 'White'),
(13,'mike@example.com', 'password321', 'Mike', 'Green'),
(14,'nancy@example.com', '$2b$12$upvb9/A98EMVEKw/mVk5qO0rnQJW/LIV/MU/HuvxuvnzpXlij0KKm', 'Nancy', 'Adams'),
(15,'oliver@example.com', 'mypassword2023', 'Oliver', 'King');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

select *
from user;

--
-- Table structure for table `vibetype`
--

DROP TABLE IF EXISTS `vibetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vibetype` (
  `vibe_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`vibe_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vibetype`
--

LOCK TABLES `vibetype` WRITE;
/*!40000 ALTER TABLE `vibetype` DISABLE KEYS */;
INSERT INTO `vibetype` VALUES (1,'Casual Dining'),(3,'Cozy & Intermate'),(2,'Fine Dining'),(6,'Loud & Lively'),(5,'Office Eats'),(4,'Special Occasion');
/*!40000 ALTER TABLE `vibetype` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Dumping routines for database 'projectdb3'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-21 21:01:31