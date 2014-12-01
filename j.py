"""
pygments.lexers.j
~~~~~~~~~~~~~~~~~

Lexer for the J programming language.

"""

import re
from pygments.lexer import bygroups, RegexLexer, words, include
from pygments.token import Comment, Error, Keyword, Name, Number, Operator, Punctuation, String, Text

__all__ = ['JLexer']

class JLexer(RegexLexer):
    """
    For `J <http://jsoftware.com/>`_ source code.

    """

    name = 'J'
    aliases = ['j']
    filenames = ['*.ijs']

    validName = r'\b[a-zA-Z]\w*'

    tokens = {
        'root': [
            # Shebang script
            (r'#!.*$', Comment.Preproc),

            # Comments
            (r'NB\..*', Comment.Single),
            (r'\n+\s*Note', Comment.Multiline, 'comment'),
            (r'\s*Note.*', Comment.Single),

            # Whitespace
            (r'\s+', Text),

            # Strings
            (r"'", String, 'singlequote'),

            # Definitions
            (r'0\s+:\s*0|noun\s+define\s*$', Name.Entity, 'nounDefinition'),
            (r'\b(([1-4]|13)\s+:\s*0)|((adverb|conjunction|dyad|monad|verb)\s+define)\b', Name.Function, 'explicitDefinition'),

            # Flow Control
            (words(( 'for_', 'goto_', 'label_'), suffix=validName+'\.'), Name.Label),
            (words(
                'assert', 'break', 'case', 'catch', 'catchd',
                'catcht', 'continue', 'do', 'else', 'elseif',
                'end', 'fcase', 'for', 'if', 'return',
                'select', 'throw', 'try', 'while', 'whilst',
                ), suffix='\.'), Name.Label),

            # Variable Names
            (validName, Name.Variable),

            # Standard Library
            (words(
                'ARGV', 'CR', 'CRLF', 'DEL', 'Debug',
                'EAV', 'EMPTY', 'FF', 'JVERSION', 'LF',
                'LF2', 'Note', 'TAB', 'alpha17', 'alpha27',
                'apply', 'bind', 'bind', 'boxopen', 'boxopen',
                'boxxopen', 'boxxopen', 'bx', 'clear', 'clear',
                'cutLF', 'cutopen', 'cutopen', 'datatype', 'datatype',
                'def', 'def', 'dfh', 'drop', 'drop',
                'each', 'each', 'echo', 'empty', 'empty',
                'erase', 'erase', 'every', 'every', 'evtloop',
                'exit', 'expand', 'expand', 'fetch', 'fetch',
                'file2url', 'fixdotdot', 'fliprgb', 'getargs', 'getenv',
                'hfd', 'inv', 'inverse', 'inverse', 'iospath',
                'isatty', 'isutf8', 'items', 'leaf', 'leaf',
                'list', 'list', 'nameclass', 'nameclass', 'namelist',
                'namelist', 'names', 'names', 'nc', 'nc',
                'nl', 'nl', 'on', 'on', 'pick',
                'pick', 'rows', 'rows', 'script', 'script',
                'scriptd', 'scriptd', 'sign', 'sign', 'sminfo',
                'smoutput', 'smoutput', 'sort', 'split', 'stderr',
                'stdin', 'stdout', 'table', 'take', 'timespacex',
                'timex', 'tmoutput', 'toCRLF', 'toHOST', 'toJ',
                'tolower', 'toupper', 'type', 'ucp', 'ucpcount',
                'usleep', 'utf8', 'uucp',
                ), Name.Builtin),

            # Copula
            (r'=[.:]', Operator),

            # Builtins
            (r'[-=+*$%@!~`^&";:.,<>{}\[\]\\|/]', Operator),

            # Short Keywords
            (r'[abCdDeEfHiIjLMoprtT]\.',  Keyword.Reserved),
            (r'[aDiLpqsStux]\:', Keyword.Reserved),
            (r'(_[0-9])\:', Keyword.Constant),

            # Parens
            (r'\(', Punctuation, 'parentheses'),

            # Numbers
            include('numbers'),

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

        'numbers': [
            (r'_{3,}', Error),
            (r'\b_{1,2}\b', Number),
            (r'_?\d+(\s*[ejr]\s*)?_?\d+', Number),
            (r'_?\d+\.(?=\d+)', Number.Float),
            (r'_?\d+x?', Number.Integer.Long),
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


