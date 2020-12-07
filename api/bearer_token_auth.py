from rest_framework.authentication import TokenAuthentication

"""
Für eine erfolgreiche Authentifizierung, muss der Client den Token im
"Authorization" HTTP header im folgenden Format schicken: Authorization: Bearer tokenKey
 """
class BearerTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'
