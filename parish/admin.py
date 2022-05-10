from django.contrib import admin

from parish.models import (
    Committee,
    Community, 
    Contribution, 
    Member, 
    Priest, 
    SubParish
)

# Register your models here.

admin.site.register(Priest)
admin.site.register(Community)
admin.site.register(SubParish)
admin.site.register(Member)
admin.site.register(Contribution)
admin.site.register(Committee)