from django.db import models

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
	ensemble_characters = models.ManyToManyField(
		'Character',
		blank=True,
		related_name='ensemble_songs')

	def __str__(self):
		return self.name

	class Meta:
		ordering = [
			'lib_start_page',
			'lib_end_page',
			'name',
		]


class CharacterType(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Character(models.Model):
	show = models.ForeignKey(Show, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	character_type = models.ForeignKey(CharacterType, on_delete=models.CASCADE)
	scenes = models.ManyToManyField(Scene, blank=True)

	def __str__(self):
		return self.name

class Entry(models.Model):
	character = models.ForeignKey(
		Character,
		on_delete=models.CASCADE)
	scene = models.ForeignKey(
		Scene,
		on_delete=models.CASCADE)
	enter_page = models.PositiveIntegerField()
	exit_page = models.PositiveIntegerField(blank=True, null=True)
	type = models.CharField(
		max_length=255,
		choices=[
			('On Stage', 'On Stage'),
			('Off Stage', 'Off Stage'),
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