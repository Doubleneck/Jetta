from database import Database

def build():
    Database().reset_database()

if __name__ == "__main__":
    build()
