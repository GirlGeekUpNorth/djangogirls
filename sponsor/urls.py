from django.urls import path
from django.contrib.auth.decorators import login_required

from sponsor.views import SponsorRequestView


urlpatterns = [
    path('sponsor-request/', login_required(SponsorRequestView.as_view()),
        name='sponsor-request'),
]
