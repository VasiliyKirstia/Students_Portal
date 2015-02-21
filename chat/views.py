from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from chat.models import Room, Message


@login_required
@csrf_exempt
def send(request):
    """
    Expects the following POST parameters:
    chat_room_id
    message
    """
    p = request.POST
    r = Room.objects.get(id=int(p['chat_room_id']))
    r.say(request.user, p['message'])
    return HttpResponse('')


@login_required
@csrf_exempt
def sync(request):
    """Return last message id

    EXPECTS the following POST parameters:
    id
    """
    if request.method != 'POST':
        raise Http404
    post = request.POST

    if not post.get('id'):
        raise Http404

    r = Room.objects.get(id=post['id'])

    lmid = r.last_message_id()

    return JsonResponse({'last_message_id': lmid})


@login_required
@csrf_exempt
def receive(request):
    """
    Returned serialized data

    EXPECTS the following POST parameters:
    id
    offset

    This could be useful:
    @see: http://www.djangosnippets.org/snippets/622/
    """
    if request.method != 'POST':
        raise Http404
    post = request.POST

    if not post.get('id') or not post.get('offset'):
        raise Http404

    try:
        room_id = int(post['id'])
    except:
        raise Http404

    try:
        offset = int(post['offset'])
    except:
        offset = 0

    r = Room.objects.get(id=room_id)

    m = r.messages(offset)

    #TODO придумать как по другому сериализовать сообщения
    return JsonResponse([message.to_json() for message in m], safe=False)


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


@login_required
@csrf_exempt
def test(request):
    """Test the chat application"""

    u = User.objects.get(id=1)  # always attach to first user id
    r = Room.objects.get_or_create(u)

    return render_to_response('chat/index.html', {'js': ['/media/js/mg/chat.js'], 'chat_id': r.pk},
                              context_instance=RequestContext(request))