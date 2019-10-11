from django.shortcuts import render, get_object_or_404
from .models import *
from django.forms.models import model_to_dict

# Create your views here.

def song_detail_list(request, show_id=None, run_id=None):
	show = get_object_or_404(Show, pk=show_id)
	run = get_object_or_404(Run, pk=run_id)
	songs = []
	for song in show.song_set.all():
		songs.append({
				**model_to_dict(song),
				'featured_actor_list': song.featured_actor_list(run),
				'ensemble_actor_list': song.ensemble_actor_list(run),
				'featured_characters': song.featured_characters,
				'featured_groups': song.featured_groups,
				'emsemble_characters': song.ensemble_characters,
				'ensemble_groups': song.ensemble_groups,
			})
	return render(request, 'show/songsummary.html', {
			'show': show,
			'run': run,
			'songs': songs
		})