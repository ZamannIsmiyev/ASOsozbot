from os import getenv

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv('5509121112:AAE3XG5Rrq1v-B1NAG1ThV6oZHUEJx1v1bA
MONGO_URI = getenv('mongodb+srv://aylak:aylak@cluster0.cd5my.mongodb.net/Cluster0?retryWrites=true&w=majority')
SUDO_USERS = list(map(int, getenv('1809457546').split()))
