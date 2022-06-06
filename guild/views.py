from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuildSetting, RaidGroup, Character, GameClass
import requests

# Create your views here.

def get_base_context():
    context = {
        'guildname': GuildSetting.objects.get(key='guildname').value,
        'serverregion': GuildSetting.objects.get(key='serverregion').value,
        'lookingfor': GuildSetting.objects.get(key='lookingfor').value,
        'aboutguild': GuildSetting.objects.get(key='aboutguild').value,
        'guildperks': GuildSetting.objects.get(key='guildperks').value,

        'raidgroups': RaidGroup.objects.filter(primary=True),
        'subgroups': RaidGroup.objects.filter(primary=False),
        'aboutroster': GuildSetting.objects.get(key='aboutroster').value,

        'codeofconduct': GuildSetting.objects.get(key='codeofconduct').value,
    }
    return context

def save_profile(request):
    print(request.POST)

    characters = Character.objects.filter(member__discord_username=request.user.username)

    for character in characters:
        rpc = request.POST.get('c_' + str(character.id))
        character.ilevel = rpc
        character.save()

    return redirect('index')

def profile(request):
    context = get_base_context()

    context['username'] = request.user.username

    characters = Character.objects.filter(member__discord_username=request.user.username)

    context['characters'] = characters

    return render(request, 'profile.html', context)

def submit_apply(request):
    mUrl = GuildSetting.objects.get(key='discordhook').value

    player_content = "*** Discord ID *** : " + request.POST['discord_name']
    player_content += "\n" + request.POST['playtime']
    player_content += "\n *** Character Details ***" 
    player_content += "\n" + request.POST['character_name'] + " iLevel "
    player_content += request.POST['character_ilevel'] 
    class_name = GameClass.objects.get(id=request.POST['character_class']).name
    player_content += " [" + class_name + "]"

    data = {"content": player_content}

    response = requests.post(mUrl, json=data)

    return redirect('index')

def apply(request):
    context = get_base_context()

    context['character_classes'] = GameClass.objects.all()

    return render(request, 'apply.html', context)

def charts(request):
    context = get_base_context()
    roster = Character.objects.all()
    classes = GameClass.objects.all()
    context['roster'] = roster
    context['classes'] = classes

    classCounts = []
    for classinfo in classes:
        classCounts.append(Character.objects.filter(character_class__id=classinfo.id).count())

    context['class_counts'] = classCounts
    context['class_count'] = classes.count()

    return render(request, 'charts.html', context)

def index(request):
    context = get_base_context()
    return render(request, 'main.html', context)