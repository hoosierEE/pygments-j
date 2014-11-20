"""
    Pygments Lexer for J language
"""

import re
from pygments.lexer import RegexLexer
# from pygments.lexer import RegexLexer, bygroups, using, include
from pygments.token import *
#from pygments.token import Comment, Operator, Name, String, Number, Keyword

__all__ = ['JLexer']

class JLexer(RegexLexer):
    name = 'J'
    aliases = ['j']
    filenames = ['*.ijs']
    mimetypes = ['text/plain']

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'NB\..*?\n', Comment.Single),
            (r'.\s+Note.*?\n', Comment.Single),
            (r'^Note.*?\n\)', Comment.Multiline),
        ]
    }

