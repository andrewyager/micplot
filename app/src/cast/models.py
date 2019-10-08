from django.db import models
from show.models import *


class Actor(models.Model):
	name = models.CharField(max_length=255)
	preferred_name = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		if self.preferred_name:
			return self.preferred_name
		return self.name


class CharacterInShow(models.Model):
	run = models.ForeignKey(Run, on_delete=models.CASCADE)
	character = models.ForeignKey(
		Character,
		on_delete=models.CASCADE)
	primary_actor = models.ForeignKey(
		Actor,
		on_delete=models.CASCADE,
		blank=True,
		null=True,
		related_name='characters')
	understudy_actors = models.ManyToManyField(
		Actor,
		blank=True,
		related_name='understudy_characters')


	@property
	def show(self):
		return self.run.show
	

	def __str__(self):
		return "{} ({})".format(self.character, self.primary_actor)





