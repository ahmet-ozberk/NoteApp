from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from django.contrib import admin
from NoteApi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/notes/",views.ListNoteAPIView.as_view(),name="note_list"),
    path("api/notes/create/", views.CreateNoteAPIView.as_view(),name="note_create"),
    path("api/notes/update/<int:pk>/",views.UpdateNoteAPIView.as_view(),name="note_update"),
    path("api/notes/delete/<int:pk>/",views.DeleteNoteAPIView.as_view(),name="note_delete")
]
