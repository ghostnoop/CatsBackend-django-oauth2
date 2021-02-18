from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from catsapi import models, views
from catsapi.models import User, Cat


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class LoginUserSerializer(serializers.ModelSerializer):
    state_user = None

    def create(self, validated_data):
        user = User.objects.get(email=validated_data['email'])
        checked = user.check_password(validated_data['password'])
        if checked:
            self.state_user = user
            return user
        else:
            return None

    class Meta:
        model = User
        fields = ('email', 'password')


class CatSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(read_only=True, source='user')
    name = serializers.CharField(required=True, max_length=100)
    birth = serializers.DateField(required=False)
    weight = serializers.FloatField(required=False)
    breed = serializers.CharField(max_length=100, allow_blank=True, required=False)
    photo = serializers.ImageField(required=False, default="")

    def create(self, validated_data):
        for user in User.objects.all():
            print(user.id, user.username)
        print(self.initial_data)
        return Cat.objects.create(owner_id_id=self.initial_data['owner_id'],
                                  birth=validated_data.get('birth'),
                                  name=validated_data.get('name'), weight=validated_data.get('weight'),
                                  breed=validated_data.get("breed"), photo=validated_data.get('photo'))

    def update(self, instance, validated_data):
        instance.birth = validated_data.get('birth', instance.birth)
        instance.name = validated_data.get('name', instance.name)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.breed = validated_data.get('breed', instance.breed)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance


    class Meta:
        model = Cat
        fields = ('id', 'birth.year', 'name', 'weight', 'breed', 'photo')
