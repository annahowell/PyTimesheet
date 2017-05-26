from django.shortcuts import render, redirect
from django.utils import timezone

from timesheet_app.forms import AddEditClientForm
from timesheet_app.models import Client


def IndexView(request):
    if request.method == "POST":
        form = AddEditClientForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.client_business_name = form.cleaned_data.get('client_business_name')
            post.client_contact_name = form.cleaned_data.get('client_contact_name')
            post.client_phone_number = form.cleaned_data.get('client_phone_number')
            post.client_email = form.cleaned_data.get('client_email')
            post.client_address1 = form.cleaned_data.get('client_address1')
            post.client_address2 = form.cleaned_data.get('client_address2')
            post.client_postcode = form.cleaned_data.get('client_postcode')
            post.client_is_active = form.cleaned_data.get('client_is_active')


            post.client_created_on = timezone.now()
            post.client_modified_on = timezone.now()
            post.client_created_by = request.user.id
            post.client_modified_by = request.user.id
            post.save()
            return redirect('client')
    else:
        form = AddEditClientForm()
        existing_clients = Client.objects.filter(is_active=1)
        return render(request, 'client_add_edit.html', {'form': form, 'existing_clients': existing_clients})


# ======================================================
