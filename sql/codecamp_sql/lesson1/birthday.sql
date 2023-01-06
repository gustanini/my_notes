CREATE TABLE friends(
  id INTEGER,
  name TEXT,
  birthday DATE
); --Create a table named friends with three columns

INSERT INTO friends (id,name,birthday)
VALUES (1, 'Ororo Munroe', "1940-5-30");
INSERT INTO friends (id,name,birthday)
VALUES (2, 'Stefano Pimentel', "2010-4-3");
INSERT INTO friends (id,name,birthday)
VALUES (3, 'gusta nini', "1888-5-30");
-- Add some people

UPDATE friends
SET name = 'Storm'
WHERE id = 1 AND name = 'Ororo Munroe';
-- change ororo's name

ALTER TABLE friends
ADD COLUMN email TEXT;
--add email column

UPDATE friends
SET email = 'storm@codecademy.com'
WHERE id = 1 AND name = 'Storm';
UPDATE friends
SET email = 'keloke@codecademy.com'
WHERE id = 1 AND name = 'Stefano Pimentel';
UPDATE friends
SET email = 'gusta@codecademy.com'
WHERE id = 1 AND name = 'gusta nini';
-- update email addresses
DELETE FROM friends
WHERE ID = 1;
-- delete storm


SELECT * FROM friends;