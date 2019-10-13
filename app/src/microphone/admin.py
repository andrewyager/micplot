from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
	pass


@admin.register(models.RxBand)
class RxBandAdmin(admin.ModelAdmin):
	pass


@admin.register(models.MicModel)
class MicModelAdmin(admin.ModelAdmin):
	pass


@admin.register(models.MicType)
class MicTypeAdmin(admin.ModelAdmin):
	pass


@admin.register(models.Microphone)
class MicrophoneAdmin(admin.ModelAdmin):
	pass


@admin.register(models.MicrophoneAssignment)
class MicrophoneAssignmentAdmin(admin.ModelAdmin):
	list_display = [
		'run',
		'microphone',
		'character'
	]
