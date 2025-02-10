# from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers
from rest_framework.views import APIView

from django.contrib.auth.models import User
from django.shortcuts import redirect

from rest_framework.response import Response
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


# for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Login logout
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView


#change password
from rest_framework import status
from rest_framework.permissions import IsAuthenticated 
from rest_framework import generics

# Create your views here.
class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset=models.ImageUpload.objects.all()
    serializer_class=serializers.ImageUploadSerializers


class SignupAPIView(APIView):
    serializer_class = serializers.SignUpSerializer    

    def post(self,request):
        serializer=self.serializer_class(data=request.data) #like form
        
        if serializer.is_valid():
            user=serializer.save()
            print(user)
            token=default_token_generator.make_token(user)
            print("token ",token)
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            print("uid ",uid)
            confirm_link=f"http://127.0.0.1:8000/accounts/active/{uid}/{token}"
            email_subject="Confirm Your Email"
            email_body=render_to_string('confirm_email.html',{'confirm_link':confirm_link})
            email=EmailMultiAlternatives(email_subject, '',to=[user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()
            return Response("Check your mail for confirmation")
        return Response(serializer.errors)
    

class UserLoginApiView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data = self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username= username, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request, user)
                return Response({'token' : token.key, 'user_id' : user.id})
            else:
                return Response({'error' : "Invalid Credential"})
        return Response(serializer.errors) 



def activate(request, uid64, token):
    try: # Error handling kortechi. uid, user nao thakte pare tar mane sekhan theke error asar somvabona ache
    # sejonne code ke try er moddhe rakhlam
        uid = urlsafe_base64_decode(uid64).decode() # encode kora sei uid ke decode kortechi
        user = User._default_manager.get(pk=uid) # decode er por je uid pelam seta kon 
        # user er seta janar jonne ei code ta
    except(User.DoesNotExist):
        user = None 
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('signup')


# class UserLogOutView(APIView):
#     def get(self, request):
#         request.user.auth_token.delete()
#         logout(request)
#         return redirect('login')

class UserLogOutView(APIView):
    def get(self, request):        
        if hasattr(request.user, 'auth_token'):
            request.user.auth_token.delete()
        
        logout(request)  # Logout the user from session
        return redirect('login')


# class Logout(GenericAPIView):
#     def get(self, request, format=None):
#         # simply delete the token to force a login
#         if request.is_authenticated():
#             request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)
  
  
  
class ChangePasswordView(generics.UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = serializers.ChangePasswordSerializer
        model = User
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    # 'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    # 'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
          
