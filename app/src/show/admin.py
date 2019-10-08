from django.contrib import admin
from reversion.admin import VersionAdmin
from import_export.admin import ImportExportMixin
from .forms import *
from .models import *
from .resources import *


class PerformanceInline(admin.TabularInline):
	model = Performance


class RunInline(admin.TabularInline):
	model = Run

class ActInline(admin.TabularInline):
	model = Act

class SceneLocationInline(admin.TabularInline):
	model = SceneLocation

class SceneInline(admin.TabularInline):
	model = Scene
	form = SceneForm

class SongInline(admin.TabularInline):
	model = Song
	form = SongForm

class CharacterInline(admin.TabularInline):
	model = Character


@admin.register(SceneLocation)
class SceneLocationAdmin(VersionAdmin):
	list_display = [
		'show',
		'location'
	]

@admin.register(Show)
class ShowAdmin(ImportExportMixin, VersionAdmin):
	list_display = ['name']
	inlines = [
		RunInline,
		PerformanceInline,
		ActInline,
		SceneLocationInline,
		SceneInline,
		SongInline,
		CharacterInline
	]
	resource_class = ShowResource


@admin.register(Act)
class ActAdmin(ImportExportMixin, VersionAdmin):
	list_display = [
		'show',
		'name',
	]
	resource_class = ActResource


@admin.register(Scene)
class SceneAdmin(ImportExportMixin, VersionAdmin):
	list_display = [
		'show',
		'act',
		'name',
		'scene_location',
		'start_page',
		'end_page',
	]
	resource_class = SceneResource
	form = SceneForm


@admin.register(Song)
class SongAdmin(ImportExportMixin, VersionAdmin):
	list_display = [
		'show',
		'scene',
		'name',
		'lib_start_page',
		'lib_end_page',
	]
	resource_class = SongResource
	form = SongForm

@admin.register(CharacterType)
class CharacterTypeAdmin(ImportExportMixin, VersionAdmin):
	list_display = [
		'name'
	]
	resource_class = CharacterTypeResource


@admin.register(Character)
class CharacterAdmin(ImportExportMixin, VersionAdmin):
	list_display = [
		'show',
		'name',
		'character_type'
	]
	resource_class = CharacterResource


@admin.register(CharacterGroup)
class CharacterGroupAdmin(ImportExportMixin, VersionAdmin):
	list_display = [
		'show',
		'name',
	]
	resource_class = CharacterGroupResource


@admin.register(Entry)
class EntryAdmin(ImportExportMixin, VersionAdmin):
	list_display = [
		'character',
		'scene',
		'enter_page',
		'exit_page',
		'type'
	]
	resource_class = EntryResource
	form = EntryForm
