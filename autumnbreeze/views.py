from django.shortcuts import render, render_to_response
from django.template import RequestContext

from autumnbreeze.forms import AnomalyForm


def main(request):
    if request.method == "POST":
        form = AnomalyForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            context = {"results": 'results'}
            return render_to_response(
                "results.html",
                context,
                context_instance=RequestContext(request)
            )
        else:
            context = {"form": form}
            return render_to_response(
                "main.html",
                context,
                context_instance=RequestContext(request)
            )
    else:
        form = AnomalyForm()
        context = {"form": form}
        return render_to_response(
            "main.html",
            context,
            context_instance=RequestContext(request)
        )
    return render(request, 'main.html', {})


def results(request):
    return render(request, 'results.html', {})
