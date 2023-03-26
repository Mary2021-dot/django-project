from django.contrib import admin
from .models import Child,Donor,ContactMessage,Event

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age', 'gender', 'admission_date')
    list_filter = ('gender', 'admission_date')
    search_fields = ('full_name',)



admin.site.register(Donor)
admin.site.register(ContactMessage)
admin.site.register(Event)


