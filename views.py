from django.shortcuts import render

from rest_framework import generics
from .models import CustomUser
from .serializers import UserRegistrationSerializer
from .serializers import CustomUserSerializer 

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

#<----------------------------Generate Token---------------------------------------->


class GenerateTokenView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Both username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid username or password."}, status=status.HTTP_401_UNAUTHORIZED)


#<------------------------------User Registration------------------------------------>

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer


#<------------------------------Store Data------------------------------------------>


class StoreDataView(APIView):
    #permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "message": "Data stored successfully."})
        else:
            return Response(serializer.errors, status=400)
        

#<------------------------------Retrieve Data---------------------------------------->


class RetrieveDataView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, id, format=None):
        try:
            user = CustomUser.objects.get(id=id)  # Fetch user data from the database using id
            serializer = CustomUserSerializer(user)  # Serialize the fetched user data
            return Response({"status": "success", "data": serializer.data})
        except CustomUser.DoesNotExist:
            return Response({"status": "error", "message": "User not found."}, status=404)

        

#<------------------------------Update Data------------------------------------------>



class UpdateDataView(APIView):
    #permission_classes = [IsAuthenticated]

    def put(self, request, id, format=None):
        new_age = request.data.get('new_age')      # Retrieve the new age from the request data
        new_gender =request.data.get('new_gender')  

        try:
            user = CustomUser.objects.get(id=id)  # Fetch user data from the database using id
        except CustomUser.DoesNotExist:
            return Response({"status": "error", "message": f"User with id '{id}' not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Update new age
        print(f"Updating data for user with id: {id}")
        print(f"Current age: {user.age}, New age: {new_age}")

        user.age = new_age
        user.save()

        #Update new gender
        print(f"Updating data for user with id: {id}")
        print(f"Current gender: {user.gender}, New gender: {new_gender}")

        user.gender = new_gender
        user.save()

        print("User data updated successfully")

        # Create a serializer instance to get the serialized data
        serializer = CustomUserSerializer(user)
        return Response({
            "status": "success",
            "message": "Data updated successfully.",
            "data": serializer.data
        })




#<------------------------------Delete Data by id------------------------------------->


class DeleteDataView(APIView):
    def delete(self, request, id, format=None):
        try:
            user = CustomUser.objects.get(id=id)
            user.delete()
            return Response({"status": "success", "message": "User deleted successfully."})
        except CustomUser.DoesNotExist:
            return Response({"status": "error", "message": "User not found."}, status=status.HTTP_404_NOT_FOUND)


