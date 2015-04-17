from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from mixins.permissions import LoginRequiredMixin
from django.utils import timezone
from chat.models import Room, Message,Invite


@login_required
@csrf_exempt
def init(request):
    """
    необходимо:
                НИЧЕГОШЕНЬКИ
    возвращает:
                rooms_list,
                invites_list.
    """
    return JsonResponse(
        {
            'rooms_list': [room.to_json() for room in Room.objects.filter(user=request.user)],  # TODO
            'invites_list': [invite.to_json() for invite in User.objects.filter(user=request.user).invites],
        }
    )


@login_required
@csrf_exempt
def send(request):
    """
    необходимо:
                chat_room_id
                message
    возвращает:
                НИЧЕГОШЕНЬКИ
    """
    chat_room_id = request.POST['chat_room_id']
    message = request.POST['message']
    r = Room.objects.get(id=int(chat_room_id))
    r.say(request.user, message)
    return HttpResponse('')


@login_required
@csrf_exempt
def passive_sync(request):
    """
    необходимо:
                chat_room_id
                last_message_id
                last_invite_id
    возвращает:
                new_messages_count
                new_invites_count
    """
    chat_room_id = request.POST['chat_room_id']
    last_message_id = request.POST['last_message_id']
    last_invite_id = request.POST['last_invite_id']

    return JsonResponse(
        {
            'new_messages_count': Room.objects.get(id=chat_room_id).messages.filter(pk__gt=last_message_id).count(),
            'new_invites_count': User.objects.get(pk=request.user).invites.filter(pk__gt=last_invite_id).count(),
        }
    )


@login_required
@csrf_exempt
def active_sync(request):
    """
    необходимо:
                chat_room_id
                last_message_id
                last_invite_id
    возвращает:
                new_messages
                new_invites
    """
    chat_room_id = request.POST['chat_room_id']
    last_message_id = request.POST['last_message_id']
    last_invite_id = request.POST['last_invite_id']

    # TODO придумать как по другому сериализовать объекты
    return JsonResponse(
        {
            'new_messages': [message.to_json() for message in
                             Room.objects.get(id=chat_room_id).messages.filter(pk__gt=last_message_id)],
            'new_invites': [invite.to_json() for invite in
                            User.objects.get(pk=request.user).invites.filter(pk__gt=last_invite_id)],
        }
    )


@login_required
@csrf_exempt
def invitation(request):
    """
    необходимо:
                invited_users_list
                chat_room_id
    возвращает:
                НИЧЕГОШЕНЬКИ,
    """
    users = request.POST['invited_users_list']
    _room = Room.objects.get(id=request.POST['chat_room_id'])

    for _user in users:
        invite = Invite(room=_room, user=_user)
        invite.save()
    return HttpResponse('')


@login_required
@csrf_exempt
def create_room(request):
    """
    необходимо:
                new_room_name
    возвращает:
                new_room_id
                new_room_name
    """



@login_required
@csrf_exempt
def join(request):
    """
    Expects the following POST parameters:
    chat_room_id
    message
    """
    p = request.POST
    r = Room.objects.get(id=int(p['chat_room_id']))
    r.join(request.user)
    return HttpResponse('')


@login_required
@csrf_exempt
def leave(request):
    """
    Expects the following POST parameters:
    chat_room_id
    message
    """
    p = request.POST
    r = Room.objects.get(id=int(p['chat_room_id']))
    r.leave(request.user)
    return HttpResponse('')