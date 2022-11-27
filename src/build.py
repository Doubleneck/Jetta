from database import Database

def build():
    Database().initialize_database()

if __name__ == "__main__":
    build()
