# app/tests.py

from django.test import TestCase, Client
from django.urls import reverse
import json

class ChatbotTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_chatbot_basic_response(self):
        """Test if chatbot endpoint returns a response"""
        url = reverse('chatbot_endpoint')
        data = {'message': 'Hello'}
        response = self.client.post(
            url, 
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('response', response.json())

    def test_chatbot_empty_message(self):
        """Test if chatbot handles empty messages properly"""
        url = reverse('chatbot_endpoint')
        data = {'message': ''}
        response = self.client.post(
            url, 
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 400)

    def test_chatbot_missing_message(self):
        """Test if chatbot handles missing message field"""
        url = reverse('chatbot_endpoint')
        data = {}
        response = self.client.post(
            url, 
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 400)
