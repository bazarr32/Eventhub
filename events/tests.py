from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from accounts.models import User
from events.models import Event, Category


class EventTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345test'
        )

        self.category = Category.objects.create(name='Sport')

        self.event = Event.objects.create(
            title='Test Event',
            description='Test Description',
            location='Shumen',
            date=timezone.now(),
            capacity=10,
            organizer=self.user
        )
        self.event.categories.add(self.category)

    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_event_detail_loads(self):
        response = self.client.get(reverse('event_detail', kwargs={'id': self.event.id}))
        self.assertEqual(response.status_code, 200)

    def test_create_event_requires_login(self):
        response = self.client.get(reverse('create_event'))
        self.assertEqual(response.status_code, 302)

    def test_logged_user_can_access_create(self):
        self.client.login(username='testuser', password='12345test')
        response = self.client.get(reverse('create_event'))
        self.assertEqual(response.status_code, 200)

    def test_event_created(self):
        self.client.login(username='testuser', password='12345test')

        response = self.client.post(reverse('create_event'), {
            'title': 'New Event',
            'description': 'Desc',
            'location': 'Park',
            'date': '04.09.2026 18:30',
            'capacity': 5,
            'categories': [self.category.id]
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Event.objects.count(), 2)

    def test_owner_can_edit_event(self):
        self.client.login(username='testuser', password='12345test')
        response = self.client.get(reverse('edit_event', kwargs={'id': self.event.id}))
        self.assertEqual(response.status_code, 200)

    def test_other_user_cannot_edit(self):
        User.objects.create_user(username='other', password='12345test')

        self.client.login(username='other', password='12345test')
        response = self.client.get(reverse('edit_event', kwargs={'id': self.event.id}))

        self.assertNotEqual(response.status_code, 200)

    def test_owner_can_delete_event(self):
        self.client.login(username='testuser', password='12345test')

        response = self.client.post(reverse('delete_event', kwargs={'id': self.event.id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Event.objects.count(), 0)

    def test_other_user_cannot_delete(self):
        User.objects.create_user(username='other', password='12345test')

        self.client.login(username='other', password='12345test')
        response = self.client.post(reverse('delete_event', kwargs={'id': self.event.id}))

        self.assertEqual(Event.objects.count(), 1)

    def test_api_list(self):
        response = self.client.get('/api/events/')
        self.assertEqual(response.status_code, 200)

    def test_api_detail(self):
        response = self.client.get(f'/api/events/{self.event.id}/')
        self.assertEqual(response.status_code, 200)

    def test_login_works(self):
        login = self.client.login(username='testuser', password='12345test')
        self.assertTrue(login)

    def test_logout(self):
        self.client.login(username='testuser', password='12345test')
        self.client.logout()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)