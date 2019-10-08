from django.contrib import admin
from reversion.admin import VersionAdmin
from cast.models import *

@admin.register(Actor)
class ActorAdmin(VersionAdmin):
	list_display = [
		'name',
		'preferred_name'
	]

@admin.register(CharacterInShow)
class CharacterInShowAdmin(VersionAdmin):
	list_display = [
		'show',
		'run',
		'character',
		'primary_actor'
	]
