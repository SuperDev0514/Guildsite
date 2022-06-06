from unicodedata import name
from django.db import models

class GuildSetting(models.Model):
    key = models.CharField(max_length=200)
    value = models.TextField()

    def __str__(self):
        return self.key

class GameContent(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class RaidGroup(models.Model):
    name = models.CharField(max_length=100)

    primary = models.BooleanField(default=False)

    raid_size = models.IntegerField(default=0)

    schedule = models.CharField(max_length=200)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in RaidGroup._meta.fields]

    def __str__(self):
        return self.name

class Member(models.Model):
    discord_id = models.CharField(max_length=32)
    discord_username = models.CharField(max_length=32)

    public_note = models.TextField(default="", blank=True)

    raid = models.ForeignKey(RaidGroup, null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return self.discord_id

    def main_character(self):
        return self.character_set.filter(main=True).first()

    def characters(self):
        return self.character_set.order_by('-main')

class GameClass(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Character(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    ilevel = models.DecimalField(max_digits=12, decimal_places=2)
    main = models.BooleanField()

    character_class = models.ForeignKey(GameClass, on_delete=models.CASCADE, null=True)

    def __str__(self):
        mtxt = "";
        ctxt = "";
        if (self.main):
            mtxt = " (main)"
        if (self.character_class != None):
            ctxt = " ["+ self.character_class.name +"]"
        return self.member.discord_id + " - " + self.name + ctxt + mtxt