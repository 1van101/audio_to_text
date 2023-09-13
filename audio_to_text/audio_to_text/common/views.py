from django.contrib.auth import get_user_model

from django.views import generic as views


UserModel = get_user_model()


class IndexView(views.TemplateView):
    template_name = 'common/index.html'
    user = UserModel


