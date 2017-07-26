from django.shortcuts import render, redirect


def dashboard_index(request):
    """
    The Dashboard Index view.
    """

    template_name = "dashboard/dashboard_index.html"
    if request.user.is_authenticated():
        return render(request, template_name)
    else:
        return redirect('index')
