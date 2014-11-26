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

    # Putting these up top for ease of modification if the core language changes.
    variableName = r'[a-zA-Z][a-zA-Z0-9_]*'
    builtins = words(('ARGV',))
    stdlib = words(('CR', 'CRLF', 'EAV', 'FF', 'LF', 'TAB',
        'noun', 'adverb', 'conjunction', 'verb', 'monad', 'dyad',
        'assert', 'boxopen', 'boxxopen', 'clear', 'datatype', 'erase',
        'nameclass', 'nc', 'sign', 'smoutput', 'script', 'scriptd',
        'expand', 'drop', 'fetch', 'pick', 'cutopen', 'do', 'empty',
        'list', 'names', 'namelist', 'nl', 'define', 'each', 'every',
        'inverse', 'leaf', 'rows', 'bind', 'def', 'on',))
    flowControl = words(( 'assert.', 'break.', 'continue.',
        'return.', 'if.', 'do.', 'else.', 'elseif.', 'end.',
        'for.', 'select.', 'case.', 'fcase.', 'throw.', 'try.',
        'catch.', 'catchd.', 'catcht.', 'while.', 'whilst.', ))
    illFormedNumber = r'_{3,}'

    tokens = {
        'root': [
            # Whitespace
            (r'\s+', Text),

            # Shebang script
            (r'#!.*$', Comment.Preproc),

            # Strings
            (r"'", String, 'singlequote'),

            # Comments
            (r'NB\..*?\n', Comment.Single),
            (r'\w\s*Note.*?\n', Comment.Single),
            (r'\s*Note.*?', Comment.Multiline, 'comment'),

            # Definitions
            (r'0\s+:\s*0|noun\s+define\s*$', Name.Label, 'nounDefinition'),
            (r'\b(([1-4]|13)\s+:\s*0)|((adverb|conjunction|dyad|monad|verb)\s+define)\b', Name.Label, 'explicitDefinition'),

            # Keywords
            (r'[abdefijoprstux]\.', Keyword),
            (r'[AcCeEiIjLopr]\:', Keyword),

            # Names
            (builtins, Name.Builtin),
            (flowControl, Name.Label),
            (variableName, Name.Variable),

            # Copula
            (r'=[.:]', Keyword.Declaration),

            # Numbers
            (illFormedNumber, Error),
            (r'_{1,2}?', Number),
            (r'[_0-9]*x', Number),
            (r'[_0-9]+[erj]*[_0-9.]', Number),
            (r'_|[0-9]*.[_0-9]*', Number),

            # Punctuation
            (r'\(', Punctuation, 'parentheses'),

            # Operators
            (r'[`~!@#$%^&*+-=;:"{}\[\]<>\?]', Error),

            # (r'(?s).', Text), # uncomment when this lexer is complete
        ],

        'comment': [
            (r'[^)]', Comment.Multiline),
            (r'^\)', Comment.Multiline, '#pop'),
            (r'[)]', Comment.Multiline),
        ],

        'explicitDefinition': [
            (r'\b[nmuvxy]\b', Name.Decorator),
            include('root'),
            (r'[^)]', Name),
            (r'^\)', Name.Label, '#pop'),
            (r'[)]', Name),
        ],

        'nounDefinition': [
            (r'[^)]', String),
            (r'^\)', Name.Label, '#pop'),
            (r'[)]', String),
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


