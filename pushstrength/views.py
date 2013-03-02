import mailchimp

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.validators import email_re
from django.http import HttpResponseRedirect

from .settings import MAILCHIMP_LIST_ID


def home(request):
    if request.method == 'POST':
        return subscribe(request)
    else:
        return render_to_response('index.html', {},
            context_instance=RequestContext(request))

def subscribe(request):
    # get and validate email
    email = request.POST.get('email', '')
    if not email or not email_re.match(email):
        error = u'Please, enter valid email address.'
        return render_to_response('index.html', {'error': error},
            context_instance=RequestContext(request))

    # get subscribers list and try to add new subscriber
    try:
        elist = mailchimp.utils.get_connection().get_list_by_id(
            MAILCHIMP_LIST_ID)
    except Exception:
        error = u'Sorry, there are some issues on the server. Please, try ' \
            'again  a bit later'
        return render_to_response('index.html', {'error': error},
            context_instance=RequestContext(request))
    
    # finally try to subscribe
    try:
        elist.subscribe(email, {'EMAIL': email})
    except Exception, e:
        # check if already subscribed
        if u'is already subscribed' in e.message:
            error = u'You are already subscribed to our newsletter.'
        elif u'Invalid Email Address' in e.message:
            error = u'Please, enter valid email address.'
        else:
            error = u'Sorry, there are some issues on the server. Please, ' \
                'try again  a bit later'
        return render_to_response('index.html', {'error': error},
            context_instance=RequestContext(request))

    # finally success
    msg = u'Please, find email in your inbox with further subscription ' \
        'confirmation details. Thank you for your request!'
    return HttpResponseRedirect(u'/?status_message=%s' % msg)
