from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Kinolar",
        default_version="v1",
        description="Api documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mirzohidxudayberganov27@gmail.com"),
        license=openapi.License(name="DATA UNION"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
