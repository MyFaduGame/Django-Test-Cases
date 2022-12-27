from django.urls import path,include
from djangotestapp.views import UserView

urlpatterns = [
    path('view/',UserView.as_view())
]