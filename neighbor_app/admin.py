from django.contrib import admin

from .models import Profile,NeighborHood,Post,Business

# Register your models here.

admin.site.register(Profile)
admin.site.register(NeighborHood)
admin.site.register(Post)
admin.site.register(Business)
