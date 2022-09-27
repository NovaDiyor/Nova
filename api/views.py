from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def post_table(request):
    table = Table.objects.filter(busyness=1)
    for i in table:
        return i.number
    number = input(int())
    if table.number == number:
        table.busyness = 2
        table.save()
    return Response(f'table {table.number} is successfully taken')


@api_view(['GET'])
def get_menu(request):
    product = Food.objects.filter(available=True)
    for i in product:
        data = {
            'name': i.name,
            'image': i.image.url,
            'bio': i.description,
            'price': i.price
        }
    return Response(data)


@api_view(['GET'])
def get_bill(request, pk):
    customer = Customer.objects.get(id=pk)
    order = Order.objects.filter(user_id=customer)
    total = 0
    for i in order:
        total = i.food.price * i.quantity
        i.food.quantity -= i.quantity
        i.food.save()
    data = {
        'quantity': order.quantity,
        'total': total,
        'seats': order.seats,
        'date': order.date,
        'time': order.time,
        'customer': customer.name
    }
    return Response(data)


@api_view(['POST'])
def get_table(request, pk):
    table = Table.objects.get(id=pk)
    if table.busyness == 1:
        return Response('table', table.number, 'is empty')
    elif table.busyness == 2:
        return Response('table', table.number, 'is taken')
