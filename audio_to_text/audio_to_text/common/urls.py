from django.urls import path

from audio_to_text.common.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
)