from django.contrib import admin
from django.contrib import admin
from .models import Event, Category, Participation


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'location', 'capacity', 'organizer')
    list_filter = ('date',)
    search_fields = ('title', 'location')


@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'joined_at')
# Register your models here.
