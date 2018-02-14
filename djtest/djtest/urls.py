from django.contrib import admin
from django.urls import path
from djapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('thing/', views.DjappView.as_view()),
    path('thing/<slug:thing1>/', views.DjappView.as_view()),
    path('thing/<slug:thing1>/<int:thing2>/', views.DjappView.as_view()),
    path('', views.DjappView.as_view())
]
