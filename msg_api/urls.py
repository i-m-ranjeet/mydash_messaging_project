from django.urls import path
from msg_api import views
# from rest_framework.authtoken.views import obtain_auth_token
# from msg_api.views import CustomAuthToken

urlpatterns = [
    path('messages/',views.Messages.as_view()),
    path('usertoken/',views.TokenAuthantication.as_view())
]