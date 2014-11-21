"""
pygments.lexers.j
~~~~~~~~~~~~~~~~~

Lexer for the J programming language.

"""

import re
from pygments.lexer import RegexLexer, bygroups, default, using, include
from pygments.token import *
#from pygments.token import Comment, Operator, Name, String, Number, Keyword

__all__ = ['JLexer']

class JLexer(RegexLexer):
    """
    For `J <http://jsoftware.com/>`_ source code.

    """

    name = 'J'
    aliases = ['j']
    filenames = ['*.ijs']
    mimetypes = ['application/x-j', 'text/plain']

    tokens = {
        'root': [
            (r'#!.*$', Comment.Preproc),
            (r'NB\..*?\n', Comment.Single),
            (r'Note.*', Comment.Multiline, 'comment'),
            (r'\(', Keyword, 'paren'),
            # (r'(?s).', Text), # uncomment when this lexer is done
        ],
        'comment': [
            (r'[^)]', Comment.Multiline),
            (r'Note.*?', Comment.Multiline, '#push'),
            (r'^\)', Comment.Multiline, '#pop'),
        ],
        'paren': [
            (r'\)', Keyword, '#pop'),
            include('root'),
        ],
    }

