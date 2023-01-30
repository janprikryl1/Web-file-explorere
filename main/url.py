from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lgn_in', views.lgn_in, name='lgn_in'),
    path('newctg', views.new_ctg, name='new_ctg'),
    path('lg_out', views.lg_out, name="lg_out"),
    path('sign_in', views.sign_in, name="sign_in"),
    path('register', views.register, name='register'),
    path('categories/<str:category>', views.ctg, name="category"),
    path('itm', views.itm, name='itm'),
    path('add_file', views.add_file, name='add_file'),
    path('del_file', views.del_file, name='del_file'),
    path('del_category', views.del_catg, name='del_category'),
]