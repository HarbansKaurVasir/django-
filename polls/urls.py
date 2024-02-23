from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('members/', views.members, name='members'),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("userform/", views.userform),

    path("addstudent/", views.add_student ,name="addstudent"),
    path("edit/<int:id>", views.edit ,name="editdata"),
    path("delete/<int:id>", views.delete ,name="delete"),
]