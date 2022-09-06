from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from django.urls import path, reverse_lazy
from .forms import UserLoginForm
urlpatterns = [
    path('', LoginView.as_view(template_name='core/home.html',
         authentication_form=UserLoginForm, redirect_authenticated_user=True), name='login'),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('kinesiologo/crear-paciente',
         views.paciente_signup_view, name='crear-paciente'),
    path('paciente/dashboard', views.paciente_dashboard_view,
         name='paciente-dashboard'),
    path('kinesiologo/signup', views.kinesiologo_signup_view,
         name='kinesiologosignup'),
    path('kinesiologo/dashboard', views.kinesiologo_dashboard_view,
         name='kinesiologo-dashboard'),
    path('logout/', LogoutView.as_view(
        # you can use your named URL here just like you use the **url** tag in your django template
        next_page=reverse_lazy('login')
    ), name='logout'),
    path('kinesiologo/detalle_paciente/<id>/',
         views.detalle_paciente_view, name='detalle-paciente'),

]
