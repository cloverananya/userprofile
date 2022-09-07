from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegistrationSerializers, ProfileSerializers
from .models import User, Profile
from rest_framework import status
from django.http import Http404
from .permissions import IsOwnerOrReadOnly, IsOwner
from rest_framework import permissions
# from django.conf import settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.hashers import make_password


# user = settings.AUTH_USER_MODEL


class UserRegistrationView(APIView):
    serializer_class = RegistrationSerializers

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializers(data=request.data)

        if serializer.is_valid():
            # serializer.validated_data
            print(serializer.validated_data)
            email = serializer.validated_data['email']
            name = serializer.validated_data['name']
            password = make_password(serializer.validated_data['password'])
            gender = serializer.validated_data['gender']
            number = serializer.validated_data['number']
            fav_actor = serializer.validated_data['fav_actor']
            date_of_birth = serializer.validated_data['date_of_birth']
            image = serializer.validated_data['image']
            user = User.objects.create(email=email, name=name, password=password)

            Profile.objects.create(user=user, gender=gender, number=number, fav_actor=fav_actor,
                                   date_of_birth=date_of_birth, image=image)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    serializer_class = RegistrationSerializers

    def get(self, *args, **kwargs):
        users = Profile.objects.all()
        serializer = ProfileSerializers(users, many=True)
        return Response(serializer.data)


class ProfileDetailList(APIView):
    serializer_class = ProfileSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        users = self.get_object(pk)
        serializer = ProfileSerializers(users)
        return Response(serializer.data)

    def put(self, request, pk):
        users = self.get_object(pk)
        serializer = ProfileSerializers(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        users = self.get_object(pk)
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
