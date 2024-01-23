from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseForbidden
from rest_framework.response import Response    
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from datetime import datetime
from .serilaizers import ItemsSerializers, LoginSerializer, UserCreationSerilaizer, UserSerializer
from .models import Items, Year, Month, Purchase, CustomUser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class Userlogin(CreateAPIView):

    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = self.request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")
        user = authenticate(request, email= email,password= password)
        if not user:
            try:
                instance = CustomUser.objects.get(email__exact = email)
                if instance:
                    return HttpResponse("Password is incorrect....")
            except Exception as e:
                print(e)
                return HttpResponseBadRequest("Could not login User")
        login(request,user)
        return Response(UserSerializer(request.user).data)
    
    
@method_decorator(csrf_exempt, name='dispatch')  
class CreateNewUser(CreateAPIView):

    serializer_class = UserCreationSerilaizer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        email = self.request.data["email"]
        password = self.request.data["password"]
        username = self.request.data["username"]
        instance = CustomUser.objects.create(username=username, email=email)
        instance.set_password(password)
        instance.save()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@method_decorator(csrf_exempt, name='dispatch') 
class RegisterPurchaseItems(CreateAPIView):

    serializer_class = ItemsSerializers
    permission_classes = (AllowAny,)
    pagination_class = None


    def post(self, request, *args, **kwargs):
        print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
        input_data = self.request.data
        print(input_data)
        pass
        # today_date = datetime.now()
        # current_year_full = today_date.strftime("%Y")
        # current_full_month = today_date.strftime('%B')
        # print(current_full_month," ====> " ,current_year_full)
        # instance, created = Year.objects.get_or_create(year__exact = str(current_year_full))
        # print(instance," Bool :", created)
        # month_instance, is_created = Month.objects.get_or_create(month__exact=str(current_full_month))
        # if is_created:
        #     instance.months.add(month_instance)
        # purchase_object = Purchase.objects.create(user=self.request.user.id, )
        # total_amount = 0
        # for item in input_data:
        #     purchase_object.items.add(Items.objects.create(name=item.name, quantity=item.quantity, amount=item.amount))
        #     total_amount+=item.amount
        # print(purchase_object)
        # print([x.name for x in purchase_object.items])
        # purchase_object.amount_spent = total_amount
        # purchase_object.save()

        return HttpResponse(status=status.HTTP_201_CREATED)
    
