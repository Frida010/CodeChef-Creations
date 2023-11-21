from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Post, Comment, SavedPost

# Category model tests
class CategoryModelTest(TestCase):
    def test_str_representation(self):
        # Creating a test Category instance
        category = Category(name='Test Category',
                            description='A test category')
        # Asserting that the string representation is as expected
        self.assertEqual(str(category), 'Test Category')


# Post model tests
class PostModelTest(TestCase):
    def setUp(self):
        # Creating a test user for authoring posts
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

    def test_number_of_likes(self):
        # Creating a test Post instance
        post = Post(title='Test Post', slug='test-post',
                    author=self.user, content='Test content')
        post.save()

        # Creating two users who like the post
        user1 = User.objects.create_user(
            username='user1', password='password1')
        user2 = User.objects.create_user(
            username='user2', password='password2')
        post.likes.add(user1, user2)

        # Asserting that the number of likes is correctly counted
        self.assertEqual(post.number_of_likes(), 2)


# Comment model tests
class CommentModelTest(TestCase):
    def test_str_representation(self):
        # Creating a test Post instance for associating the comment
        post = Post(title='Test Post', slug='test-post', author=User.objects.create_user(
            username='testuser', password='testpassword'), content='Test content')
        post.save()

        # Creating a test Comment instance
        comment = Comment(post=post, name='Test Commenter',
                          email='test@example.com', body='Test comment body')
        # Asserting that the string representation is as expected
        self.assertEqual(
            str(comment), 'Comment Test comment body by Test Commenter')


# SavedPost model tests
class SavedPostModelTest(TestCase):
    def test_str_representation(self):
        # Creating a test user
        user = User.objects.create_user(
            username='testuser', password='testpassword')
        # Creating a test Post instance for associating with the SavedPost
        post = Post(title='Test Post', slug='test-post',
                    author=user, content='Test content')
        post.save()
