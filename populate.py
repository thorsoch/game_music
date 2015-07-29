# -*- coding: utf-8 -*-

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'game_music.settings')

import django
django.setup()

from video.models import Video, Comment, Tag, Like, Requesto
from django.utils import timezone

def populate():

    add_video("SU2Wvcg2jmM", "名を冠する者たち＜ゼノブレイド＞", tag='ゼノブレイド')
    add_video("j3pE1yyEGRk", "機の律動＜ゼノブレイド＞", tag='ゼノブレイド')
    add_video("2CQDonCO6Ws", "敵との対峙＜ゼノブレイド＞", tag='ゼノブレイド')
    add_video("4fuTpR9j-tA", "ガウル平原 昼＜ゼノブレイド＞", tag='ゼノブレイド')
    add_video("aH8HIebZlyg", "太陽は昇る＜大神＞", tag='大神')
    add_video("ZzSeDQh9TDk", "Overdosing Heavenly Bliss＜空の軌跡 the 3rd＞", tag='空の軌跡 the 3rd')
    add_video("KlqHx8tr9o0", "追究 ～つきとめたくて＜逆転検事２＞", tag='逆転検事２')
    add_video("mDnr_-Gc-ZI", "時の回廊＜クロノ・トリガー＞", tag='クロノ・トリガー')

    add_video("BroCkzRgaCU", "彼の者の名は＜ブレデフォFF＞", tag='ブレイブリーデフォルト フライング・フェアリー')
    add_video("XxGFVxqILN0", "地平を喰らう蛇＜ブレデフォFF＞", tag='ブレイブリーデフォルト フライング・フェアリー')
    add_video("9Muuejw2qNY", "戦闘！ホウオウ＜ポケモンHGSS＞", tag='ポケットモンスター ハートゴールド・ソウルシルバー')
    add_video("gOPZdnRcHGc", "Red Zone＜トトリのアトリエ＞", tag='トトリのアトリエ ～アーランドの錬金術士2～')
    add_video("-Xf-Pa4jCCs", "10番道路＜ポケモンBW＞", tag='ポケットモンスター ブラック・ホワイト')
    add_video("-7r6rzUw0k8I", "戦闘！チャンピオンアイリス＜ポケモンBW2＞", tag='ポケットモンスター ブラック2・ホワイト2')
    add_video("dwtASYeer8Y", "Megalomania＜ライブ・ア・ライブ＞", tag='ライブ・ア・ライブ')
    add_video("o7AT9wfZNMw", "仲間を求めて＜ファイナルファンタジーVI＞", tag='ファイナルファンタジーVI')
    add_video("uH-bOjFgyvY", "決戦！ディアルガ！＜ポケダン時闇＞", tag='ポケモン不思議のダンジョン 時の探検隊・闇の探検隊')

    add_video("8NkWgW-kDKo", "全ての人の魂の戦い", tag='ペルソナ3')
    add_video("1bG6PPQyxyI", "Reach Out To The Truth", tag='ペルソナ4')

    add_video("POPD80fxcD4", "CROWNED＜星のカービィ Wii＞", tag='星のカービィ Wii')
    add_video("V2mMvaN_WVA", "伝説のエアライドマシン＜カービィのエアライド＞", tag='カービィのエアライド')
    add_video("uTOt8uUBj4A", "コルダ＜カービィのエアライド＞", tag='カービィのエアライド')
    add_video("BW0NiufrMsQ", "シティトライアル＜カービィのエアライド＞", tag='カービィのエアライド')
    add_video("gvdZ4_CQt5g", "ポップスター＜星のカービィ64＞", tag='星のカービィ64')
    add_video("ggGPqnkCihY", "ゼロ・ツー＜星のカービィ64＞", tag='星のカービィ64')


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