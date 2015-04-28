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
    data = request.POST.get('data')
    _pack = Pack.objects.create(subject=Subject.objects.get_or_create(name=request.user.pk))

    KeyPressTime.objects.bulk_create(
        [KeyPressTime(key=key_code, time=time, pack=_pack) for key_code, time in data.key_press]
    )
    KeyReleaseTime.objects.bulk_create(
        [KeyReleaseTime(key=key_code, time=time, pack=_pack) for key_code, time in data.key_release]
    )
    return HttpResponse('')



























