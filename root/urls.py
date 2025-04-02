from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.views import IndexView, AboutView, BlogView, CoursesView, TecherView, contactview,UserCreateView, UserSigninView, UserLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('kurs/', CoursesView.as_view(), name='kurs'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('aloqa/', contactview, name='aloqa'),
    path('oqituvchi/', TecherView.as_view(), name='teacher'),


    path('signup/', UserCreateView.as_view(), name='user_create'),
    path('singin/', UserSigninView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
