# Drew's Minecraft Site

This project was created for an into to Python course in 2014.  One of the requirements for the project was to NOT use a database.  All of the data needed to hard coded.

Another requirement for this project was to use Google App Engine.  I had no desire to continue using this, so it has been stripped out and replaced with Flask and Jinja2.

## Plans for future updates:

- The first order of business with this is to clean up the code.  This will mostly entail stripping out some of the code that was working with GAE but is no longer needed with Jinja doing the template rendering.

- The second update I'd like to make is to clean up the css a little and improve the functionality by adding a "back" button to the individual item pages.

- Next I will be stripping out the hard coded data and replacing it with a MySQL database and some ORM (Likely SQL Alchemy).

- The next step  will be to complete the data and add features.