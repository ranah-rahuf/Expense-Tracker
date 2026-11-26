from django.http import HttpResponse

def home(request):
    return HttpResponse("Smart Expense Tracker is alive!")