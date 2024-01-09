from rest_framework.authentication import TokenAuthentication as BaseTokenauth

class TokenAuthentication(BaseTokenauth):
    keyword='Bearer'