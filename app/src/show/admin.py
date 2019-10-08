from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import *


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

class CharacterInline(admin.TabularInline):
	model = Character

@admin.register(SceneLocation)
class SceneLocationAdmin(VersionAdmin):
	list_display = [
		'show',
		'location'
	]

@admin.register(Show)
class ShowAdmin(VersionAdmin):
	list_display = ['name']
	inlines = [
		RunInline,
		PerformanceInline,
		ActInline,
		SceneLocationInline,
		SceneInline,
		CharacterInline
	]


@admin.register(CharacterType)
class CharacterTypeAdmin(VersionAdmin):
	list_display = [
		'name'
	]


@admin.register(Character)
class CharacterAdmin(VersionAdmin):
	list_display = [
		'show',
		'name',
		'character_type'
	]


@admin.register(Entry)
class EntryAdmin(VersionAdmin):
	list_display = [
		'character',
		'scene',
		'enter_page',
		'exit_page',
		'type'
	]
