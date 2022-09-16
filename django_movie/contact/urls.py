from django.urls import path
from .views import ContactView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", ContactView.as_view(), name="contact"),

]
