"""
pygments.lexers.j
~~~~~~~~~~~~~~~~~

Lexer for the J programming language.

"""

import re
from pygments.lexer import RegexLexer, words, include
from pygments.token import Comment, Error, Keyword, Name, Number, Operator, Punctuation, String, Text

__all__ = ['JLexer']

class JLexer(RegexLexer):
    """
    For `J <http://jsoftware.com/>`_ source code.

    """

    name = 'J'
    aliases = ['j']
    filenames = ['*.ijs']

    variableName = r'[a-zA-Z][a-zA-Z0-9_]*'

    tokens = {
        'root': [
            # Whitespace
            (r'\s+', Text),

            # Shebang script
            (r'#!.*$', Comment.Preproc),

            # Strings
            (r"'", String, 'singlequote'),
            (r'NB\..*?\n', Comment.Single),
            (r'Note.*?\n', Comment.Multiline, 'comment'),

            # Definitions
            (r'0\s+:\s*0|noun\s+define', String, 'noundef'),
            (r'\b(([1-4]|13)\s+:\s*0)|((adverb|conjunction|dyad|monad|verb)\s+define)\b', Name, 'explicitDefinition'),

            # Keywords
            (r'[AcCeEiIjLopr]\.', Keyword),
            (r'[AcCeEiIjLopr]\:', Keyword),

            # Names
            (words(('ARGV', 'BINPATH', 'CR', 'CRLF', 'DEL', 'EAV',
                'EMPTY', 'FF', 'LF', 'LF2', 'TAB',)), Name.Builtin),
            (words(( 'assert.', 'break.', 'continue.', 'return.',
                'if.', 'do.', 'else.', 'elseif.', 'end.',
                'for.', 'select.', 'case.', 'fcase.', 'throw.',
                'try.', 'catch.', 'catchd.', 'catcht.',
                'while.', 'whilst.', )), Name.Label),
            (variableName, Name.Variable),

            # Copula
            (r'=[.:]', Keyword.Declaration),

            # Numbers
            (r'_{3,}', Error),
            (r'_{1,2}?', Name.Decorator),
            (r'_|[0-9]*\..x', Error),
            (r'[_0-9]*x', Name.Decorator),
            (r'[_0-9]+[erj]*[_0-9.]', Name.Decorator),
            (r'[^0-9]*\.[0-9]*', Error),
            (r'_|[0-9]*.[_0-9]*', Name.Decorator),

            # Punctuation
            (r'\(', Punctuation, 'parentheses'),

            # Operators
            (r'[\\\|`~!@#$%^&*+-=;:"{}\[\]<>\?]', Keyword),

            # (r'(?s).', Text), # uncomment when this lexer is complete
        ],

        'noundef': [
            (r'[^)]', String),
            (r'^\)', String, '#pop'),
            (r'[)]', String),
        ],

        'comment': [
            (r'[^)]', Comment.Multiline),
            (r'^\)', Comment.Multiline, '#pop'),
            (r'[)]', Comment.Multiline),
        ],

        'parentheses': [
            (r'\)', Punctuation, '#pop'),
            include('root'),
        ],

        'explicitDefinition': [
            include('root'),
            (r'\b[nmuvxy]\b', Name.Decorator),
            (r'[^)]', Name),
            (r'^\)', Name, '#pop'),
            (r'[)]', Name),
        ],

        'singlequote': [
            (r"[^']", String),
            (r"''", String),
            (r"'", String, '#pop'),
        ],
    }


