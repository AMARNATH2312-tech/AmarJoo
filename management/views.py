from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseForbidden
from rest_framework.response import Response    
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from datetime import datetime
from .serilaizers import ItemsSerializers, LoginSerializer, UserCreationSerilaizer, UserSerializer, PurchasedItemSerializers
from .models import Items, Year, Month, Purchase, CustomUser, Amount, ItemInfo
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pexels_api import API
from veg_management.settings import PEXELS_API_KEY
import tqdm
import json



# Create your views here.   

@method_decorator(csrf_exempt, name='dispatch')
class Userlogin(CreateAPIView):

    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        print("Whether Am i hitting................")
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
        print("sign_in is calling")
        email = self.request.data["email"]
        password = self.request.data["password"]
        firstname = self.request.data["firstName"]
        lastname = self.request.data["lastName"]
        username = firstname+lastname
        instance = CustomUser.objects.create(first_name=firstname,last_name=lastname, username = username,email=email)
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
        input_data = self.request.data
        print(input_data)
        today_date = datetime.now()
        current_year_full = today_date.strftime("%Y")
        current_full_month = today_date.strftime('%B')
        print(current_full_month," ====> " ,current_year_full)
        try:
            instance = Year.objects.get(year__exact = str(current_year_full))
        except Exception as e:
            instance = Year.objects.create(year=str(current_year_full))
        print(instance)

        try:
            month_instance = Month.objects.get(month_name__exact = str(current_full_month))
        except Exception as e:
            month_instance = Month.objects.create(month_name=str(current_full_month), amount=Amount.objects.create())
            instance.months.add(month_instance)
        # purchase_object = Purchase.objects.create(user=self.request.user.id, )
        purchase_object = Purchase.objects.create(user=CustomUser.objects.get(id=22), amount_spent=0)
        total_amount = 0
        for item in input_data:
            print(item)
            try:
                item_info_instance = ItemInfo.objects.get(item_name = item["name"])
            except Exception as e:
                item_info_instance = ItemInfo.objects.create(item_name = item["name"])
                image_name, content = download_images(item["name"])
                item_info_instance.image.save(image_name, content=content)
                
            purchase_object.items.add(Items.objects.create(name=item_info_instance, quantity=item["quantity"], amount=item["amount"]))  
            total_amount+=item["amount"]
            
        purchase_object.amount_spent = total_amount
        purchase_object.save()
        month_instance.purchases.add(purchase_object)
        month_instance.money_spent = month_instance.money_spent+total_amount
        month_instance.save()

        return HttpResponse(status=status.HTTP_201_CREATED)
    

@method_decorator(csrf_exempt, name='dispatch')
class FetchGroceries(ListAPIView):
    # authentication_classes = None
    permission_classes = (AllowAny,)
    def get(self, request, *args, **kwargs):
        month =  kwargs.get("month")
        print(month)
        try:
            purchases = Month.objects.get(month_name=month).purchases.all()
            print(purchases)
            serailized_data = PurchasedItemSerializers(purchases, many=True)
            return Response(serailized_data.data)
        except Exception as e:
            return Response("")
        

class ParticularPurchaseItems(ListAPIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        purchase_id =  kwargs.get("id")
        try:
            queryset = Purchase.objects.get(id=purchase_id).items.all()
            serialized_data = ItemsSerializers(queryset, many=True).data
            return Response(serialized_data)
        except Exception as e:
            return Response("")
        
        
def create_file_name(query, file_name):
    if "jpeg" in file_name:
        return f"{query}.jpeg"
    if "jpg" in file_name:
        return f"{query}.jpg"


def download_images(item_name):
    api = API(PEXELS_API_KEY)
    PAGE_LIMIT = 10
    RESULTS_PER_PAGE = 1
    query = item_name 

    photos_dict = {}
    page = 1
    counter = 0

    # Step 1: Getting urls and meta information
    while page < PAGE_LIMIT:
        api.search(query, page=page, results_per_page=RESULTS_PER_PAGE)
        photos = api.get_entries()
        for photo in tqdm.tqdm(photos):
            photos_dict[photo.id] = vars(photo)['_Photo__photo']
            counter += 1
            if not api.has_next_page:
                break
            page += 1

    print(f"Finishing at page: {page}")
    print(f"Images were processed: {counter}")
    start_download(photos_dict, query)


def start_download(photos_dict, query):
    PATH = r'C:\Users\Amarnath V\Vegetable_management\veg_management\media\veg_images'
    RESOLUTION = 'original'

    if photos_dict:
        os.makedirs(PATH, exist_ok=True)
        
        # Saving dict
        # with open(os.path.join(PATH, f'{query}.json'), 'w') as fout:
        #     json.dump(photos_dict, fout)
        
        for val in tqdm.tqdm(photos_dict.values()):
            url = val['src'][RESOLUTION]
            fname = os.path.basename(val['src']['original'])
            image_path = os.path.join(PATH, create_file_name(query, fname))
            if not os.path.isfile(image_path):
                response = requests.get(url, stream=True)
                if response.status_code == 200:
                    content = response.content
                    with open(image_path, 'wb') as outfile:
                        outfile.write(content)
                    return image_path, content
                # with open(image_path, 'wb') as outfile:
                #     outfile.write(response.content)
                #     return image_path, response.content 
            else:
                # ignore if already downloaded
                print(f"File {image_path} exists")


