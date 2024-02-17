from django.shortcuts import render
from .models import AccountDetails
from. serializer import AccountDetailsSer,AccountDetailsSerForNameAndBal
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

class AccountDetailsView(APIView):
    def get(self,r,pk):

     try:
        accountobj = AccountDetails.objects.get(pk=pk)
        ser = AccountDetailsSerForNameAndBal(accountobj)
        return Response(ser.data,status=status.HTTP_200_OK)
     except ObjectDoesNotExist:
         return Response({"messege":"Given ID: {} is not present".format(pk)},status=status.HTTP_204_NO_CONTENT)
    def post(self,r):
        ser=AccountDetailsSer(data=r.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)

class AccountDetailsupdateDelete(APIView):
    def put(self,r,pk):
        obj = AccountDetails.objects.get(pk=pk)
        serobj= AccountDetailsSer(obj,data=r.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_202_ACCEPTED)

    def delete(self,r,pk):
        obj = AccountDetails.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AccountDetailsBlank(APIView):
    def get(self,r):
        return Response({'messege':'ID should be present'},status=status.HTTP_400_BAD_REQUEST)
