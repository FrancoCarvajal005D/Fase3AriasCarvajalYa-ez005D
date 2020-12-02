from django.urls import path 
from noticia import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contacto/',views.contacto, name='contacto'),
    path('quienes_somos/',views.quienes_somos, name='quienes_somos'),
    path('categorias/',views.categorias, name='categorias'),
]

urlpatterns+=[
    path('contacto/create/', views.ContactoCreate.as_view(), name='contacto_create'),
    path('contacto/<int:pk>/update/', views.ContactoUpdate.as_view(), name='contacto_update'),
    path('contacto/<int:pk>/delete/', views.ContactoDelete.as_view(), name='contacto_delete'),
]