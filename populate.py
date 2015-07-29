# -*- coding: utf-8 -*-

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'game_music.settings')

import django
django.setup()

from video.models import Video, Comment, Tag, Like, Requesto
from django.utils import timezone

def populate():

    add_video("zYNsQ6ibdZs", "test")
    add_video("97SY3wNIh0w", "test2", tag='music')
    add_video("JKl8m3TRGjM", "test3", tag='music')
    add_video("2_Z73-rMZLw", "test4", tag='music')
    add_video("hRWkVrJJHPY", "test5")
    add_video("kkFVOuO2gZ4", "長いタイトルを入れると表示されるのはtestawinaoewgnaignoaingioangoianiwegnoangiangoawingionaiwgnaowinga")
    add_video("t_G4MXjgnGE", "途中までです")

def channel_retrieve(chan_id):
    # grab all the videos in a channel and run add_video with it
    pass

def add_video(video_id, title, tag=None):
    p = Video.objects.get_or_create(video_id = video_id)[0]
    p.name = title
    p.url = "https://www.youtube.com/embed/" + video_id

    p.thumb = "http://img.youtube.com/vi/" + video_id + "/1.jpg"
    p.uploaded = timezone.now()

    if tag:
        t = Tag.objects.get_or_create(video_id = video_id)[0]
        t.name = tag
        t.save()

    p.save()
    return p

def kill_user(user_id):
    # delete user and all user's comments with corresponding user_id
    pass

# Start execution here!
if __name__ == '__main__':
    Video.objects.all().delete()
    Comment.objects.all().delete()
    Like.objects.all().delete()
    Requesto.objects.all().delete()
    print("Starting Video population script...")
    populate()