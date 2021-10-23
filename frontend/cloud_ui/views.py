from django.shortcuts import render

# Create your views here.
def getProcessedData(request):
    context = {}
    return render(request, "cloud_ui/index.html", context)