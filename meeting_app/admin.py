from django.contrib import admin

from .models.user import CustomUser
from .models.user_profile import UserProfile
from .models.group import CustomGroup
from .models.user_group import UserGroup
from .models.topic import Topic
from .models.progress import Progress
from .models.post import Post
from .models.notification import Notification
from .models.meeting import Meeting
from .models.daily_note import Note
from .models.comment import Comment

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(CustomGroup)
class CustomGroupAdmin(admin.ModelAdmin):
    pass

@admin.register(UserGroup)
class UserGroupAdmin(admin.ModelAdmin):
    pass

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    pass

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass