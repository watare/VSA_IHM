from django.contrib import admin

from listings.models import Band, Listing


class BandAdmin(admin.ModelAdmin):
    list_display = ('name','year_formed','genre')

class ListAdmin(admin.ModelAdmin):
    list_display = ('name','band')
admin.site.register(Band,BandAdmin)
admin.site.register(Listing,ListAdmin)