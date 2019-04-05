# election protection
Security Election Project

Start the set up by cloning this repo to your desired location

git clone https://github.com/MelissaLaskowski/electionprotection.git

Requirements:

 - python 3.7 (should work with most versions of python 3)
 
 - pip3 install Flask
 
 - pip3 install mysql
 
 - pip3 install mysql-connector-python
 
 - pip3 install flask-login
 
 - pip3 install flask-wtf
 
Set Up Database: (open mysql in the election protection directory)

- mysql -u root -p

- SOURCE DB/CreateDB.sql;

- CREATE USER 'electionAdmin'@'localhost' IDENTIFIED BY 'ElectionProtectionPass';

- GRANT ALL ON electionData.* TO 'electionAdmin'@'localhost' WITH GRANT OPTION;

- quit;

- python3 DB/insertdata.py
 
Running App:

- python3 app.py

- got to http://127.0.0.1:5000/ 

Test Users:

(FullName	SSN	DOB	Has_Voted)

Aurore Canty	103-86-7984	12/12/2008	false

Ali Barff	501-76-4250	12/11/1933	true

Hanna Heam	668-44-4039	12/13/1962	false

Terrence Hotton	359-84-2986	5/20/1977	true

Nonah Sessions	430-65-4218	7/27/1964	true

Tannie Shervil	272-76-1736	11/30/1942	false

Vladamir Hurche	636-63-3445	10/19/1968	false

Kerrie Salvidge	705-73-1509	5/2/1985	false

Justinn Odams	167-03-1092	2/25/1935	true
