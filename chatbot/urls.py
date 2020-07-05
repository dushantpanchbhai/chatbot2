from django.contrib import admin
from django.urls import path
from bot import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.first_page,name="first_page"),
    path('home/',views.home,name="home"),
    path('feedback/',views.feedback, name='feedback'),
    path('chat/',views.chat,name='chat'),
    path('contactus/', views.contactus, name='contactus'),
    path('info/',views.info, name='info'),
    path('msg/', views.chat, name='chat'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
