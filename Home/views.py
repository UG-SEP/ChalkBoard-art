from django.shortcuts import redirect, render

from User.views import deco_auth
from .models import Food, Items, Order
import razorpay
from django.views.decorators.csrf import csrf_exempt

def Home(request):
    if request.method == "POST":
        pass
    popular_food=Food.objects.filter(is_popular=True)
    special_food=Food.objects.get(is_special=True)
    return render(request,'Home/index.html',{'popular':popular_food,'special':special_food})

def Menu(request):
    main_course,sandwich,salads,maggi=[],[],[],[]
    dishes=Food.objects.all()
    for dish in dishes:
        if dish.category.name == "Main Course":
            main_course.append(dish)
        elif dish.category.name == "Sandwich":
            sandwich.append(dish)
        elif dish.category.name == "Salads":
            salads.append(dish)
        else:
            maggi.append(dish)
    return render(request,'Home/menu.html',{'main_course':main_course,'sandwich':sandwich,'salads':salads,
    'maggi':maggi})

@deco_auth
def Cart(request):
    items=Items.objects.filter(user=request.user)
    cost=Cost(items)
    return render(request,'Home/cart.html',{'cart':items,'cost':cost,'size':len(items),'iscart':'yes'})

@deco_auth
def Add_item(request):
    id=request.GET.get('id')
    food=Food.objects.get(id=id)
    cart=Items.objects.create(food=food,user=request.user)
    cart.save()
    return redirect('home')

def Cost(items):
    total=0
    for item in items:
        total+=item.food.price
    return total

@deco_auth
def Remove_Item(request):
    Items.objects.filter(id=request.GET.get('id')).delete()
    return redirect('cart')

def Order_Food(request):
    id=request.GET.get('id')
    food=Food.objects.get(id=id)
    return render(request,'Home/order.html',{'food':food,'iscart':'no'})

@deco_auth
def Summary(request):  
    if request.method == "POST":
        price=int(request.POST.get('price'))
        price*=100
        iscart=request.POST.get('iscart')
        if iscart == "no":
            id=int(request.POST.get('id'))
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        name=request.POST.get('name')
        client=razorpay.Client(auth=("rzp_test_LvlW8rpW4ehTCe","NavgZ407NBWMIDqz0fwYFQM0"))
        payment = client.order.create({'amount':price,'currency':'INR','payment_capture':'1'})
        print(payment)
        order= Order.objects.create(user=request.user,address=address,name=name,phone=phone,razorpay_payment_id=payment['id'])
        if iscart == "yes":
            cart=Items.objects.filter(user=request.user)
            for item in cart:
                order.dish.add(item.food)
        else:
            food=Food.objects.get(id=id)
            print(food)
            order.dish.add(food)
        if request.POST.get('later'):
            order.pay_on_delivery=True
        order.save()
        if request.POST.get('later'):
            order.paid=True
            order.save()
            return redirect('success')
        else:
            return render(request,"Home/summary.html",{'payment': payment,'name':name,'phone':phone,'email':request.user.email})
    price=request.GET.get('price')
    id=request.GET.get('id')
    return render(request,'Home/summary.html',{'price':price,'iscart':request.GET.get('iscart'),'id':id})

@csrf_exempt
def Success(request):
    if request.method == "POST":
        a =  (request.POST)
        order_id = ""
        for key , val in a.items():
            print(key,val)
            if key == "razorpay_order_id":
                order_id = val
                break
    
        user = Order.objects.filter(razorpay_payment_id = order_id).first()
        user.paid = True
        user.save()
        

    return redirect("home")

@deco_auth
def My_Orders(request):
    my_orders=Order.objects.filter(user=request.user)
    my_orders=[o for o in my_orders if o.paid==True]
    return render(request,'Home/my_orders.html',{'cart':my_orders})

@deco_auth
def Customer_Orders(request):
    if request.user.is_staff == True:
        filter=request.GET.get('filter')
        if filter=="pending":
            orders=Order.objects.filter(paid=True,order_received=False,shipped=False)
        elif filter=='shipped':
            orders=Order.objects.filter(shipped=True,order_received=False)
        elif filter=='completed':
            orders=Order.objects.filter(order_received=True)
        else:
            orders=Order.objects.all()
        orders=[o for o in orders if o.paid==True]
        return render(request,'Home/all_orders.html',{'cart':orders})
    else:
        redirect('home')

def Order_Shipped(request):
    id=request.GET.get('id')
    order=Order.objects.get(id=id)
    order.shipped=True
    order.save()
    return redirect('customer-orders')

def Order_Completed(request):
    id=request.GET.get('id')
    order=Order.objects.get(id=id)
    order.order_received=True
    order.save()
    return redirect('customer-orders')
