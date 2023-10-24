from django.contrib import admin

from .models import (
    Availability,
    CustomUser,
    Mentee,
    Mentor,
    NotificationSettings,
    Session
)

admin.site.register(CustomUser)
admin.site.register(Mentor)
admin.site.register(Mentee)
admin.site.register(Session)
admin.site.register(Availability)
admin.site.register(NotificationSettings)
