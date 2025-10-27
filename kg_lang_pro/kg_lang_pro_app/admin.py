from xml.dom.minidom import Document

from django.contrib import admin
from .models import *

admin.site.register(Documents)
admin.site.register(Lesson)
admin.site.register(Letter)
admin.site.register(Numbers)
