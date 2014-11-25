"""
pygments.lexers.j
~~~~~~~~~~~~~~~~~

Lexer for the J programming language.

"""

import re
from pygments.lexer import RegexLexer, words, include
from pygments.token import Comment, Keyword, Name, Number, Operator, Punctuation, String, Text

__all__ = ['JLexer']

class JLexer(RegexLexer):
    """
    For `J <http://jsoftware.com/>`_ source code.

    """

    name = 'J'
    aliases = ['j']
    filenames = ['*.ijs']

    tokens = {
        'root': [
            # Whitespace
            (r'\s+', Text),
            # Strings
            (r"'", String, 'singlequote'),
# Keywords
            (r'[AcCeEiIjLopr]\.', Keyword),
            (r'[AcCeEiIjLopr]\:', Keyword),
# Names
            (r'[a-zA-Z]\w+', Name),
            (words(('if.', 'then.', 'else.', 'end.', 'while.', 'do.', 'echo')), Keyword.Reserved),
            (r'#!.*$', Comment.Preproc),
            (r'0 :0.*', Comment.Multiline, 'comment'),
# Numbers
            (r'[_0-9][_0-9.a-zA-Z]*', Number),
            (r'=[.:]', Keyword.Declaration),
# Operators
            (r'[~!@#$%^&*+-=;:"{}\[\]<>\?]', Operator),
            (r'NB\..*?\n', Comment.Single),
# Punctuation
            (r'\(', Punctuation, 'parentheses'),
            # (r'(?s).', Text), # uncomment when this lexer is complete
        ],
        'comment': [
            (r'^[^)]', Comment.Multiline),
            (r'^\)', Comment.Multiline, '#pop'),
        ],
        'parentheses': [
            (r'\)', Punctuation, '#pop'),
            include('root'),
        ],
        'singlequote': [
            (r"[^']", String),
            (r"''", String),
            (r"'", String, '#pop'),
        ],
    }


