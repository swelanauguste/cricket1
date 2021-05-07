from django.urls import path

from .views import ItemCreate, ItemDetail, ItemList, ItemUpdate

app_name = 'inventory'

urlpatterns = [
    path('', ItemList.as_view(), name='list'),
    path('<int:pk>', ItemDetail.as_view(), name='detail'),
    path('<int:pk>update', ItemUpdate.as_view(), name='update'),
    path('create', ItemCreate.as_view(), name='create'),
]
