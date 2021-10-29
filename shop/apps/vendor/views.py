from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import Vendor


def become_vendor(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            # Save form as new user object
            user = form.save()
            # Log in new user
            login(request, user)
            # Create related vendor object for new user
            vendor = Vendor.objects.create(name=user.username, created_by=user)
            # Redirect user to homepage
            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'vendor/become_vendor.html', {'form': form})


@login_required
def vendor_admin(request):
    vendor = request.user.vendor

    return render(request, 'vendor/vendor_admin.html', {'vendor': vendor})
