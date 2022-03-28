from django.urls import path

from Home.views import Add_item, Customer_Orders, Home, Menu, Cart, My_Orders, Order_Completed, Order_Food, Order_Shipped, Remove_Item, Success, Summary

urlpatterns = [
    path('',Home,name="home"),
    path('menu/',Menu,name="menu"),
    path('cart/',Cart,name="cart"),
    path('add-item/',Add_item,name="add_item"),
    path('remove-item/',Remove_Item,name="remove-item"),
    path('order/',Order_Food,name="order"),
    path('summary/',Summary,name="summary"),
    path('success/',Success,name="success"),
    path('my-orders/',My_Orders,name="my-order"),
    path('customer-orders/',Customer_Orders,name="customer-orders"),
    path('order-shipped/',Order_Shipped,name="order-shipped"),
    path('order-received/',Order_Completed,name="order-received")
]
