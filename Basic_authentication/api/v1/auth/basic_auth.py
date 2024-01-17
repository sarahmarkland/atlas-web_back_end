#!/usr/bin/env python3
"""Basic authentication"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """BasicAuth class"""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extract base64 authorization header"""
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]
