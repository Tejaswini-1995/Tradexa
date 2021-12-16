from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUserModel


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = (
            "email",
            "first_name",
            "last_name",
            "mobile",
            "otp",
            "password",

        )

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = (
            "email",
            "first_name",
            "last_name",
            "mobile",
            "otp",
            "password",
        )


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    readonly_fields=('created_at','updated_at')

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ("first_name", "last_name", "email",  "mobile")


    fieldsets = (
    ('Primary Info', {'fields':     ('email', 'mobile')}),
    ('Personal info', {'fields': ('first_name','last_name')}),

    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "mobile"),
            },
        ),
    )
    search_fields = ("first_name",'email')
    ordering = ("email",)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(CustomUserModel, UserAdmin)

admin.site.unregister(Group)