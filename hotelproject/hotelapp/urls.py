from . import views
from django.urls import path
app_name='hotelapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('hotel/<int:hotel_id>/',views.detail,name='detail'),
    path('add/',views.add_hotel,name='add_hotel'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]
