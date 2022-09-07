from rest_framework import serializers
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


#
#
# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ('user', 'gender', 'number', 'fav_actor', 'date_of_birth', 'image')
#
#
# class UserSerializer(serializers.ModelSerializer):
#     profiles = ProfileSerializer(many=True)
#
#     class Meta:
#         model = User
#         fields = ('email', 'profiles', 'name', 'is_staff', 'is_active',)
#
#         #
#         # def create(self, validated_data):
#         #     user = User.objects.create_user(
#         #         email=validated_data['email'],
#         #         name=validated_data['name'],
#         #     )
#         #     password = self.validated_data['password']
#         #     user.set_password(password)
#         #     user.save()
#         #
#         #     # create_profile
#         #     profile_data = validated_data.pop('profile')
#         #     for p in user:
#         #         for user in profile_data:
#         #             Profile.objects.create(
#         #                 user=user, **p)
#         #         # gender=profile_data['gender'],
#         #         # number=profile_data['number'],
#         #         # fav_actor=profile_data['fav_actor'],
#         #         # date_of_birth=profile_data['date_of_birth'],
#         #         # image=profile_data['image'],
#         #         # )
#         #         return user
#
#         # def create(self, validated_data):
#         #     profile_data = validated_data.pop('profile')
#         #     user = User.objects.create(**validated_data)
#         #     Profile.objects.create(user=user, **profile_data)
#         #     return user
#         # #
#         # def to_representation(self, instance):
#         #     representation = super(UserSerializer).to_representation()
#         #     representation['profile'] = ProfileSerializer(instance.profile_set.all(), many=True).data
#         #     return representation
#         # def create(self, validated_data):
#         #     profile_data = validated_data.pop('profile')
#         #     user = User.objects.create(**validated_data)
#         #     for user in profile_data:
#         #         User.objects.create(user=user, **user)
#         #     return user
#         def create(self, validated_data):
#             profiles_data = validated_data.pop('profiles')
#             user = User.objects.create(**validated_data)
#             for profile_data in profiles_data:
#                 Profile.objects.create(user=user, **profile_data)
#             return user
GENDER = (
    ('Male', 'Boy'),
    ('Female', 'Girl'),
)


class RegistrationSerializers(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(max_length=250)
    name = serializers.CharField(max_length=250)
    gender = serializers.ChoiceField(choices=GENDER)
    number = serializers.IntegerField()
    fav_actor = serializers.CharField(max_length=250)
    date_of_birth = serializers.DateField()
    image = serializers.ImageField()


class ProfileSerializers(serializers.ModelSerializer):
    email = serializers.PrimaryKeyRelatedField(source='user.email', read_only=True)
    user = serializers.PrimaryKeyRelatedField(source='user.name', read_only=True)
    class Meta:
        model = Profile
        fields = ('user', 'gender', 'number', 'fav_actor', 'date_of_birth', 'image', 'email')

    # def save(self, **kwargs):
    #     pass

