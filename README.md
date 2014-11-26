PYGMENTS-J
==========

A [J](http://jsoftware.com) lexer for [pygments](http://pygments.org)

> Work in progress

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



Workflow
--------

The [instructions](http://pygments.org/docs/lexerdevelopment/) did not work for me, so this part was tricky to suss out.


### STEP 1: Write a Lexer

First, write a lexer. Mine is `j.py`.


### STEP 2: Put it in `pygments/lexers/`

```sh
# This example is for OSX
sudo cp j.py /Library/Python/2.7/site-packages/pygments/lexers/
```


### STEP 3: Regenerate mapping file
Then, tell Pygments about it by re-running the `_mapping.py` file (this step only has to be done *once*):

```sh
cd /Library/Python/2.7/site-packages/pygments/lexers/
python _mapping.py
```

`_mapping.py` will re-generate itself, adding the new lexer (`j.py`) to its table of available lexers.

Now our local Pygments is capable of lexing J! We can try it out:

```sh
pygmentize -f html -O full -o test.html test.ijs
```


### STEP 4: Edit and test, edit and test...
If our lexer is all done we can stop now. Mine isn't, so after updating `j.py` in this directory, I run my helper script:

```sh
./updateLexer
```

> ProTip: you don't even have to leave Vim:
> ```viml
> :silent execute "!./updateLexer" | redraw!
> ```

And then open `output/test.html` in my browser and refresh to see the changes.



Useful Links
------------

* [Python regex](https://docs.python.org/2.7/library/re.html#)
* [Pygments lexer development](http://pygments.org/docs/lexerdevelopment/)
