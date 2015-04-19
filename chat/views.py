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
from chat.models import Room, Message, Invite, Membership


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
            'rooms_list': [room.to_json() for room in request.user.room_set.all()],
            'invites_list': [invite.to_json() for invite in request.user.invites.all()],
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
    chat_room_id = request.POST.get('chat_room_id')
    message = request.POST.get('message')

    room = request.user.room_set.get(id=chat_room_id)
    room.say(request.user, message)
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
    chat_room_id = request.POST.get('chat_room_id')
    last_message_id = request.POST.get('last_message_id')
    last_invite_id = request.POST.get('last_invite_id')

    return JsonResponse(
        {
            'new_messages_count': request.user.room_set.get(id=chat_room_id).messages.filter(pk__gt=last_message_id).count() if chat_room_id else 0,
            'new_invites_count': request.user.invites.filter(pk__gt=last_invite_id).count() if last_invite_id else 0,
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
    chat_room_id = request.POST.get('chat_room_id')
    last_message_id = request.POST.get('last_message_id')
    last_invite_id = request.POST.get('last_invite_id')

    messages = []
    if chat_room_id is not None and Membership.objects.get(user=request.user, room=Room.objects.get(id=chat_room_id)):
        messages = [message.to_json() for message in Room.objects.get(id=chat_room_id).messages.filter(pk__gt=last_message_id)]

    return JsonResponse(
        {
            'new_messages': messages,
            'new_invites': [invite.to_json() for invite in request.user.invites.filter(pk__gt=last_invite_id)],
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
    users = request.POST.getlist('invited_users_list[]')  # TODO
    _room = Room.objects.get(id=request.POST.get('chat_room_id'))

    if not Membership.objects.get(user=request.user, room=_room):
        raise Http404

    for _user in User.objects.in_bulk(users).values():
        Invite.objects.update_or_create(room=_room, to=_user)
    return HttpResponse('')


@login_required
@csrf_exempt
def remove_invite(request):
    """
    необходимо:
                room_id
    возвращает:
                НИЧЕГОШЕНЬКИ,
    """
    invite = Invite.objects.get(to=request.user, room=Room.objects.get(id=request.POST.get('room_id')))
    if invite is not None:
        invite.delete()
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
    new_room_name = request.POST.get('new_room_name')

    new_room = Room(title=new_room_name)
    new_room.save()
    new_room.join(request.user)

    return JsonResponse(
        {
            'new_room_id': new_room.id,
            'new_room_name': new_room.title,
        }
    )


@login_required
@csrf_exempt
def join(request):
    """
    необходимо:
                chat_room_id
    возвращает:
                НИЧЕГОШЕНЬКИ
    """
    room = Room.objects.get(id=request.POST.get('chat_room_id'))
    if request.user.invites.filter(room=room):
        room.join(request.user)
    return HttpResponse('')


@login_required
@csrf_exempt
def leave(request):
    """
    необходимо:
                chat_room_id
    возвращает:
                НИЧЕГОШЕНЬКИ
    """
    room = Room.objects.get(id=request.POST.get('chat_room_id'))
    room.leave(request.user)
    if not Membership.objects.filter(room=room):
        room.delete()
    return HttpResponse('')