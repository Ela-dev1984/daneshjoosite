from django.urls import path
from .views import (
    home,
    add_student,
    delete_student,
    sort_student,
    profile_student,
    show_student,
)

urlpatterns = [
    path("", home, name="home"),
    path("add/", add_student, name="add"),
    path("delete/<int:id>/", delete_student, name="delete"),
    path("sort/", sort_student, name="sort"),
    path("show/", show_student, name="show"),
    path("profile/<int:id>/", profile_student, name="profile"),
]
