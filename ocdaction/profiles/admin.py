from django.contrib import admin
from custom_user.admin import EmailUserAdmin
from .models import OCDActionUser
from django.utils.translation import ugettext_lazy as _


class OCDActionUserAdmin(EmailUserAdmin):
    """
    You can customize the interface of your model here.
    """

    fieldsets = (
	        (None, {'fields': (('email','password1', 'password2', 'username'))}),
	        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
	                                       'groups', 'user_permissions')}),
	        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
	    )

# Register your models here.
admin.site.register(OCDActionUser, OCDActionUserAdmin)
