from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('', views.crawler, name='crawler'),
    path('idea/<int:idea_id>/', views.idea, name='idea'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
]
