# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import signup

class AuthenticationTests(TestCase):
    def setUp(self):
        self.url = reverse("signup")
        self.resp = self.client.get(self.url)


    def test_auth_status_code(self):
        """:ac: Returns a status code 200."""
        self.assertEqual(self.resp.status_code, 200)


    def test_csrf(self):
        self.assertContains(self.resp, "csrfmiddlewaretoken")


    def test_contains_user_form(self):
        form_test = self.resp.context.get("form")
        self.assertIsInstance(form_test, UserCreationForm)

    def test_form_inputs(self):
        self.assertContains(self.resp, '<input', 5)
        self.assertContains(self.resp, 'type="text"', 1)
        self.assertContains(self.resp, 'type="email"', 1)
        self.assertContains(self.resp, 'type="password"', 2)
