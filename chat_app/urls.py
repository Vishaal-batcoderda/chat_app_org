from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chat.views import MessageViewSet, profile, chat_view  # Import the views for profile and chat

# Register the API routes
router = DefaultRouter()
router.register(r'messages', MessageViewSet)

# URLs for authentication and API
urlpatterns = [
    # Login and Logout
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Ensure this works correctly with logout functionality

    # Root path (redirect to login)
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='home'),

    # Profile page (redirect after login)
    path('profile/', profile, name='profile'),  # Profile page route

    # Chat page
    path('chat/', chat_view, name='chat'),  # Chat page route

    # API URLs
    path('api/', include(router.urls)),  # API paths for messages
]