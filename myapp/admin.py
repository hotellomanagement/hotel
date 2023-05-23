from django.contrib import admin
from myapp.models import*

# Register your models here.
@admin.register(contact)
class contactadmin(admin.ModelAdmin):
    list_display=('firstname','email','subject','message')

@admin.register(product)
class productadmin(admin.ModelAdmin):
     pass

@admin.register(blog)
class blogadmin(admin.ModelAdmin):
     pass

@admin.register(FAQ)
class FAQadmin(admin.ModelAdmin):
     pass

@admin.register(Room)
class Roomadmin(admin.ModelAdmin):
     pass



@admin.register(booking)
class bookingadmin(admin.ModelAdmin):
  list_display=('firstname','lastname','checkout','checkin','phonenumber','emailid','roomtype','noofadults','noofchildren','userid','status',)

@admin.register(subscribe)
class subscribeadmin(admin.ModelAdmin):
     pass

@admin.register(Ordernow)
class orderadmin(admin.ModelAdmin):
    pass