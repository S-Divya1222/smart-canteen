from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Redirect default /admin/ path to custom Admin Order Management page
    path("admin/", RedirectView.as_view(pattern_name="admin_orders", permanent=False)),

    path("", include("canteen.urls")),

    # Django login/logout URLs
    path("accounts/", include("django.contrib.auth.urls")),

    # Serve media files reliably in both local and production
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )