from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'uuid',
            'first_name',
            'last_name',
            'email',
            'username',
        ]

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        self.request_user = kwargs.pop('request_user', None)

        if self.instance == self.request_user:
            pass
        else:
            del self.fields['last_name']
            del self.fields['email']


