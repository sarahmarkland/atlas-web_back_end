#!/usr/bin/env python3
"""Regex-ing"""

import re


def filter_datum(fields, redaction, message, separator):
    """returns the log message obfuscated"""
    if not fields or not isinstance(fields, list):
        return
    if not separator or not isinstance(separator, str):
        return
    if not message or not isinstance(message, str):
        return
    if not redaction or not isinstance(redaction, str):
        return

    for field in fields:
        message = re.sub(field + "=.*?" + separator,
                         field + "=" + redaction + separator, message)
    return message
