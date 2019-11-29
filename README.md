# Emotion-based-Music-Player

## Steps to install
- git clone or git pull
- Run the following command first:
> mysql -u <user> -p moodplayer < '/Path/of/the/project'/Database.sql

- Make a seperate keys.py file and add it in the root of your project.
- Add the following lines:

> user = "<your-sql-username>"
> password = "<your-sql-password>"
> paralleldots_api_key = "<contact-me-for-this or get-your-own>"

- Don't worry, this file is in .gitignore, so none of your details would be leaked

- Run python3 main.py
