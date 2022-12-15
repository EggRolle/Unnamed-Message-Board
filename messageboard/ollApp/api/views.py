from django.http import JsonResponse

def getRoutes(request):
    routes = [
        'get /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]

    return JsonResponse(routes, safe=False)
    