from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from djangotestapp.models import user

class UserTestCases(APITestCase):
    @classmethod
    def SetUpTestData(cls):
        print("Running test data")
        email = "example@gmail.com"
        username = "abc xyz"

        User = user.objects.create(email=email,username=username)
        User.save()

    def TestingData(self):
        response = self.client.post('/user/view/',{'email':'example@gmail.com','username':'xyz abc'})
        self.assertEqual(response.status_code,200)

        response = self.client.post('/user/view/',{'email':'example@gmail.com','username':'xyz abc'})
        self.assertEqual(response.status_code,400)
        