import unittest
from werkzeug.security import generate_password_hash
from database import the_database

class TestDatabase(unittest.TestCase):
    def setUp(self, connection=the_database.connection):
        self.connection = connection
    
    def test_username_and_password_are_right_after_insert(self):
        username = '1'
        password = 'Testi3'
        hash_value = generate_password_hash(password)
        
        cursor = self.connection.cursor()

        values_1 = {"username": username}
        values_2 = {"username": username, "password": hash_value}

        cursor.execute("DELETE FROM users WHERE username =:username", values_1)
        cursor.execute("""INSERT INTO users (username, password)\
                          VALUES (:username, :password)""", values_2)        
        self.connection.commit()

        sql = """SELECT username, password FROM users\
                 WHERE username=:username AND password=:password"""
        result = cursor.execute(sql, values_2).fetchone()
        self.assertEqual(result[0], '1')
        self.assertEqual(result[1], hash_value)
        
        cursor.execute("DELETE FROM users WHERE username =:username", values_1)
        self.connection.commit()
        cursor.close()
        
    def test_notes_are_right_after_insert(self):
        user_id = 1
        bib_citekey = "Test"
        bib_category = "Test"
        author = "Test"
        title = "Test"
        year = "2022"
        doi_address = "https://Test"
        
        cursor = self.connection.cursor()

        values = {"user_id": user_id,\
                  "bib_citekey": bib_citekey,\
                  "bib_category": bib_category,\
                  "author": author,\
                  "title": title,\
                  "year": year,\
                  "doi_address":doi_address}

        cursor.execute("DELETE FROM notes\
                        WHERE user_id=:user_id AND\
                        bib_citekey=:bib_citekey AND\
                        bib_category=:bib_category", values)
        cursor.execute("""INSERT INTO notes
                          (user_id, bib_citekey, bib_category, author, title, year, doi_address)
                          VALUES 
                         (:user_id,
                         :bib_citekey,
                         :bib_category,
                         :author,
                         :title,
                         :year,
                         :doi_address)""", values)
        self.connection.commit()
        
        sql = """SELECT user_id, bib_citekey, bib_category, author, title, year, doi_address\
                 FROM notes WHERE user_id=:user_id AND\
                 bib_citekey=:bib_citekey AND\
                 bib_category=:bib_category"""
        result = cursor.execute(sql, values).fetchone()
        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], "Test")
        self.assertEqual(result[2], "Test")
        self.assertEqual(result[3], "Test")
        self.assertEqual(result[4], "Test")
        self.assertEqual(result[5], "2022")
        self.assertEqual(result[6], "https://Test")
        
        cursor.execute("DELETE FROM notes\
                        WHERE user_id=:user_id AND\
                        bib_citekey=:bib_citekey AND\
                        bib_category=:bib_category", values)
        self.connection.commit()
        cursor.close()
