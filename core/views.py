from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from events.models import Event
from events.forms import EventForm


class HomeView(ListView):
    model = Event
    template_name = 'home.html'
    context_object_name = 'events'


class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
    context_object_name = 'event'
    pk_url_kwarg = 'id'


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'create_event.html'
    login_url = '/accounts/login/'

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')


class EventEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'edit_event.html'
    context_object_name = 'event'
    pk_url_kwarg = 'id'
    login_url = '/accounts/login/'

    def test_func(self):
        event = self.get_object()
        return event.organizer == self.request.user

    def get_success_url(self):
        return reverse_lazy('event_detail', kwargs={'id': self.object.id})


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'delete_event.html'
    context_object_name = 'event'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    login_url = '/accounts/login/'

    def test_func(self):
        event = self.get_object()
        return event.organizer == self.request.user