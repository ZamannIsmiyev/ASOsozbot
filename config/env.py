from os import getenv

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv('5469320918:AAE2F2s26dSsEW4gGZDKKK_2pqc5qgJu9Ng
MONGO_URI = getenv('mongodb+srv://aylak:aylak@cluster0.cd5my.mongodb.net/Cluster0?retryWrites=true&w=majority')
SUDO_USERS = list(map(int, getenv('1809457546').split()))
