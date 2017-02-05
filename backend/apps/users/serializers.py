from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
   
    document = serializers.FileField(max_length=None,use_url=True)

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'email', 'last_login',
            'is_active', 'document', 'date_joined', 'last_updated'
        )
