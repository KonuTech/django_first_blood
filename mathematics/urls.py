from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello),
    path("hello/", views.hello),
    path("hello/<name>/", views.hello),
    path("mathematics/<operation>/<int:a>/<int:b>", views.calculator)  # to wymaga utworzenia funkcji calculator
]
