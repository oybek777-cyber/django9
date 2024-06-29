from django.contrib import admin
from .models import News,Categroy,Contact
# Register your models here.
admin.site.register(Categroy)


@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display=('title','slug','state','create_date')
    search_fields=('title',)
    list_display_links=('slug','title',)
    list_filter=('title','state',)
    prepopulated_fields = {'slug': ('title',),}
    short_description = 'title'



class AdminContact(admin.ModelAdmin):
    pass
admin.site.register(Contact,AdminContact)