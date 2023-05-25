#!/usr/bin/env python3
"""module docs for filtered_logger.py"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    The filter_datum function takes in a list of fields, a redaction string,
    a message string and a separator. It returns the message with all instances
    of the fields replaced by the redaction.

    :param fields:List[str]: Specify the fields that are to be redacted
    :param redaction:str: Replace the fields that are to be redacted
    :param message:str: Pass in the message that is to be filtered
    :param separator:str: Separate the fields in the message
    :return: A string with the message and separator
    """
    for key in fields:
        pattern = key + r'(.*?)' + separator  # all chars btw key & sep
        replacement = key + '=' + redaction + separator
        message = re.sub(pattern, replacement, message)
    return message
