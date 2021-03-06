from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from cast.models import *
from show.models import *
import logging
import plistlib

logger = logging.getLogger(__name__)


def character_list(request, run_id=0):
	run = get_object_or_404(Run, pk=run_id)
	characters = CharacterInShow.objects.filter(run=run).select_related('primary_actor').order_by('primary_actor__name')

	context = {
		'run': run,
		'characters': characters
	}

	return render(request, 'cast/character_list.html', context)

def cast_export(request, run_id=0):
	run = get_object_or_404(Run, pk=run_id)
	characters = CharacterInShow.objects.filter(run=run).select_related('primary_actor').order_by('primary_actor__name')

	character_list = []

	for character in characters:
		obj = {
			'comments': '',
			'Name': str(character.primary_actor.name).strip(),
			'RoleName': str(character.character.name).strip(),
			'Scaled': False,
			'Compressed': False,
			'Version': 1
		}
		character_list.append(obj)

	plist = plistlib.dumps(character_list)

	response = HttpResponse(plist, content_type='application/wavetool-players')
	response['Content-Disposition'] = 'attachment; filename="{}.pla"'.format(run.show.name)
	return response



def cast_list(request, run_id=0):
	run = get_object_or_404(Run, pk=run_id)
	characters = run.show.character_set.all()
	character_groups = run.show.charactergroup_set.order_by('name')
	character_list = []
	for character in characters:
		characters_in_show = run.characterinshow_set.filter(character=character).order_by('character__name')
		co = {
			'name': character.name,
			'type': character.character_type,
			'actor_list': characters_in_show
		}
		character_list.append(co)

	group_list = []
	for group in character_groups:
		characters = []
		actors = []
		for character in group.characters.all():
			characters_in_show = run.characterinshow_set.filter(character=character)
			actor_list = []
			for actor in characters_in_show:
				if actor.primary_actor:
					if actor.primary_actor.pk not in actors:
						actors.append(actor.primary_actor.pk)
						actor_list.append(actor)
			co = {
				'name': character.name,
				'actors': actor_list
			}
			if actor_list:
				characters.append(co)
		go = {
			'name': group.name,
			'characters': characters
		}
		group_list.append(go)

	context = {
		'run': run,
		'characters_in_show': character_list,
		'character_groups': group_list,
	}

	return render(request, 'cast/cast_list.html', context)