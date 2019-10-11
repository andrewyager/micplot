from django.db import models
from django.apps import apps

class Show(models.Model):
	name = models.CharField(max_length=255)
	script_edition = models.CharField(
		max_length=255,
		default="First Edition")
	copyright = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name

class Run(models.Model):
	show = models.ForeignKey(Show, on_delete=models.CASCADE)
	start_date = models.DateField()
	end_date = models.DateField()

	def __str__(self):
		return "{} ({} - {})".format(self.show, self.start_date, self.end_date)

class Performance(models.Model):
	show = models.ForeignKey(Show, on_delete=models.CASCADE)
	run = models.ForeignKey(Run, on_delete=models.CASCADE)
	date = models.DateField()
	time = models.TimeField()
	

	def __str__(self):
		return "{} ({} at {})".format(self.run, self.date, self.time)


class Act(models.Model):
	show = models.ForeignKey(Show, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name


class SceneLocation(models.Model):
	show = models.ForeignKey(Show, on_delete=models.CASCADE)
	location = models.CharField(max_length=255)

	def __str__(self):
		return self.location


class Scene(models.Model):
	show = models.ForeignKey(Show, on_delete=models.CASCADE)
	act = models.ForeignKey(Act, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	scene_location = models.ForeignKey(
		SceneLocation,
		on_delete=models.CASCADE,
		blank=True,
		null=True)
	start_page = models.PositiveIntegerField()
	end_page = models.PositiveIntegerField()

	def __str__(self):
		return "{} {}".format(self.act, self.name)

	class Meta:
		ordering = [
			'show',
			'start_page',
			'end_page',
			'name',
		]


class Song(models.Model):
	show = models.ForeignKey(Show, on_delete=models.CASCADE)
	scene = models.ForeignKey(Scene, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	lib_start_page = models.PositiveIntegerField()
	lib_end_page = models.PositiveIntegerField()
	featured_characters = models.ManyToManyField(
		'Character',
		blank=True,
		related_name='featured_songs')
	featured_groups = models.ManyToManyField(
		'CharacterGroup',
		blank=True,
		related_name='featured_group_songs')
	ensemble_characters = models.ManyToManyField(
		'Character',
		blank=True,
		related_name='ensemble_songs')
	ensemble_groups = models.ManyToManyField(
		'CharacterGroup',
		blank=True,
		related_name='ensemble_group_songs')

	def __str__(self):
		return self.name

	def featured_actor_list(self, run):
		CharacterInShow = apps.get_model('cast.CharacterInShow')
		actors = []
		for character in self.featured_characters.all():
			actor_list = CharacterInShow.objects.filter(character=character)
			for actor in actor_list:
				if actor not in actors:
					actors.append(actor)
		for group in self.featured_groups.all():
			for character in group.characters.all():
				actor_list = CharacterInShow.objects.filter(character=character)
				for actor in actor_list:
					if actor not in actors:
						actors.append(actor)
		return actors

	def ensemble_actor_list(self, run):
		CharacterInShow = apps.get_model('cast.CharacterInShow')
		actors = []
		for character in self.ensemble_characters.all():
			actor_list = CharacterInShow.objects.filter(character=character)
			for actor in actor_list:
				if actor not in actors:
					actors.append(actor)
		for group in self.ensemble_groups.all():
			for character in group.characters.all():
				actor_list = CharacterInShow.objects.filter(character=character)
				for actor in actor_list:
					if actor not in actors:
						actors.append(actor)
		return actors
	

	class Meta:
		ordering = [
			'show',
			'lib_start_page',
			'lib_end_page',
			'name',
		]


class CharacterType(models.Model):
	name = models.CharField(max_length=255)
	ordering_preference = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.name

	class Meta:
		ordering = [
			'ordering_preference',
			'name'
		]

class Character(models.Model):
	show = models.ForeignKey(Show, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	character_type = models.ForeignKey(CharacterType, on_delete=models.CASCADE)
	scenes = models.ManyToManyField(Scene, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = [
			'show',
			'character_type__ordering_preference',
			'name',
		]

class CharacterGroup(models.Model):
	show = models.ForeignKey(Show, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	scenes = models.ManyToManyField(Scene, blank=True)
	characters = models.ManyToManyField(Character, blank=True)

	def __str__(self):
		return self.name

class Entry(models.Model):
	show = models.ForeignKey(Show, on_delete=models.CASCADE)
	entry_type = models.CharField(
		max_length=255,
		choices=[
			('character', 'Character'),
			('group', 'Group')
		])
	character = models.ForeignKey(
		Character,
		on_delete=models.CASCADE,
		blank=True,
		null=True)
	character_group = models.ForeignKey(
		CharacterGroup,
		on_delete=models.CASCADE,
		blank=True,
		null=True)
	scene = models.ForeignKey(
		Scene,
		on_delete=models.CASCADE)
	enter_page = models.PositiveIntegerField()
	exit_page = models.PositiveIntegerField(blank=True, null=True)
	speaks = models.BooleanField(default=True)
	type = models.CharField(
		max_length=255,
		choices=[
			('On Stage', 'On Stage'),
			('Off Stage', 'Off Stage Voice/Action'),
		],
		default='On Stage')

	def __str__(self):
		if self.exit_page:
			return "{} - {} Enters {} {} Exits {}".format(
				self.character,
				self.scene,
				self.enter_page,
				self.type,
				self.exit_page)
		return "{} - {} Enters {} {}".format(
			self.character,
			self.scene,
			self.enter_page,
			self.type)