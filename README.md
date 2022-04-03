# Description
This is an api that allows you to receive email notifications of new releases by selected musical bands from the discogs.com database. I'm planning on using OAuth to authenticate with the discogs website thus an account is necessary.  For delivering emails I decided to stick with Mailgun.
## How to run it
In order for this api to work you need an external psql database. To connect to the database you need to set the environment variables located in config/env_vars.sh.
## Currently working features
As of yet the api is capable of registering a new user and putting it to a db, loging in and returning a JWT and changing the current status of an email.
