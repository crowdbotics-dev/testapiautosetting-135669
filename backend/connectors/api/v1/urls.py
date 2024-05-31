from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors135669ViewSet

router = DefaultRouter()
router.register(
    "testconnectors135669", Testconnectors135669ViewSet, basename="testconnectors135669"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
