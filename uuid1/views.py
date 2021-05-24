from django.shortcuts import render
from rest_framework import generics, views
from rest_framework import status
from rest_framework.response import Response
from .models import Uuid
from .utils import get_uuid
# Create your views here.



class HomeView(views.APIView):
    """
    returns all generated lists of uuid along side their timestamp reversely
    """

    def get(self, request):
        lists = []
        _id = get_uuid()
        user = Uuid.objects.create(uuids=_id)
        user.save()
        my_user = Uuid.objects.all().order_by("-created")
        for i in my_user:
            user = {
                str(i.created) : str(i.uuids)
            }
            lists.append(user)
        return Response(lists, status=status.HTTP_200_OK)
