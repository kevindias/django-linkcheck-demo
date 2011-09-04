from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from linkshare import forms
from linkshare import models


def index(request):
    """Displays all posts."""
    posts = models.Post.objects.all()
    return render_to_response("linkshare/index.html",
                              {'posts': posts},
                              context_instance=RequestContext(request))


def show_post(request, post_id):
    """Displays one post."""
    post = get_object_or_404(models.Post, pk=post_id)
    return render_to_response("linkshare/show_post.html",
                              {'post': post},
                              context_instance=RequestContext(request))


def add_post(request):
    """Adds a new post."""
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            return HttpResponseRedirect(new_post.get_absolute_url())
    else:
        form = forms.PostForm()
    return render_to_response("linkshare/add_post.html",
                              {'form': form},
                              context_instance=RequestContext(request))
