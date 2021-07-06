# Hatchways Backend Assignment

This project is a flask based API with all the mentioned endpoints. 
Requirements.txt is included in the folder but no external library except flask and requests has been used

I have never worked with custom cache storage and using redis for this application meant extra work for you to assess it so I have built a **simple file based cache system** which is written in **python**.
Every time a new tag  is used to find posts actual API call will be made otherwise if the tag already exists in our cache it will try to retrieve the posts from the **cache.json**  file.
It does not handle the usecase where newer posts are added at the URL provided by you, It would get complex to maintain a cache that way.

**Steps to run the project:**
 - python3 api/api.py - to run the server
 - python3 tests/tests.py - to run the server
 
 Made by Nishad Raisinghani
