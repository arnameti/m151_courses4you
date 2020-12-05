from rest_framework.permissions import BasePermission


# Gibt ein True zurück, wenn es ein post-request oder der Benutzer authentifiziert ist, ansonsten wird False zurückgegeben.
class IsAuthenticatedOrPostOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST' or request.user and request.user.is_authenticated:
            return True
        else:
            return False
