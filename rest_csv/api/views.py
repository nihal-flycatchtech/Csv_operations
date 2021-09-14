from django.shortcuts import render
from rest_framework import generics, viewsets
import io, csv, pandas as pd
from rest_framework.response import Response
from rest_csv.models import File
from rest_csv.api.serializers import FileUploadSerializer, CsvOperationSerializer
from rest_framework import status
from django.http import HttpResponse


class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for index, row in reader.iterrows():
            new_file = File(
                id=row['id'],
                firstname=row["firstname"],
                lastname=row['lastname'],
                email=row["email"],
                profession=row["profession"]
            )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)


class GetApiViewset(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = CsvOperationSerializer


class UpdateApi(generics.RetrieveUpdateAPIView):
    queryset = File.objects.all()
    serializer_class = CsvOperationSerializer


class DeleteApi(generics.DestroyAPIView):
    queryset = File.objects.all()
    serializer_class = CsvOperationSerializer


def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['id', 'firstname', 'lastname', 'email', 'profession'])

    users = File.objects.all().values_list('id', 'firstname', 'lastname', 'email', 'profession')
    for user in users:
        writer.writerow(user)

    return response
