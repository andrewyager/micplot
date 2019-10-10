from import_export import resources
from .models import *

class ActorResource(resources.ModelResource):
	class Meta:
		model = Actor

class CharacterInShowResource(resources.ModelResource):
	class Meta:
		model = CharacterInShow
