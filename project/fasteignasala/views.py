from django.shortcuts import render
# from fasteignasala.models import Base_user

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
        "address" : "Bólstaðahlíð 26",
        "zip" : "105",
        "description" : "Bólstaðahlíð 26, 105 Reykjavík 2-3 herbergja hús á jarðhæð með sjávarútsýni. Forstofa með flísum á gólfi og góðum fataskáp.",
    },
{
        "address" : "Stekkjargerði 14",
        "zip" : "600",
        "description" : "Stekkjargerði 14, 600 Akureyri 3-4 herbergja íbúð á jarðhæð með sjávarútsýni. Forstofa með flísum á gólfi og góðum fataskáp.",
    },
{
        "address" : "Skúlagata 10",
        "zip" : "101",
        "description" : "Skúlagata 10, 101 Reykjavík 3-4 herbergja íbúð á jarðhæð með sjávarútsýni. Forstofa með flísum á gólfi og góðum fataskáp.",
    },
{
        "address" : "Kambsvegur 14",
        "zip" : "104",
        "description" : "Kambsvegur 14, 104 Reykjavík 3-4 herbergja íbúð á jarðhæð með sjávarútsýni. Forstofa með flísum á gólfi og góðum fataskáp.",
    },
{
        "address" : "Ásbúð 40",
        "zip" : "210",
        "description" : "Ásbúð 40, 210 Garðabær 3-4 herbergja íbúð á jarðhæð með sjávarútsýni. Forstofa með flísum á gólfi og góðum fataskáp.",
    },
{
        "address" : "Birkiás 11",
        "zip" : "210",
        "description" : "Vesturgata 73, 210 Garðabær 3-4 herbergja íbúð á jarðhæð með sjávarútsýni. Forstofa með flísum á gólfi og góðum fataskáp.",
    },
]

# Create your views here.
def home(request):
    context = {"apartments" : apartments}
    return render(request, 'forsida/home.html', context)

def um_okkur(request):
    return render(request, 'um_okkur/um_okkur.html', {"title": "Um okkur"})

def starfsmenn(request):
    context = {"base_users" : Base_user.objects.all()}
    return render(request, 'starfsmenn/starfsmenn.html', context)

def soluskra(request):
    return render(request, 'soluskra/soluskra.html', {"title": "Söluskrá"})

def nyskraning(request):
    return render(request, 'nyskraning/nyskraning.html', {"title": "Nýskráning"})