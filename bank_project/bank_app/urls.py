from django.urls import path

from bank_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('new/',views.new_page,name='new'),
    path('form/',views.form_view,name='form_view')

]