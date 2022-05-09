from .import views
from django.urls import path
app_name='farmapp'
urlpatterns = [
    path('',views.fun,name='fun'),
    path('farm/<int:farm_id>/',views.detail,name='detail'),
    path('add/',views.add_farm,name='add_farm'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    ]