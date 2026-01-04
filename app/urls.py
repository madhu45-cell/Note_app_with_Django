from django.urls import path, include
from .views import indexview, aboutview, savedataview, deleteview, updateviewpage
urlpatterns = [
    path('', indexview, name='home'),
    path('about/', aboutview, name='about'),
    path('save-data/', savedataview, name='save_data'),
    path('delete/<int:id>', deleteview, name='delete'),
    path('update/<int:id>', updateviewpage, name='update')
]
