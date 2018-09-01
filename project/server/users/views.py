from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name="auth/loginPage.html"


class RegisterView(TemplateView):
    template_name="auth/registrationPage.html"
