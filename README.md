# hackvento-19-submission-blue-print
hackvento-19-submission-blue-print created by GitHub Classroom


<H1> Email based website update system. </h1>

Almost all the organizations and educational institutions have a website these days, but it's often observed that the website 
is not up to date it's mainly due to the fact that updating website is a tedious process.
We created a web app that enables the users to use his/her email address, to basically send an email to the website itself and 
upadte the content over there.

We first signed up on google cloud platform to obtain the OAUTH token for using the gmail API, then in the DJango app, user is 
asked to enter email when using the app first time. This email would be used to update his/her website. He is then given 
a link which he needs to paste on his webpage.

When he sends an email to the gmail id given to him the DJango web app detects it and automatically upadates the database 
related to his website. When the website is opened the chagnes are displayed there.

Further, 
this can be used as a replacement or in a complementary way to SLACK.

<h2> Use cases : </h2>

1. College and educational institutions 
2. News agencies 
3. Government websites 
4. Anybody who updates his website frequently 

Further, this can be connected to a text classifier so that we can classify the text before updating the website. 
