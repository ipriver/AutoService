from django.test import TestCase, Client
from .models import Article
import datetime


class NewsConnectionTests(TestCase):

    def setUp(self):
        from . import urls
        self.client = Client()
        self.app_name = urls.app_name

    def test_check_mainpage_status(self):
        """
        check if status is 200 OK
        """
        response = self.client.get('/{}/'.format(self.app_name))
        self.assertIs(response.status_code, 200)


class ArticleTests(TestCase):

    def setUp(self):
        self.article = Article.objects.create(title='1',
                                              article_descr='2')

    def test_check_creation(self):
        """
        cehck if Article was created correctly
        """
        self.assertEqual(self.article.date.date(),
                         datetime.datetime.now().date())
        self.assertIs(self.article.title, '1')
        self.assertIs(self.article.article_descr, '2')
