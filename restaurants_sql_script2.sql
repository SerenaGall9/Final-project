CREATE DATABASE  IF NOT EXISTS `projectdb2` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `projectdb2`;
-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: projectdb2
-- ------------------------------------------------------
-- Server version	8.4.3

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

select * 
from cuisine;

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

select *
from londonlocation;

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
  `description` varchar(5000) NOT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `restaurants`
--

LOCK TABLES `restaurants` WRITE;
/*!40000 ALTER TABLE `restaurants` DISABLE KEYS */;

/*!40000 ALTER TABLE `restaurants` ENABLE KEYS */;
UNLOCK TABLES;

select *
from restaurants;

-- DROP TABLE restaurants;

INSERT into restaurants (name, address, location_id, phone_number, website, description, menu_link, cuisine_id, vibe_id) 
VALUES 
('Coco Grill & Lounge', '34a Shad Thames, London, SE1 2YG', 2 , '+44 20 7407 7999', 'https://www.coco-restaurants.com/coco-index.html', 'Coco Grill & Lounge is a stylish alcohol-free restaurant in London offering modern Anatolian cuisine with halal ingredients, all set against the iconic backdrop of Tower Bridge. Known for its elegant ambiance, Coco features a unique Redemption Bar serving crafted alcohol-free cocktails and a scenic shisha terrace for a memorable dining experience.', 'https://www.coco-restaurants.com/menu.html', 5, 3),
('Olives and Meze','131 Clapham High St, London SW4 7SS', 2, '020 3583 7790','https://www.olivesandmeze.co.uk/', '​Olives + Meze is a contemporary Mediterranean eatery with locations in Clapham and Soho, London, celebrated for its fresh, healthy dishes like charcoal-grilled meats, vibrant salads, and house specials such as the Mix Protein Gym Box. Recognized at the 2024 British Kebab Awards, it offers a sleek dining experience and convenient takeaway options.', 'https://www.olivesandmeze.co.uk/menu', 5, 5),
('Scarpetta Canary Wharf', '20 Canada Square, London, E14 5NN', 3 , '+44 20 3649 6803', 'https://scarpettapasta.com/restaurant-canary-wharf/', "​Scarpetta Canary Wharf is a modern Italian restaurant located at 20 Canada Square, London E14 5NN, offering fresh handmade pasta, Italian cocktails, and a curated selection of wines in a stylish, lively setting. It's an ideal spot for after-work drinks, date nights, or gatherings with friends and family. ", 'https://scarpettapasta.com/wp-content/uploads/2024/05/A4-Food-Menu-1.pdf',  1, 5),
('Alexander The Great Greek Restaurant', '8 Plender Street, London, NW1 0JT', 1 ,  '+44 20 7388 1111', 'https://alexanderthegreatgreekrestaurant.co.uk/', '​Alexander The Great is a family-run Greek restaurant in Camden, London, offering authentic Mediterranean cuisine in a warm, traditional setting. Signature dishes like kleftiko and moussaka are prepared with locally sourced ingredients, making it a favorite for both casual meals and special occasions.', 'https://alexanderthegreatgreekrestaurant.co.uk/menu/', 5, 2),
('La Tagliata', '80 Upper Street, Islington, London N1 0NP, UK', 3,  '020 73 771 551', 'https://www.la-tagliata.com/?404=%27', '​La Tagliata is a family-run Italian restaurant located in Spitalfields, London, near Liverpool Street station. It offers authentic Italian cuisine in a setting reminiscent of an Italian villa, featuring themed rooms like the library and wine cellar. The restaurant specializes in traditional dishes, including its namesake tagliata steak, and provides private dining options for intimate gatherings.', 'https://www.la-tagliata.com/menu/', 1, 4), 
('Gloria Trattoria', '54–56 Great Eastern Street, Shoreditch, London EC2A 3QR' , 3, '020 4578 4370', 'https://menu.bigmammagroup.com/gloria', '​Gloria is a vibrant 1970s Capri-style trattoria located in Shoreditch, London, operated by the Big Mamma Group. It offers a lively atmosphere with a menu of Italian classics made from ingredients sourced from 180 small producers across Italy, including dishes like Spaghetti al Tartufo and Neapolitan pizzas baked in a Marana oven','https://menu.bigmammagroup.com/gloria',1, 1), 
('Chutney Mary', '73 St. James’s Street, London SW1A 1PH', 4 , '020 7629 6688', 'https://www.chutneymary.com/', '​Chutney Mary is a pioneering Indian fine dining restaurant located in St James’s, London, renowned for its elegant interiors and diverse regional Indian cuisine. Established in 1990, it offers an opulent dining experience complemented by the stylish Pukka Bar and private dining rooms', 'https://www.chutneymary.com/menu/', 2, 3),
('Dishoom Covent Garden', '12 Upper St. Martin’s Lane, London WC2H 9FB', 4, '020 7420 9320', 'https://www.dishoom.com/covent-garden/', "​Dishoom is a celebrated Indian restaurant group in the UK, inspired by the Irani cafés of Bombay. Their all-day menu offers a diverse selection of Bombay comfort food, featuring dishes from the city's cafés, grills, street stalls, and homes. Guests can enjoy options ranging from small plates and grills to biryanis and curries, all served in a setting that pays homage to the vibrant culture of Bombay", 'https://www.dishoom.com/menu/all-day-main/', 2, 6), 
('Gymkhana', '42 Albemarle Street, London W1S 4JH', 4, '020 3011 5900', 'https://gymkhanalondon.com/', "​Gymkhana is a two-Michelin-starred Indian restaurant in Mayfair, London, inspired by the elite clubs of colonial India. It offers refined North Indian cuisine with a focus on tandoor and chatpatta dishes, all set within opulent interiors that evoke the elegance of Raj-era mansions", 'https://gymkhanalondon.com/wp-content/uploads/2020/02/GYMKHANA-ALC-1.pdf', 2, 2), 
('Babel grill house' , '40 Brick lane, London E1 6RF', 3, '+44 20 7392 9675', 'https://www.babelgrillhouse.co.uk/', "Babel Grill House is a Lebanese halal restaurant located on Brick Lane in London, offering authentic Middle Eastern cuisine in a warm and inviting atmosphere. Their menu features a variety of dishes, including cold and hot mezza, grilled meats, and traditional desserts, all prepared using inherited ingredients elevated to new levels.", 'https://www.babelgrillhouse.co.uk/menu', 4,3), 
('Baba ghanouj' , '105 Gloucester Road, London, SW7 4SS', 4, '02039171660' , 'https://www.babaghanouj.co.uk/', "Baba Ghanouj is a charming Lebanese restaurant in South Kensington, offering an array of authentic dishes like shawarma, manakeesh, and vibrant mezze. With its cozy atmosphere and diverse menu, it’s a go-to spot for both casual dining and special gatherings.", "https://www.babaghanouj.co.uk/uploads/our_menu/photo_68309BABA%20GHANOUJ%202024%20MENU%20(1).pdf", 4, 4), 
('Mazar' , '11-12 Battersea Square, Battersea, London, SW11 3RA', 2, '020 7978 5374', 'https://mazarrestaurant.com/', "​Mazar Restaurant in Battersea offers an authentic Lebanese dining experience, specializing in a diverse array of hot and cold mezze dishes that showcase the rich flavors of Lebanese and Mediterranean cuisine. Located in the vibrant Battersea Square, it provides both indoor and outdoor seating, fostering a welcoming atmosphere for guests to enjoy their meals.", 'https://mazarrestaurant.com/#menu', 4, 2),
('Beit El Zaytoun', '15-17 Barrets Green Road, London, NW10 7AE', 1, '+442089611166', 'https://beitelzaytoun.com', 'Beit El Zaytoun is a celebrated Lebanese restaurant in London, renowned for its authentic cuisine and vibrant atmosphere. The menu features a wide array of traditional dishes, including mezze, grilled meats, and specialty items like lamb shawarma and kabse lahme, complemented by desserts such as baklava cheesecake and pistachio cake. ', 'https://beitelzaytoun.com/menu', 4, 1), 
('Nijo', '20 Berkeley Street, London, W1J 8EE', 4 ,'020 98862426' , 'https://nijulondon.com/', "NIJŪ is a refined Japanese restaurant in Mayfair, London, offering a contemporary take on 'katei ryōri'—traditional Japanese home-style cooking. Led by third-generation sushi master Chef Endo Kazutoshi, the restaurant features a bespoke sushi bar, a grill serving premium Wagyu and Kobe beef, and an intimate private dining space, Nipperkin, inspired by Japanese listening bars from the 1950s", 'https://nijulondon.com/menus/', 3, 3), 
('Inamo sukoshi',  '2 – 10, Bethnal Green Road, London, E1 6GY', 3  ,'0207 186 8800' , 'https://boxpark.co.uk/food-and-drink/inamo-sukoshi/', "Inamo Sukoshi at BOXPARK Wembley serves a dynamic fusion of sushi and Asian street food, featuring signature dishes like Dragon Rolls, Bao Buns, and Katsu Curry. Recognized with awards such as the Golden Chopsticks Award for Best Street Food UK in 2023, it offers a vibrant dining experience in the heart of Wembley Park ", 'https://boxpark.co.uk/food-and-drink/inamo-sukoshi/',3, 6);

select *
from restaurants;

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
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

ALTER TABLE user
ADD first_name VARCHAR(50),
ADD last_name VARCHAR(50);

UPDATE user
SET first_name = 'Alice'
WHERE email = 'alice.demo@example.com';

UPDATE user
SET last_name = 'Demo'
WHERE email = 'alice.demo@example.com';

UPDATE user
SET first_name = 'Robert'
WHERE email = 'bob.testuser@example.net';

UPDATE user
SET last_name = 'Testuser'
WHERE email = 'bob.testuser@example.net';

UPDATE user
SET first_name = 'Charlie'
WHERE email = 'charlie.fake@example.org';

UPDATE user
SET last_name = 'Fake'
WHERE email = 'charlie.fake@example.org';

UPDATE user
SET first_name = 'Dana'
WHERE email = 'dana.sample@example.com';

UPDATE user
SET last_name = 'Sample'
WHERE email = 'dana.sample@example.com';

UPDATE user
SET first_name = 'Eve'
WHERE email = 'eve.placeholder@example.io';

UPDATE user
SET last_name = 'Placeholder'
WHERE email = 'eve.placeholder@example.io';

select *
from user;



--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'alice@example.com','password123'),(2,'bob@example.com','securepass'),(3,'charlie@example.com','qwerty123'),(4,'diana@example.com','letmein456'),(5,'edward@example.com','sunshine789');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

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

select *
from vibetype;

CREATE TABLE Review (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    restaurant_id INT NOT NULL,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review VARCHAR(1000) NOT NULL,
    creation_date DATE,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (restaurant_id) REFERENCES Restaurant(restaurant_id)
);

INSERT INTO Review (user_id, restaurant_id, rating, review, creation_date) VALUES
(1, 1, 5, 'An unforgettable Mediterranean experience! The ambiance was warm and romantic.', '2025-04-15'),
(2, 2, 4, 'Fresh sushi and stylish interior. Loved the cozy vibe.', '2025-04-10'),
(3, 3, 5, 'Absolutely amazing Indian food! Perfect for a date night.', '2025-04-12'),
(4, 1, 3, 'Nice place but the service was a bit slow.', '2025-04-14'),
(2, 3, 4, 'Elegant setting and flavorful dishes. Will definitely return.', '2025-04-16'),
(5, 2, 5, 'One of the best Japanese spots in London. Highly recommend the omakase.', '2025-04-17'),
(1, 2, 2, 'Great food, but too noisy for my taste.', '2025-04-11'),
(4, 3, 5, 'Chutney Mary never disappoints. A true fine dining experience.', '2025-04-13');
    
select * 
From Review;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-16 21:11:37