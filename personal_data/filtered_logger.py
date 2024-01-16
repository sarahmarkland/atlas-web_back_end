#!/usr/bin/env python3
"""Regex-ing"""

import logging
import re
import typing


def filter_datum(fields: typing.List[str], redaction: str, message: str,
                 separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        message = re.sub(field + "=.*?" + separator,
                         field + "=" + redaction + separator, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: typing.List[str] = None):
        """
        Initialize the RedactingFormatter.

        Args:
            fields (list): List of strings representing fields to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record.

        Args:
            record (logging.LogRecord): Log record to format.

        Returns:
            str: Formatted log message.
        """
        message = super(RedactingFormatter, self).format(record)

        if self.fields:
            message = filter_datum(self.fields, self.REDACTION, message,
                                   self.SEPARATOR)
        return message
