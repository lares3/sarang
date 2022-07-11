from operator import truediv
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .helpers import send_otp_to_phone
from .models import User

@api_view(['post'])
def send_otp(request):
    data=request.data

    if data.get('phone_number') is None:
        return Response({'status':400,
        'message':'key_phone_number_is_reqired'})
    
    if data.get('password') is None:
        return Response({'status':400,
        'message':'key_password_is_reqired'})

    user=User.objects.create(
        phone_number=data.get('phone_number'),
        otp=send_otp_to_phone(data.get('phone_number')))
    user.set_password=data.get('set_password')
    user.save()

    return Response({'status':200,'message':'otp sent'})
    

@api_view(['post'])
def varify_otp(request):
    data=request.data

    if data.get('phone_number') is None:
        return Response({'status':400,
        'message':'key_phone_number_is_reqired'})
    
    if data.get('otp') is None:
        return Response({'status':400,
        'message':'key_otp_is_reqired'})

    try:
        user_obj=User.objects.get(phone_number=data.get('phone_number'))
    
    except Exception as e:
        return Response({'status':400,
        'message':'invalid phone'})

    if user_obj.otp==data.get('otp'):
        user_obj.is_phone_varified=True
        user_obj.save()
        return Response({'status':200,
        'message':'otp matched'})

    return Response({'status':400,
        'message':'invalid otp'})
