from django.shortcuts import render, get_object_or_404
from cast.models import *
from show.models import *
import logging

logger = logging.getLogger(__name__)


def cast_list(request, run_id=0):
	run = get_object_or_404(Run, pk=run_id)
	characters = run.show.character_set.all()
	character_groups = run.show.charactergroup_set.all()
	character_list = []
	for character in characters:
		characters_in_show = run.characterinshow_set.filter(character=character)
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
	for character in character_list:
		logger.warn(character)

	return render(request, 'cast/cast_list.html', context)