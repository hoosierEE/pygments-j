from pygments import highlight
from pygments.lexers import JLexer
from pygments.formatters import HtmlFormatter

code = 'echo 1 2 3 NB. a comment'
print (highlight(code, JLexer(), HtmlFormatter()))
