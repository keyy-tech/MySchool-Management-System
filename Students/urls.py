from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.student_create, name="student_create"),
    path("update/<int:pk>/", views.student_update, name="student_update"),
    path("read/", views.student_list, name="student_list"),
    path("profile/<int:pk>", views.student_detail, name="student_profile"),
    path("delete/<int:pk>", views.student_delete, name="student_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
