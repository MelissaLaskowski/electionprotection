-- LOAD DATA LOCAL INFILE  'C:/Users/importsjc/RIT/Computer Security/DB/authorized_voters.csv'
-- INTO TABLE authorized_voters
-- FIELDS TERMINATED BY ',' 
-- ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
-- IGNORE 1 ROWS;

-- LOAD DATA LOCAL INFILE  'C:/Users/importsjc/RIT/Computer Security/DB/election_timespan.csv'
-- INTO TABLE election_timespan
-- FIELDS TERMINATED BY ',' 
-- ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
-- IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE  'C:/Users/importsjc/RIT/Computer Security/DB/votes.csv'
INTO TABLE votes
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;