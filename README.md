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

 - pip3 install pyopenssl
 
Set Up Database: (open mysql in the election protection directory)

- mysql -u root -p

- SOURCE DB/CreateDB.sql;

- CREATE USER 'electionAdmin'@'localhost' IDENTIFIED BY 'ElectionProtectionPass';

- GRANT ALL ON electionData.* TO 'electionAdmin'@'localhost' WITH GRANT OPTION;

- quit;

- python3 DB/insertdata.py
 
Running App:

- python3 app.py

- got to https://127.0.0.1:5000/

- due to the test server not having SSL Certificates you will see a warning from your browser that the site is unsafe, click to continue to the site. On a real server a certificate would be used to ensure this message does not effect user's experience and improve security.

Test Users:

(FullName	SSN	DOB	Has_Voted)

Aurore Canty	103867984	12122008	false

Ali Barff	501764250	12111933	true

Hanna Heam	668444039	12131962	false

Terrence Hotton	359842986	05201977	true

Nonah Sessions	430654218	07271964	true

Tannie Shervil	272761736	11301942	false

Vladamir Hurche	636633445	10191968	false

Kerrie Salvidge	705731509	05021985	false

Justinn Odams	167031092	02251935	true
