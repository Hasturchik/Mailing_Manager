from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sendpost.views import ClientViewSet, MailingViewSet, MessageViewSet
from sendpost.admin import admin

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'mailings', MailingViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]