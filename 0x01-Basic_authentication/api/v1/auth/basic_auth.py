#!/usr/bin/env python3
"""Basic authentication class handler"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """inherits from Auth"""

    def extract_base64_authorization_header(self, authorization_header: str)\
            -> str:
        '''returns the Base64 part of the Authorization header'''
        if authorization_header is None\
                or (not isinstance(authorization_header, str))\
                or (not authorization_header.startswith("Basic ")):
            return None
        else:
            return authorization_header.split(" ")[1]