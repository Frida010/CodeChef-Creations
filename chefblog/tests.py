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


# Comment model tests
class CommentModelTest(TestCase):
    def test_comment_is_linked_to_correct_post(self):
        # Creating a test Post instance
        post = Post.objects.create(
            title='Test Post', slug='test-post', author=User.objects.create_user(
                username='testuser', password='testpassword'), content='Test content')
        # Creating a test Comment instance linked to the test Post
        comment = Comment(post=post, name='Test Commenter',
                          email='test@example.com', body='Test comment body')
        comment.save()
        # Asserting that the comment is correctly linked to the post
        self.assertEqual(comment.post, post)

    def test_comment_approval(self):
        # Creating a test Post instance
        post = Post.objects.create(
            title='Test Post', slug='test-post', author=User.objects.create_user(
                username='testuser', password='testpassword'), content='Test content')
        # Creating a test Comment instance linked to the test Post
        comment = Comment(post=post, name='Test Commenter',
                          email='test@example.com', body='Test comment body')
        comment.save()
        # Asserting that the comment starts as not approved
        self.assertFalse(comment.approved)
        # Approving the comment and asserting that it is now approved
        comment.approved = True
        comment.save()
        self.assertTrue(comment.approved)


# SavedPost model tests
class SavedPostModelTest(TestCase):
    def test_saved_post_is_linked_to_correct_user_and_post(self):
        # Creating a test user
        user = User.objects.create_user(
            username='testuser', password='testpassword')
        # Creating a test Post instance
        post = Post.objects.create(
            title='Test Post', slug='test-post', author=user, content='Test content')
        # Creating a test SavedPost instance linked to the test user and post
        saved_post = SavedPost(user=user, post=post)
        saved_post.save()
        # Asserting that the saved post is correctly linked to the user and post
        self.assertEqual(saved_post.user, user)
        self.assertEqual(saved_post.post, post)

    def test_user_can_unsave_post(self):
        # Creating a test user
        user = User.objects.create_user(
            username='testuser', password='testpassword')
        # Creating a test Post instance
        post = Post.objects.create(
            title='Test Post', slug='test-post', author=user, content='Test content')
        # Creating a test SavedPost instance linked to the test user and post
        saved_post = SavedPost(user=user, post=post)
        saved_post.save()
        # Asserting that the user has a saved post
        self.assertTrue(user.savedpost_set.exists())
        # Deleting the saved post and asserting that the user no longer has any saved posts
        saved_post.delete()
        self.assertFalse(user.savedpost_set.exists())
