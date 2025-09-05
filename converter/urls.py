# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.upload_and_convert, name="upload_and_convert"),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.convert_images_to_pdf, name="convert_images_to_pdf"),
]