from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_index(request):
    """
    The Dashboard Index view.
    """

    template_name = "dashboard/dashboard_index.html"
    return render(request, template_name)
