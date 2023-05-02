from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import ShoppingCart
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from common.views import TitleMixin


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'TOPS_CROPS - Авторизация'


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Отлично! Регистрация прошла успешно!'
    title = 'TOPS_CROPS - Регистрация'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'TOPS_CROPS - Личный кабинет'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['shopping_carts'] = ShoppingCart.objects.filter(
            user=self.object)
        return context

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))
