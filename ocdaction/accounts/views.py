from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def my_account(request):
    return render(request, 'accounts/my_account.html')
