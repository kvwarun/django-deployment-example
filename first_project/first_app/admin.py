from django.contrib import admin
from first_app.models import AccessRecord, Topic, Webpage


admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
