from django.shortcuts import render
from django.views.generic import ListView, FormView, CreateView
from .models import Users, Teacher, Saqlovchi, Banner, Kurs, Blog, Gallery
from httpx import get
from django.contrib.auth import login,logout
from django.shortcuts import redirect
from .mixins import NotLoginRequiredMixin
from .forms import UserCreateForm, UserLoginForm, BlogForm

from django.views import View
BOT_TOKEN = '7219637434:AAFLN2MS5UcE1QSDFH4P_Vr_xSZgZYXRIfg'


class IndexView(ListView):
    model = Teacher
    context_object_name = 'teacher'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        banner = Banner.objects.all()
        course = Kurs.objects.all()
        blogs = Blog.objects.all()
        gallery = Gallery.objects.all()

        contex['banner'] = banner
        contex['course'] = course
        contex['blogs'] = blogs
        contex['gallery'] = gallery
        return contex
    


class AboutView(ListView):
    model = Teacher
    context_object_name = 'about'
    template_name = 'about.html'  

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        banner = Banner.objects.all()
        gallery = Gallery.objects.all()
        contex['gallery'] = gallery
        contex['banner'] = banner
        return contex
    


class BlogView(ListView):
    model = Teacher
    context_object_name = 'blog'
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        banner = Banner.objects.all()
        blog = Blog.objects.all()
        contex['banner'] = banner
        contex['blog'] = blog
        contex['blog_form'] = BlogForm()
        return contex
    


# class ContactView(ListView):
#     model = Banner
#     context_object_name = 'contact'
#     template_name = 'contact.html'  

#     def get_context_data(self, **kwargs):
#         contex = super().get_context_data(**kwargs)
#         banner = Banner.objects.all()
#         contex['banner'] = banner
#         return contex
    


def send_message(chat_id, message) :
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = get(url, params=params)
   
    # print(response.text, response.status_code)


def contactview(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        email = data.get('email')
        message = data.get('message')
        last_name = data.get('last_name')
        phone = data.get('phone')
        text = f"""
Foydalanuvchi ismi: {first_name}
Foydalanuvchining familiyasi: {last_name}
Foydalanuvchi email: {email}
Foydalanuvchining telefon raqami: {phone}
Foydalanuvchining habari: {message}
"""
        data = Saqlovchi.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            message = message
        )
        data.save()
        send_message(6329326811, text)
    banners = Banner.objects.all()
    return render(request, 'contact.html', context={'banner': banners}) 



class CoursesView(ListView):
    model = Kurs
    context_object_name = 'course'
    template_name = 'courses.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        banner = Banner.objects.all()
        contex['banner'] = banner
        return contex
    


class TecherView(ListView):
    model = Teacher
    context_object_name = 'teachers'
    template_name = 'teacher.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        banner = Banner.objects.all()
        contex['banner'] = banner
        teachers  = Teacher.objects.all()
        contex['teachers'] = teachers 
        return contex



class UserCreateView(NotLoginRequiredMixin, CreateView):
    model = Users
    form_class = UserCreateForm
    template_name = 'register.html'
    success_url = '/'


class UserSigninView(FormView):
    form_class = UserLoginForm
    template_name = 'login.html'
    success_url = '/'


    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = Users.objects.filter(username=username).first()
        if user and user.check_password(password):
            login(self.request, user)
            return redirect('/') 
        return super().form_valid(form)
    

class UserLogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/')
    