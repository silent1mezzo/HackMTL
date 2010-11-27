from django.contrib import admin
from models import Restaurant, Reservation, Theatre

class RestaurantAdmin(admin.ModelAdmin):
    pass

class ReservationAdmin(admin.ModelAdmin):
    pass

class TheatreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Theatre, TheatreAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Reservation, ReservationAdmin)

