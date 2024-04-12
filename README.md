# Welcome to your Flamingo Bingo CDK project!

API End Points (Please make sure to hit api's with API Key Mentioned)
-------------

Player Registration API:
-----------------------
Invoke Url : https://y70hnbtaqd.execute-api.us-west-2.amazonaws.com/dev/playerRegistration
Method : POST 
Pay Load: 
{ 
"email_id": "naveena@gmail.com", 
"name": "naveena"
}
API Key: dummy_api_key

Flamingo Sighting Submission API:
--------------------------------
Invoke Url : https://y70hnbtaqd.execute-api.us-west-2.amazonaws.com/dev/flamingoSightingSubmission
Method : POST
Pay Load: 
{
"region":"South America"
}
API Key: dummy_api_key


Flamingo Get Card API:
----------------------
Invoke Url :https://y70hnbtaqd.execute-api.us-west-2.amazonaws.com/dev/getCard?email=sri@gmail.com
Method : GET
API Key: dummy_api_key

Curl Commands to hit API:
------------------------

1.Player Registration API:
-----------------------
curl -X POST \
  'https://y70hnbtaqd.execute-api.us-west-2.amazonaws.com/dev/playerRegistration' \
  -H 'Content-Type: application/json' \
  -H 'x-api-key: dummy-api-key' \
  -d '{
        "email_id": "naveena@gmail.com",
        "name": "naveena"
      }'

2.Flamingo Sighting Submission API:
----------------------------------
curl -X POST \
  'https://y70hnbtaqd.execute-api.us-west-2.amazonaws.com/dev/flamingoSightingSubmission' \
  -H 'Content-Type: application/json' \
  -H 'x-api-key: dummy-api-key' \
  -d '{
        "region":"South America"
      }'

3.Flamingo Get Card API:
----------------------

curl -X GET -H "x-api-key:ZyohwUpy6h53vrkgdy7JM9ZTuGRkds112eIYjzjC" 'https://y70hnbtaqd.execute-api.us-west-2.amazonaws.com/dev/getCard?email=sri@gmail.com'

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


Git Command (Code resides in master branch og repo)
-----------
git clone -b master https://github.com/naveena8082/FlamingoBingoApp.git


Note:
----
Changes Made:
------------
You will be now able to register player from frontend and also perform sighting submission from frontend

1. Created AWS resources using aws cdk 
2. Integrated API's in frontend for player registration and sighting submission
3. Added alert messages
4. Restructured the frontend and backend code











