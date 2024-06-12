from django.contrib import admin
from .models import Artist, Concert, Festival


admin.site.register(Artist)
admin.site.register(Concert)
admin.site.register(Festival)

