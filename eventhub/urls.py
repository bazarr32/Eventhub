from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import HomeView, EventDetailView, EventCreateView, EventEditView, EventDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('event/<int:id>/', EventDetailView.as_view(), name='event_detail'),
    path('create/', EventCreateView.as_view(), name='create_event'),
    path('event/<int:id>/edit/', EventEditView.as_view(), name='edit_event'),
    path('event/<int:id>/delete/', EventDeleteView.as_view(), name='delete_event'),
    path('accounts/', include('accounts.urls')),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)