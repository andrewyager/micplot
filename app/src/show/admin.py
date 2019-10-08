from django.contrib import admin
from reversion.admin import VersionAdmin
from import_export import resources
from import_export.admin import ImportExportMixin
from .models import *

class ShowResource(resources.ModelResource):
	class Meta:
		model = Show


class RunResource(resources.ModelResource):
	class Meta:
		model = Run


class PerformanceResource(resources.ModelResource):
	class Meta:
		model = Performance

class ActResource(resources.ModelResource):
	class Meta:
		model = Act


class SceneLocationResource(resources.ModelResource):
	class Meta:
		model = SceneLocation


class SceneResource(resources.ModelResource):
	class Meta:
		model = Scene

class SongResource(resources.ModelResource):
	class Meta:
		model = Song


class CharacterResource(resources.ModelResource):
	class Meta:
		model = Character


class CharacterTypeResource(resources.ModelResource):
	class Meta:
		model = CharacterType


class EntryResource(resources.ModelResource):
	class Meta:
		model = Entry


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

class SongInline(admin.TabularInline):
	model = Song

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
