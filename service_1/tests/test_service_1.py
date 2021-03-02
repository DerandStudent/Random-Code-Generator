from flask import url_for
from flask_testing import TestCase
import requests_mock
from unittest.mock import patch
from application import app, db
from application.models import Codes

class TestBase(TestCase):
    #create app
    def create_app(self):
        #add temp sqlite db so we dont mess with actual database
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite://data.db")
        #retrun finished
        return app
    
    #setup values in temp database
    def setup(self):
        db.create_all()
        db.session.add(Codes(code="A12341234"))
        db.session.commit()
    
    #once finished with db remove everything and close it
    def teardown(self):
        db.session.remove()
        db.close()

class TestIndex(TestBase):
    #checking for index page 
    #status code is used to translate html request codes into a 500 so there is a match
    def test_index(self):
        response = self.client.get(url_for("index"))
        self.assertEqual(response.status_code, 500)

class TestResponse(TestBase):
    def test_Simple_1(self):
        with requests_mock.mock() as test:
            test.get("http://code_part_1:5001", text ='A')
            test.get("http://code_part_2:5002", text = '0000')
            test.get("http://code_part_3:5003", text = '0000')
            response = self.client.get(url_for('index'))
            self.assertIn(b'A', response.data)
            self.assertIn(b'0000', response.data)
            self.assertIn(b'0000', response.data)
    
    def test_Simple_2(self):
        with requests_mock.mock() as test:
            test.get("http://code_part_1:5001", text ='B')
            test.get("http://code_part_2:5002", text = '1234')
            test.get("http://code_part_3:5003", text = '1234')
            response = self.client.get(url_for('index'))
            self.assertIn(b'B', response.data)
            self.assertIn(b'1234', response.data)
            self.assertIn(b'1234', response.data)
    
    def test_Simple_3(self):
        with requests_mock.mock() as test:
            test.get("http://code_part_1:5001", text ='C')
            test.get("http://code_part_2:5002", text = '8181')
            test.get("http://code_part_3:5003", text = '5353')
            response = self.client.get(url_for('index'))
            self.assertIn(b'C', response.data)
            self.assertIn(b'8181', response.data)
            self.assertIn(b'5353', response.data)
    
    def test_Simple_4(self):
        with requests_mock.mock() as test:
            test.get("http://code_part_1:5001", text ='D')
            test.get("http://code_part_2:5002", text = '9876')
            test.get("http://code_part_3:5003", text = '5432')
            response = self.client.get(url_for('index'))
            self.assertIn(b'D', response.data)
            self.assertIn(b'9876', response.data)
            self.assertIn(b'5432', response.data)
    
    def test_Simple_5(self):
        with requests_mock.mock() as test:
            test.get("http://code_part_1:5001", text ='E')
            test.get("http://code_part_2:5002", text = '2893')
            test.get("http://code_part_3:5003", text = '2839')
            response = self.client.get(url_for('index'))
            self.assertIn(b'E', response.data)
            self.assertIn(b'2893', response.data)
            self.assertIn(b'2839', response.data)
    
    def test_Simple_6(self):
        with requests_mock.mock() as test:
            test.get("http://code_part_1:5001", text ='F')
            test.get("http://code_part_2:5002", text = '7292')
            test.get("http://code_part_3:5003", text = '7292')
            response = self.client.get(url_for('index'))
            self.assertIn(b'F', response.data)
            self.assertIn(b'7292', response.data)
            self.assertIn(b'7292', response.data)


    