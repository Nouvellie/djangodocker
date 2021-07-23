from .models import VerifiedAccount
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class VerifiedAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifiedAccount
        fields = (
            'ver_acc_id',
            'ver_acc_verified',
            'id'
        )


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        print(attrs)
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if user is not None:
            if user.is_active:
                data = super().validate(attrs)
                refresh = self.get_token(self.user)
                refresh['username'] = self.user.username
                try:
                    obj = VerifiedAccount.objects.get(id=self.user)
                    refresh['verified'] = obj.ver_acc_verified
                    data['username'] = self.user.username
                    data['verified'] = obj.ver_acc_verified
                    
                except Exception as e:
                    raise serializers.ValidationError('Something Wrong!')
                return data
            else:
                raise serializers.ValidationError('Account is Blocked.')
        else:
            raise serializers.ValidationError('Incorrect username and password combination!')