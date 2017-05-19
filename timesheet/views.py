from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'entry/index.html'
    context_object_name = 'latest_question_list'


    def get_queryset(self):
        """Return the last five published questions."""
        return 'lol'

# ======================================================
