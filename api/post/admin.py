import logging
from django.contrib import admin
from django.utils.html import mark_safe
from django_admin_inline_paginator.admin import TabularInlinePaginated

from .model import Post






class PostAdmin(admin.ModelAdmin):
    save_on_top = True
    model = Post

    list_display = (
        "post_title",
        "user",

        "created_at",
    )

    exclude = ("can_reply",)
    readonly_fields = (
        "user",
        "post_title",
        "post_content",

    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(approved="pending")

    def has_add_permission(self, request, obj=None):
        return False

    stacked_inlines = []


    def save_model(self, request, obj, form, change):
        if obj.approved == "rejected":
            obj.send_notification()
        return super().save_model(request, obj, form, change)
