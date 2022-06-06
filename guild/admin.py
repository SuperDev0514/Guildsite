from django.contrib import admin

from .models import GuildSetting, GameContent
from .models import RaidGroup, Member, Character, GameClass

admin.site.register(GuildSetting)

admin.site.register(RaidGroup)
admin.site.register(Member)
admin.site.register(Character)
admin.site.register(GameClass)
admin.site.register(GameContent)