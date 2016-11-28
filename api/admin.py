from django.contrib import admin
from .models import *


class ShopInline(admin.StackedInline):
    model = Shop
    extra = 0
    suit_classes = 'suit-tab suit-tab-general'


class StructuresAdmin(admin.ModelAdmin):
    inlines = (ShopInline,)
    fieldsets = [
        ('Основная информация', {
            'classes': ('suit-tab', 'suit-tab-main',),
            'fields': [
                'address','index'
            ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': []}),

    ]
    suit_form_tabs = (('main', 'Основные'),
                      ('general', 'Магазины'),
                      )

class AdvertisementsInline(admin.StackedInline):
    model = Advertisements
    extra = 0
    suit_classes = 'suit-tab suit-tab-general'


class AdvertisementsAdmin(admin.ModelAdmin):
    inlines = (AdvertisementsInline,)
    fieldsets = [
        ('Основная информация', {
            'classes': ('suit-tab', 'suit-tab-main',),
            'fields': [
                'name',
            ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': []}),

    ]
    suit_form_tabs = (('main', 'Основные'),
                      ('general', 'Реклама'),
                      )

admin.site.register(Events)
admin.site.register(Structures,StructuresAdmin )
admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(Advertisements)
admin.site.register(PlayListAdvertisements, AdvertisementsAdmin)
admin.site.register(Terminal)
