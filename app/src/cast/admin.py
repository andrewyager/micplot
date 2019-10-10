from django.contrib import admin
from reversion.admin import VersionAdmin
from cast.models import *
from .resources import *
from import_export.admin import ImportExportMixin


@admin.register(Actor)
class ActorAdmin(ImportExportMixin, VersionAdmin):
	list_display = [
		'name',
		'preferred_name'
	]
	resource_class = ActorResource


@admin.register(CharacterInShow)
class CharacterInShowAdmin(ImportExportMixin, VersionAdmin):
	list_display = [
		'show',
		'run',
		'character',
		'primary_actor'
	]
	resource_class = CharacterInShowResource
