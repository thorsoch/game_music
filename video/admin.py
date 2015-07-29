from django.contrib import admin
from video.models import Video, Comment, Like, Tag, Requesto
from video.models import UserProfile

# Register your models here.
# class PageAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'url')
#     search_fields = ['title']
#
# Add in this class to customized the Admin Interface
# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug':('name',)}

class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'video_id', 'likes', 'uploaded')
    search_fields = ['name']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'name', 'posted')
    search_fields = ['name']

class RequestoAdmin(admin.ModelAdmin):
    list_display = ('text', 'user_id')

admin.site.register(Video, VideoAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like)
admin.site.register(UserProfile)
admin.site.register(Requesto, RequestoAdmin)
admin.site.register(Tag)