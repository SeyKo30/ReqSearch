
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import signup



urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_company, name='create_company'),
    path('list/', views.company_list, name='company_list'),
    path('success/', views.success_page, name='success_page'),
    path('login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('signup/', signup, name='signup'),
    path('about-us/', views.about_us, name='about_us'),
    path('upload/', views.upload_document, name='upload_document'),
    path('processing/', views.processing_page, name='processing_page'),
    path('delete_company/<int:company_id>/', views.delete_company, name='delete_company')
]
