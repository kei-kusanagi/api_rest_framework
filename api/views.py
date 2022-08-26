from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "holaaaaa desde api django con SjonRespones"})