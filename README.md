# Welcome to your Flamingo Bingo CDK project!

API End Points (Please make sure to hit api's with API Key Mentioned)
-------------

Player Registration API:
-----------------------

Invoke Url : https://m97t449xz5.execute-api.us-west-2.amazonaws.com/dev/playerRegistration
Method : POST
Pay Load: 
{
"email_id": "naveena@gmail.com",
"name": "naveena@gmail.com"
}

API Key: bmecQdyWPb6dfWlyoVgUqjcbOO4H0lW2yw7xURDi


Flamingo Sighting Submission API:
--------------------------------

Invoke Url : https://m97t449xz5.execute-api.us-west-2.amazonaws.com/dev/flamingoSightingSubmission
Method : POST
Pay Load: 
{
"region":"South America"
}

API Key:bmecQdyWPb6dfWlyoVgUqjcbOO4H0lW2yw7xURDi

Flamingo Get Card API:
----------------------

Invoke Url :https://m97t449xz5.execute-api.us-west-2.amazonaws.com/dev/getCard?email=naveena@gmail.com'
Method : GET
API Key:bmecQdyWPb6dfWlyoVgUqjcbOO4H0lW2yw7xURDi


Curl Commands to hit API:
------------------------

1.Player Registration API:
-----------------------
curl -X POST \
  'https://m97t449xz5.execute-api.us-west-2.amazonaws.com/dev/playerRegistration' \
  -H 'Content-Type: application/json' \
  -H 'x-api-key: bmecQdyWPb6dfWlyoVgUqjcbOO4H0lW2yw7xURDi' \
  -d '{
        "email_id": "naveena@gmail.com",
        "name": "naveena@gmail.com"
      }'


2.Flamingo Sighting Submission API:
----------------------------------
curl -X POST \
  'https://m97t449xz5.execute-api.us-west-2.amazonaws.com/dev/flamingoSightingSubmission' \
  -H 'Content-Type: application/json' \
  -H 'x-api-key: bmecQdyWPb6dfWlyoVgUqjcbOO4H0lW2yw7xURDi' \
  -d '{
        "region":"South America"
      }'

3.Flamingo Get Card API:
----------------------

curl -X GET -H "x-api-key: bmecQdyWPb6dfWlyoVgUqjcbOO4H0lW2yw7xURDi" 'https://m97t449xz5.execute-api.us-west-2.amazonaws.com/dev/getCard?email='naveena@gmail.com'


UI Url:(Replace localhost with your local server)
-------
http://localhost:8000/PlayerRegistration.html
http://localhost:8000/game.html?email=sri@gmail.com&dataSource=customer
http://localhost:8000/game.html?email=sri@gmail.com&dataSource=mock (use the mock page to get an idea on UI design if you have any permission related issue)


If I have more time to work on assignments I will work on following areas
-------------------------------------------------------------------------

Backend improvements:
--------------------

I will implement field level validations for each and every api

I would change the design of data models in way it can incorporate games in the system where multiple player can participate in it 

I will incorporate the room functionality where one player can create it and share it to another players

I will incorporate the functionality which will determine the winner of the game 


UI Improvments:
---------------
I will incorporate the api for player registration and flamingo sighting submission

I will incorporate aavtar selection option while creating the player,Display Winner of the game,Room Creation UI


Note:
----
As the main functionality of assignment is working as expected i'm submitting the assignment,I am facing dependency issues with apis and dynamo db tables while creating using CDK.
I was busy with office work and if i get some time i'll work on it and resubmit the assignment





