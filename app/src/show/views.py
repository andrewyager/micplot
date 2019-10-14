from django.shortcuts import render, get_object_or_404
from .models import *
from django.forms.models import model_to_dict
from cast.models import *
from microphone.models import *

import logging

logger = logging.getLogger(__name__)

# Create your views here.

def song_detail_list(request, show_id=None, run_id=None):
    show = get_object_or_404(Show, pk=show_id)
    run = get_object_or_404(Run, pk=run_id)
    songs = []


    for song in show.song_set.all():
        featured_actor_list = song.featured_actor_list(run)
        ensemble_actor_list = song.ensemble_actor_list(run)
        ensemble_actor_list = [x for x in ensemble_actor_list if x not in featured_actor_list]

        featured_characters = song.featured_characters.all()
        ensemble_characters = song.ensemble_characters.all()
        ensemble_characters = [x for x in ensemble_characters if x not in featured_characters]

        featured_groups = song.featured_groups.all()
        ensemble_groups = song.ensemble_groups.all()
        ensemble_groups = [x for x in ensemble_groups if x not in featured_groups]
        songs.append({
                **model_to_dict(song),
                'scene': song.scene,
                'featured_actor_list': featured_actor_list,
                'ensemble_actor_list': ensemble_actor_list,
                'featured_characters': featured_characters,
                'featured_groups': featured_groups,
                'emsemble_characters': ensemble_characters,
                'ensemble_groups': ensemble_groups,
            })
    return render(request, 'show/songsummary.html', {
            'show': show,
            'run': run,
            'songs': songs
        })

def minimal_mic_character_list_by_actor(request, show_id=None, run_id=None):
    show = get_object_or_404(Show, pk=show_id)
    run = get_object_or_404(Run, pk=run_id)
    mic_assigned = []
    nomic_assigned = []

    character_assignments = CharacterInShow.objects.filter(run=run).select_related('primary_actor').order_by('primary_actor__name')

    last_character = None
    mic_list = []
    add = False

    for ca in character_assignments:
        if last_character != ca.primary_actor:
            if add:
                mic = MicrophoneAssignment.objects.filter(show=show, run=run, character__in=mic_list)
                logger.warn(mic)
                if mic:
                    mic_assigned.append({
                        'actor': last_character,
                        'micable_characters': mic_list
                        })
                else:
                    nomic_assigned.append({
                        'actor': last_character,
                        'micable_characters': mic_list
                        })
            add = False
            last_character = ca.primary_actor
            mic_list = []
        if ca.character.character_type.could_use_microphone:
            add = True
            mic_list.append(ca.character)

    if add:
        if mic:
            mic_assigned.append({
                        'actor': last_character,
                        'micable_characters': mic_list
                        })
        else:
            nomic_assigned.append({
                'actor': last_character,
                'micable_characters': mic_list
                })

    microphones = Microphone.objects.all()
    characters = mic_assigned + nomic_assigned
    return render(request, 'show/charactermicsummary.html', {
            'show': show,
            'run': run,
            'characters': characters,
            'mic_assigned': mic_assigned,
            'nomic_assigned': nomic_assigned,
            'microphones': microphones,
            'changes': len(characters) - len(microphones)
        })

def micindex(request, show_id=None, run_id=None):

    show = get_object_or_404(Show, pk=show_id)
    run = get_object_or_404(Run, pk=run_id)

    return render(request, 'show/micindex.html', {
            'show': show,
            'run': run
        })


