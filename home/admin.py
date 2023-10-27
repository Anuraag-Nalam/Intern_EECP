from django.contrib import admin
from home.models import Newpatient
from home.models import Existpatient
from home.models import AfterPatient
from home.models import Live
# Register your models here.
admin.site.register(Newpatient)
admin.site.register(Existpatient)
admin.site.register(AfterPatient)
admin.site.register(Live)
