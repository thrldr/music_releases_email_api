# Description
This is an api that allows you to receive email notifications of new releases by selected bands from the discogs.com database. I'm going to use an OAuth to authenticate with the service's api so an account is necessary. For email sending I'm plainning on using Mailgun's python client.
## How to run it
In order for this api to work it requires an external database. I've decided to use postgresql. To connect to the database you need to set the environment variables located in env_vars.sh.
