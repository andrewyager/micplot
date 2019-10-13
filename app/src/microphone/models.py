from django.db import models
from django import apps


class Manufacturer(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name


class MicModel(models.Model):
	manufacturer = models.ForeignKey('microphone.Manufacturer', on_delete=models.CASCADE)
	name = models.CharField(max_length=255)

	def __str__(self):
		return "{} {}".format(self.manufacturer.name, self.name)


class RxBand(models.Model):
	band = models.CharField(max_length=255)
	frequency_low_mhz = models.PositiveIntegerField()
	frequency_high_mhz = models.PositiveIntegerField()

	def __str__(self):
		return self.band


class MicType(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name


class Microphone(models.Model):
	rx_number = models.CharField(max_length=255)
	model = models.ForeignKey('microphone.MicModel', on_delete=models.CASCADE, blank=True, null=True)
	type = models.ForeignKey('microphone.MicType', on_delete=models.CASCADE)
	rx_band = models.ForeignKey(RxBand, blank=True, null=True, on_delete=models.CASCADE)

	def __str__(self):
		if self.model is not None:
			if self.rx_band is not None:
				return "Mic {} - {} (Band {})".format(self.rx_number, self.model, self.rx_band)
			else:
				return "Mic {} - {}".format(self.rx_number, self.model)
		else:
			return "Mic {}".format(self.rx_number)


class MicrophoneAssignment(models.Model):
	show = models.ForeignKey('show.Show', on_delete=models.CASCADE)
	run = models.ForeignKey('show.Run', on_delete=models.CASCADE)
	character = models.ForeignKey('show.Character', on_delete=models.CASCADE)
	microphone = models.ForeignKey('microphone.Microphone', on_delete=models.CASCADE)
	fixed_assignment = models.BooleanField(default=True)

	def __str__(self):
		return "{} {}".format(self.character, self.microphone)


	class Meta:
		ordering = [
			'show',
			'run',
			'microphone__rx_number',
			'character__character_type__ordering_preference',
			'character__billing_order',
		]



