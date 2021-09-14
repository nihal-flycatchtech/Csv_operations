from django.urls import path
from rest_csv.api.views import UploadFileView, GetApiViewset, UpdateApi, DeleteApi, export_users_csv
from rest_framework import routers


urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload-file'),
    path('List/', GetApiViewset.as_view(), name='List'),
    path('Update/<int:pk>', UpdateApi.as_view(), name='Update'),
    path('Delete/<int:pk>', DeleteApi.as_view(), name='Delete'),
    path('export/', export_users_csv, name='export'),

]
