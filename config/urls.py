from django.http import HttpResponse


def home(request):
    return HttpResponse("Todo Backend is Running!")


urlpatterns = [
    path('', home),  # Add this line for the root path
    path('admin/', admin.site.urls),
    path('api/', include('todos.urls')),
]
