from .models import *
from django import forms
import logging
logger = logging.getLogger(__name__)


class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		exclude = [id,]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		show = None
		if self.data.get('show', None):
			try:
				show = Show.objects.get(pk=self.data['show'])
			except Show.DoesNotExist:
				pass
		else:
			try:
				show = self.instance.show
			except Show.DoesNotExist:
				pass
		if show:
			self.fields['character'].queryset = Character.objects.filter(show=show)
			self.fields['character_group'].queryset = CharacterGroup.objects.filter(show=show)
			self.fields['scene'].queryset = Scene.objects.filter(show=show)

	def clean(self):
		show_id = self.cleaned_data.get('show')
		entry_type = self.cleaned_data.get('entry_type')
		if entry_type == 'character':
			character = self.cleaned_data.get('character')
			if character == None:
				raise forms.ValidationError({
						"character": "Character must be set",
						})
			try:
				character = Character.objects.get(
					show=show_id,
					id=character.id)
			except:
				raise forms.ValidationError({
					"character": "Character is not from this show",
					})
		elif entry_type == 'group':
			character_group = self.cleaned_data.get('character_group')
			if character_group == None:
				raise forms.ValidationError({
					"character_group": "Character Group must be set",
					})
			try:
				character = CharacterGroup.objects.get(
					show=show_id,
					id=character_group.id)
			except:
				raise forms.ValidationError({
					"character_group": "Character Group is not from this show",
					})
		return self.cleaned_data


class SongForm(forms.ModelForm):
	class Meta:
		model = Song
		exclude = [id,]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		show = None
		if self.data.get('show', None):
			try:
				show = Show.objects.get(pk=self.data['show'])
			except Show.DoesNotExist:
				pass
		else:
			try:
				show = self.instance.show
			except Show.DoesNotExist:
				pass
		if show:
			self.fields['scene'].queryset = Scene.objects.filter(show=show)
			self.fields['featured_characters'].queryset = Character.objects.filter(show=show)
			self.fields['featured_groups'].queryset = Character.objects.filter(show=show)
			self.fields['ensemble_characters'].queryset = Character.objects.filter(show=show)
			self.fields['ensemble_groups'].queryset = Character.objects.filter(show=show)



class SceneForm(forms.ModelForm):
	class Meta:
		model = Scene
		exclude = [id,]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		show = None
		if self.data.get('show', None):
			try:
				show = Show.objects.get(pk=self.data['show'])
			except Show.DoesNotExist:
				pass
		else:
			try:
				show = self.instance.show
			except Show.DoesNotExist:
				pass
		if show:
			self.fields['act'].queryset = Act.objects.filter(show=show)
			self.fields['scene_location'].queryset = SceneLocation.objects.filter(show=show)
