from xml.dom.minidom import Document

from django.contrib import admin
from .models import *

admin.site.register(Documents)
admin.site.register(Lessons)
admin.site.register(Letters)
admin.site.register(Numbers)
