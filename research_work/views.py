import json
from urllib.parse import quote_from_bytes, unquote

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from research_work.models import *


@csrf_exempt
@login_required
def send_pack(request):
    """
    data:{
        key_press[
            {
                key_code
                time
            }
        ]
        key_release[
            {
                key_code,
                time
            }
        ]
    }
    """
    data = json.loads(request.POST.get('data'))
    print("\ndata come: " + str(data) )

    _subject, _ = Subject.objects.get_or_create(name=request.user.pk)
    print("\nsubject created/get")

    _pack = Pack.objects.create(subject=_subject)
    print("\n_pack created")

    KeyPressTime.objects.bulk_create(
        [KeyPressTime(key=my_dict['key_code'], time=my_dict['time'], pack=_pack) for my_dict in data['key_press']]
    )
    print("\n kPresses added")

    KeyReleaseTime.objects.bulk_create(
        [KeyPressTime(key=my_dict['key_code'], time=my_dict['time'], pack=_pack) for my_dict in data['key_release']]
    )
    print("\nkReleases added")

    return HttpResponse('')



























