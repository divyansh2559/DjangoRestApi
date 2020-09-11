from registerapi.viewsets import usersViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users',usersViewset)
