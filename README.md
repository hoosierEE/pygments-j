PYGMENTS-J
==========

This is my attempt to write a Pygments lexer for J language.

Inspired by the lack of syntax highlighting for J on GitHub, as well as the opportunity to contribute to an open-source project and brush up on my Python a bit, this project hopes to make the world a better place.

Get Started with Pygments
-------------------------

There is a great answer [here](http://stackoverflow.com/q/14755721/2037637) with some wondrous resources, specifically the list of other Pygments modules. But we're not even to that point yet. First, install and run Pygments.

* Arch Linux

  `pacman -S python2-pygments`

* OSX

  `pip install pygments`

Verify you have a working Pygments installation by running `pyhi.py` like so:

```sh
python examples/pyhi.py
```

If successful, it should print some HTML-looking stuff:

```html
<div class="highlight"><pre><span class="k">print</span> <span class="s">&quot;Hello World&quot;</span>
</pre></div>
```

Next, we want to write a new lexer for Pygments.

Testing out a new Lexer
-----------------------

This was the trickiest bit of info to find.

First, write a lexer. Mine is `j.py`. Next, `sudo cp` this lexer to Pygments' lexers directory:

```sh
# This example is for OSX
sudo cp j.py /Library/Python/2.7/site-packages/pygments/lexers/
```

Then, tell Pygments about it by re-running the `_mapping.py` file (this step only has to be done *once*):

```sh
cd /Library/Python/2.7/site-packages/pygments/lexers/
python _mapping.py
```

...which will cause `_mapping.py` to re-generate itself, adding the new lexer (`j.py`) to its table of available lexers.

Now our local Pygments is capable of lexing J! Try it out:

```sh
pygmentize -f html -O full -o test.html test.ijs
```

If your lexer is all done you can stop now. Mine isn't, so I use the helper script `updateLexer` after I make changes to `j.py` in this directory.

Useful Links
------------

* [Python regex](https://docs.python.org/dev/library/re.html#regular-expression-syntax)
* [Pygments lexer development](http://pygments.org/docs/lexerdevelopment/)
