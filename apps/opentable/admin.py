from django.contrib import admin
from models import Restaurant, Reservation

class RestaurantAdmin(admin.ModelAdmin):
    pass

class ReservationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Reservation, ReservationAdmin)

