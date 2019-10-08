from import_export import resources
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


class CharacterGroupResource(resources.ModelResource):
	class Meta:
		model = CharacterGroup


class CharacterTypeResource(resources.ModelResource):
	class Meta:
		model = CharacterType


class EntryResource(resources.ModelResource):
	class Meta:
		model = Entry