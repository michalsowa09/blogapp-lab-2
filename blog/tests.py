from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from django.urls import reverse

class BlogTests(TestCase):
    def setUp(self):
        #Tworze testowego użytkownika i posta (status published):

        self.user = User.objects.create_user(username='testuser', password='password123')
        self.post = Post.objects.create(
            title='Testowy Post',
            content='Treść testowa',
            author=self.user,
            status='published'
        )

    def test_post_model_str(self):
        # Testuje czy model zwraca poprawny tytuł:

        self.assertEqual(str(self.post), 'Testowy Post')

    def test_post_list_view(self):
        # Testuje czy strona główna się ładuje i zawiera tytuł posta:

        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Testowy Post')
