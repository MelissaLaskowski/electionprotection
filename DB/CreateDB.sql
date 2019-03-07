CREATE SCHEMA `electionData` DEFAULT CHARACTER SET utf8 ; /* NOTE: sticking to a set of valid characters, like UTF-8, will benefit overall security. */

/* Create 'election_timespan' Table. This table holds the start dates and times of the election. They should not be changed. */
CREATE TABLE `electionData`.`election_timespan` (
  `start_time` DATETIME NOT NULL,
  `end_time` DATETIME NOT NULL);

/* Create 'votes' Table. This table holds each vote in the form of 'voter_id' the anonymous identifier and 'candidate_id' the id of the candidate the vote was placed for. */
CREATE TABLE `electionData`.`votes` (
  `voter_id` VARCHAR(64) NOT NULL,
  `candidate_id` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`voter_id`),
  INDEX `candidate_idx` (`candidate_id` ASC));

/* Create 'authorized_voters' Table. This table holds the unencrypted fields: 'full_legal_name' and 'salt'. This table holds the encrypted fields: 'dob', 'ssn', and 'has_voted' */
CREATE TABLE `electionData`.`authorized_voters` (
  `full_legal_name` VARCHAR(256) NOT NULL,
  `dob` VARCHAR(64) NOT NULL,
  `ssn` VARCHAR(64) NOT NULL,
  `has_voted` VARCHAR(64) NOT NULL,
  `salt` VARCHAR(64) NULL,
  PRIMARY KEY (`full_legal_name`));
