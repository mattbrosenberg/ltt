from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.models import Group

from .models import User
from .forms import UserCreationForm, UserChangeForm
from trancheur.models import Bond, MoneyMarket, Residual


class MyUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'type_of',)
    list_filter = ('type_of',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email','username')
    ordering = ('email', 'type_of',)
    # filter_horizontal = ('type_of',)

admin.site.register(User, MyUserAdmin)
admin.site.unregister(Group)
admin.site.register(Bond)
admin.site.register(MoneyMarket)
admin.site.register(Residual)
