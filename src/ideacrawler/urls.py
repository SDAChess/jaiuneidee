from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('idea/<int:idea_id>/', views.idea, name='idea'),
    path('submit/', views.submit, name='submit'),
    path('accounts/', include('django.contrib.auth.urls')),
]
