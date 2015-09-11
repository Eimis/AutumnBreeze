from django.contrib import admin

from autumnbreeze.models import ComparingOption


class ComparingOptionAdmin(admin.ModelAdmin):
    pass


admin.site.register(ComparingOption, ComparingOptionAdmin)
