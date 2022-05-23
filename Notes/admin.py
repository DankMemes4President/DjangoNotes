from django.contrib import admin
from Notes.models import User, UserProfile, Note, Tag

# admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Note)
admin.site.register(Tag)
