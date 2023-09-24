from django.shortcuts import render, redirect
from car_part_sale.models import *
from . serializers import *
from rest_framework.decorators import api_view , authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.fields import CurrentUserDefault
import uuid
import random


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def apiOverview(request):
    api_urls = {
        'INFO': "Please refer the PDF document. ",
        'Users': 'api/users/',
        'Categories': 'api/categories/',
        'Parts': 'api/parts/',
        'Cart': 'api/cart/',
        'Orders': 'api/orders',
        'Token': 'api/token'

    }

    return Response(api_urls)



### List All users
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def userList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)



### Register New User
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def userCreate(request):
    serializer = UserCreateSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = "Successfully registerd a new user"
        data['email'] = user.email
        data['username'] = user.username

    else:
         data = serializer.errors
    
    return Response(data)



### List Categories
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def categoryList(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)



@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def catDetail(request,pk):
    categoeries = Category.objects.get(id = pk)
    serializer = CategoryAllSerializer(categoeries,many=False)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def catCreate(request):
    serializer = CategoryAllSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def catUpdate(request,pk):
    categoery = Category.objects.get(id = pk)
    serializer = CategoryAllSerializer(instance=categoery, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def catDelete(request,pk):
    categoery = Category.objects.get(id = pk)
    categoery.delete()

    return Response("Item successfully deleted")


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def catCreate(request):
    serializer = CategoryAllSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


### List Parts
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def partList(request):
    part = Part.objects.all()
    serializer = PartSerializer(part, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def partDetails(request, pk):
    part = Part.objects.get(id = pk)
    serializer = PartAllSerializer(part, many=False)
    return Response(serializer.data)



### List Cart
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def cartList(request):
    cart = Cart.objects.filter(user = request.user)
    serializer = CartSerializer(cart, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def cartCreate(request):
    print(request.data['part'])
    part_id = int(request.data['part'])
    part_check = Part.objects.get(id=part_id)
    if(part_check):
        if(Cart.objects.filter(user=request.user.id, part=part_id)):
            return Response({'status':"Product Already in Cart"})
        else:
            part_qty = int(request.data['part_qty'])

            if part_check.stock >= part_qty:
                Cart.objects.create(user=request.user, part=part_check, part_qty=part_qty)
                return redirect(cartList)
            else:
                return Response({'status':"No Stocks"})
    else:
        return Response({'status':"Invalid Product"})
    


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def cartDelete(request,pk):
    cart = Cart.objects.filter(user = request.user,id = pk).first()
    if cart:
        cart.delete()

        return Response({'status':"Item successfully deleted"})
    else:
        return Response({'status':"you don't have permision to delete it"})


##order_view
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def orderList(request):
    order = Order.objects.filter(user = request.user)
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)

##orderView single
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def orderView(request,pk):
    order = Order.objects.get(id = pk)
    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)

##order_status_update
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def orderUpdate(request,pk):
    order = Order.objects.get(id = pk)
    # serializer = OrderStatusSerializer(instance=order, data = request.data)
    # if serializer.is_valid():
    #     serializer.save()
    # return Response(serializer.data)

    if order.status == "Pending" or order.status == "Out for Shipping":
        order.status = "Out for Shipping"
        order.save()

        return Response({'status':"Order Shipped Successfully"})

    return Response({'status':"Order still in Pending state"})


##order_status_update_delivered
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def orderDelivered(request,pk):
    order = Order.objects.get(id = pk)
    if order.status == "Out for Shipping" or order.status == "Completed":
        order.status = "Completed"
        order.save()
        return Response({'status':"Order Delivered Successfully"})

    
    
    return Response({'status':"Order still in Out for Shipping state"})



##order_create
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def orderCreate(request):
    name = (request.data['name'])
    email = (request.data['email'])
    address = (request.data['address'])
    payment_mode = (request.data['payment_mode'])

    cart = Cart.objects.filter(user=request.user)
    cart_total_price = 0
    for item in cart:
        cart_total_price = cart_total_price + item.part.price * item.part_qty

    status = "Pending"
    
    tracking_no = str(uuid.uuid4()).split('-')[-1] + "_" +str(random.randint(1111111,9999999))
    delivery_date = request.data['delivery_date']
    if cart:
        order = Order.objects.create(user=request.user ,name=name,email=email,
                            address=address,total_price=cart_total_price,
                            payment_mode=payment_mode,status=status,
                            tracking_no=tracking_no,delivery_date=delivery_date
                            )
        
        order_items = Cart.objects.filter(user=request.user)
        for item in order_items:
            OrderItem.objects.create(order=order,
                                    part=item.part,
                                    price=item.part.price,
                                    quantity=item.part_qty 
                                    )
            
            # reduce stocks
            orderedparts = Part.objects.filter(id=item.part.id).first()
            orderedparts.stock = orderedparts.stock - item.part_qty
            orderedparts.save()

        # Clear Cart
        Cart.objects.filter(user=request.user).delete()



        return Response({'status':"Order Created Successfully"})

    else:
        return Response({'status':"Already Created, Empty cart!"})
    