from django.test import TestCase, Client
from .models import Article, PriceList, About_Comment
import datetime


class NewsConnectionTests(TestCase):

    def setUp(self):
        from . import urls
        self.client = Client()
        self.app_name = urls.app_name

    def test_pages_status(self):
        """
        check if status is 200 OK
        """
        pages_list = ['', '/contacts/', '/about/', '/pricelist/']
        for i in pages_list:
            response = self.client.get('{}'.format(i))
            self.assertIs(response.status_code, 200)


class ArticleTests(TestCase):

    def setUp(self):
        self.article = Article.objects.create(title='1',
                                              article_descr='2')

    def test_check_creation_of_aticle(self):
        """
        cehck if Article was created correctly
        """
        self.assertEqual(self.article.date.date(),
                         datetime.datetime.now().date())
        self.assertIs(self.article.title, '1')
        self.assertIs(self.article.article_descr, '2')


class PriceListTests(TestCase):

    def setUp(self):
        self.pricelist = PriceList.objects.create(transp_type='1', price=2)

    def test_check_creation_of_pricelist(self):
        """
        cehck if PriceList was created correctly
        """
        self.assertIs(self.pricelist.transp_type, '1')
        self.assertIs(self.pricelist.price, 2)


class CommentsTests(TestCase):

    def setUp(self):
        self.comment = About_Comment.objects.create(author='1', comment='2',
                                                    title='3')

    def test_check_creation_of_comment(self):
        """
        cehck if Comment was created correctly
        """
        self.assertEqual(self.comment.date.date(),
                         datetime.datetime.now().date())
        self.assertIs(self.comment.author, '1')
        self.assertIs(self.comment.comment, '2')
        self.assertIs(self.comment.title, '3')
