from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import Url

from analytics.models import ClickEvent
# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitUrlForm()

        context = {
            "title": "Url Shortner",
            "form": form
        }

        return render(request, "shortner/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)

        template = "shortner/home.html"
        context = {
            "title": "Url Shortner",
            "form": form
        }

        if form.is_valid():
            url = form.cleaned_data.get("url")
            obj, created = Url.objects.get_or_create(url=url)
            context = {
                "object": obj,
                "created": created
            }

            if created:
                template = "shortner/success.html";
            else:
                template = "shortner/alreadyexists.html"

        return render(request, template, context)



class URLRedirectView(View):

    def get(self, request, shortcode = None, *args, **kwargs):
        obj = get_object_or_404(Url, shortcode=shortcode)
        event = ClickEvent.objects.create_event(obj)
        return HttpResponseRedirect(obj.url)
        # return HttpResponse("Hello {shortcode}".format(shortcode = obj.url))

