from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post

class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user_1 = User.objects.create_user(username='test_user_1', password='p@ssw0rd')
        test_user_1.save()

        test_post = Post.objects.create(author=test_user_1, title='Blog title', body='body content')
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        
        self.assertEqual(author, 'test_user_1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'body content')
