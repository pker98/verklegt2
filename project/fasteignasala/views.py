from django.shortcuts import render

apartments = [
    {
        "address" : "Vesturgata 73",
        "zip" : "300",
        "description" : "Vesturgata 73, 300 Akranes 3-4 herbergja íbúð á jarðhæð með sjávarútsýni. Forstofa með flísum á gólfi og góðum fataskáp.",
    },
    {
        "address" : "Bankastræti 73",
        "zip" : "101",
        "description" : "Vesturgata 73, 300 Akranes 3-4 herbergja íbúð á jarðhæð með sjávarútsýni. Forstofa með flísum á gólfi og góðum fataskáp.",
    },
{
        "address" : "Bankastræti 73",
        "zip" : "101",
        "description" : "Vesturgata 73, 300 Akranes 3-4 herbergja íbúð á jarðhæð með sjávarútsýni. Forstofa með flísum á gólfi og góðum fataskáp.",
    },
{
        "address" : "Bankastræti 73",
        "zip" : "101",
        "description" : "Vesturgata 73, 300 Akranes 3-4 herbergja íbúð á jarðhæð með sjávarútsýni. Forstofa með flísum á gólfi og góðum fataskáp.",
    },
{
        "address" : "Bankastræti 73",
        "zip" : "101",
        "description" : "Vesturgata 73, 300 Akranes 3-4 herbergja íbúð á jarðhæð með sjávarútsýni. Forstofa með flísum á gólfi og góðum fataskáp.",
    },
{
        "address" : "Bankastræti 73",
        "zip" : "101",
        "description" : "Vesturgata 73, 300 Akranes 3-4 herbergja íbúð á jarðhæð með sjávarútsýni. Forstofa með flísum á gólfi og góðum fataskáp.",
    },
{
        "address" : "Bankastræti 73",
        "zip" : "101",
        "description" : "Vesturgata 73, 300 Akranes 3-4 herbergja íbúð á jarðhæð með sjávarútsýni. Forstofa með flísum á gólfi og góðum fataskáp.",
    },
{
        "address" : "Bankastræti 73",
        "zip" : "101",
        "description" : "Vesturgata 73, 300 Akranes 3-4 herbergja íbúð á jarðhæð með sjávarútsýni. Forstofa með flísum á gólfi og góðum fataskáp.",
    },
]

# Create your views here.
def home(request):
    context = {"apartments" : apartments}
    return render(request, 'forsida/home.html', context)

def um_okkur(request):
    return render(request, 'um_okkur/um_okkur.html', {"title": "Um okkur"})

def starfsmenn(request):
    return render(request, 'starfsmenn/starfsmenn.html', {"title": "Starfsmenn"})

def soluskra(request):
    return render(request, 'soluskra/soluskra.html', {"title": "Söluskrá"})

def nyskraning(request):
    return render(request, 'nyskraning/nyskraning.html', {"title": "Nýskráning"})