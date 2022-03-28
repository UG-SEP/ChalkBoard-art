from django.contrib import admin
from .models import Categories,Food, Items, Order

class OrderAdmin(admin.ModelAdmin):
    search_fields=('name','address','phone','razorpay_payment_id')
    list_display=['name','phone','address']
    list_filter=['name','phone','address','razorpay_payment_id']

admin.site.register(Categories)
admin.site.register(Food)
admin.site.register(Items)
admin.site.register(Order,OrderAdmin)

