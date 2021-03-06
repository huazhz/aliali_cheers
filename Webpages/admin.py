from django.contrib import admin
from .models import Picture, Picture_Comment, Video, Catagory, \
    Video_Comment, Audio, Audio_Comment, Like_Item, Dislike_Item, Collect_Item


class AudioAdmin(admin.ModelAdmin):
    list_display = ['user', 'audio', 'upload_time']


admin.site.register(Audio, AudioAdmin)


class Audio_CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'audio', 'create_time']


admin.site.register(Audio_Comment, Audio_CommentAdmin)


class PictureAdmin(admin.ModelAdmin):
    list_display = ['user', 'picture', 'upload_time']


admin.site.register(Picture, PictureAdmin)


class Picture_CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'picture', 'create_time']


admin.site.register(Picture_Comment, Picture_CommentAdmin)


class VideoAdmin(admin.ModelAdmin):
    list_display = ['user', 'video', 'upload_time']


admin.site.register(Video, VideoAdmin)


class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['catagory_name']


admin.site.register(Catagory, CatagoryAdmin)


class Video_CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'video', 'create_time']


admin.site.register(Video_Comment, Video_CommentAdmin)


class Like_ItemAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(Like_Item, Like_ItemAdmin)


class Dislike_ItemAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(Dislike_Item, Dislike_ItemAdmin)


class Collect_ItemAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(Collect_Item, Collect_ItemAdmin)
