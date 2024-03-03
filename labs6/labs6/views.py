from django.shortcuts import render, redirect, get_object_or_404
from .models import Agent, Property, Client, Request
from .forms import AgentForm, PropertyForm, ClientForm, RequestForm

# Agent views---------------------------------------------------------
def agent_list(request):
    agents = Agent.objects.all()
    return render(request, 'agent_list.html', {'agents': agents})

def agent_detail(request, id):
    agent = get_object_or_404(Agent, pk=id)
    return render(request, 'agent_detail.html', {'agent': agent})

def agent_create(request):
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agent_list')
    else:
        form = AgentForm()
    return render(request, 'agent_form.html', {'form': form})

def agent_update(request, id):
    agent = get_object_or_404(Agent, pk=id)
    if request.method == 'POST':
        form = AgentForm(request.POST, instance=agent)
        if form.is_valid():
            form.save()
            return redirect('agent_list')
    else:
        form = AgentForm(instance=agent)
    return render(request, 'agent_form.html', {'form': form})

def agent_delete(request, id):
    agent = get_object_or_404(Agent, pk=id)
    agent.delete()
    return redirect('agent_list')

# Property views---------------------------------------------------------
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

def property_detail(request, id):
    property = get_object_or_404(Property, pk=id)
    return render(request, 'property_detail.html', {'property': property})

def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'property_form.html', {'form': form})

def property_update(request, id):
    property = get_object_or_404(Property, pk=id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'property_form.html', {'form': form})

def property_delete(request, id):
    property = get_object_or_404(Property, pk=id)
    property.delete()
    return redirect('property_list')

# Client views---------------------------------------------------------
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def client_detail(request, id):
    client = get_object_or_404(Client, pk=id)
    return render(request, 'client_detail.html', {'client': client})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})

def client_update(request, id):
    client = get_object_or_404(Client, pk=id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {'form': form})

def client_delete(request, id):
    client = get_object_or_404(Client, pk=id)
    client.delete()
    return redirect('client_list')

# Request views---------------------------------------------------------
def request_list(request):
    requests = Request.objects.all()
    return render(request, 'request_list.html', {'requests': requests})

def request_detail(request, id):
    request_obj = get_object_or_404(Request, pk=id)
    return render(request, 'request_detail.html', {'request': request_obj})

def request_create(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_list')
    else:
        form = RequestForm()
    return render(request, 'request_form.html', {'form': form})

def request_update(request, id):
    request_obj = get_object_or_404(Request, pk=id)
    if request.method == 'POST':
        form = RequestForm(request.POST, instance=request_obj)
        if form.is_valid():
            form.save()
            return redirect('request_list')
    else:
        form = RequestForm(instance=request_obj)
    return render(request, 'request_form.html', {'form': form})

def request_delete(request, id):
    request_obj = get_object_or_404(Request, pk=id)
    request_obj.delete()
    return redirect('request_list')
