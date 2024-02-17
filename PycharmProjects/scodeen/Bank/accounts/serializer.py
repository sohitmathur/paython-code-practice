from rest_framework import serializers
from . models import AccountDetails

class AccountDetailsSer(serializers.ModelSerializer):
    class Meta:
        model=AccountDetails
        fields  = "__all__"


class AccountDetailsSerForNameAndBal(serializers.ModelSerializer):
    class Meta:
        model=AccountDetails
        fields=('account_name','bal')