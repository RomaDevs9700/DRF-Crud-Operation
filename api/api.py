from rest_framework import routers
from library import views

router = routers.DefaultRouter()
router.register(r"books", views.BookViewSet, basename="books")
router.register(r"lib-users", views.LibUserViewSet)
router.register(r"rented-books", views.RentBookViewSet)

