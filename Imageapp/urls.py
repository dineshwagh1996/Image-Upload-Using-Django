from django.urls import path
from Imageapp import views


urlpatterns = [
    path('display/', views.get),

    path('ImageUpload/', views.ImgaeUpload),
    path('success', views.success),

]
