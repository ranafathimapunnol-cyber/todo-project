from django.http import JsonResponse


def home(request):
    return JsonResponse({"message": "Welcome to the Todo API. Go to /api/todos/ to see data."})


urlpatterns = [
    path('', home),  # This fixes the 404 on the main page
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),
]
