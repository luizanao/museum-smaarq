from django.contrib import admin
from models import *
from django.contrib.contenttypes.generic import GenericTabularInline, generic_inlineformset_factory

ImagemGenericFormSet = generic_inlineformset_factory(Image, extra=1)


class ImagemInline(GenericTabularInline):
    model = Image
    extra = 1
    ct_field_name = 'content_type'
    id_field_name = 'object_id'

#####################################################

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('col_itemname', 'image_thumb')
    inlines = [ImagemInline]

#####################################################

admin.site.register(Collection, CollectionAdmin)