from django.shortcuts import render, redirect


def home_index(request):
    """
    The Home Index view.
    """

    template_name = "index.html"
    if request.user.is_authenticated():
        return redirect('task-list')
    else:
        return render(request, template_name)
