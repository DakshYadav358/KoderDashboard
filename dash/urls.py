from django.urls import path

from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('Blog_Dashboard', views.Blog_Dashboard, name='Blog_Dashboard'),
        path('Tables', views.Tables, name='Tables'),
        path('User_Profile', views.User_Profile, name='User_Profile'),
        path('Forms_And_Components', views.Forms_And_Components, name='Forms_And_Components'),
        path('Errors', views.Errors, name='Errors'),
        path('Blog_Posts', views.Blog_Posts, name='Blog_Posts'),
        path('Add_New_Posts', views.Add_New_Posts, name='Add_New_Posts')
]
