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
            (r'\s+', Text),
            (r'[_0-9][_0-9.a-zA-Z]*', Number),
            (r'[a-z]\w+', Name),
            (r'[AcCeEiIjLopr]\.', Keyword),
            (words(('if.', 'then.', 'else.', 'end.', 'while.', 'do.', 'echo')), Keyword.Reserved),
            (r'#!.*$', Comment.Preproc),
            (r'=[.:]', Keyword.Declaration),
            (r'[~!@#$%^&*+-=;:"{}\[\]<>\?]', Operator),
            (r'NB\..*?\n', Comment.Single),
            (r'Note.*', Comment.Multiline, 'comment'),
            (r'\(', Punctuation, 'parentheses'),
            (r"'", String, 'singlequote'),
            # (r'(?s).', Text), # uncomment when this lexer is complete
        ],
        'comment': [
            (r'[^)]', Comment.Multiline),
            (r'Note.*?', Comment.Multiline, '#push'),
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

