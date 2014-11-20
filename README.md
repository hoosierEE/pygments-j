PYGMENTS-J
==========

This is my attempt to write a Pygments lexer for J language.

Inspired by the lack of syntax highlighting for J on GitHub, as well as the opportunity to contribute to an open-source project and brush up on my Python a bit, this project hopes to make the world a better place.

Get Started with Pygments
-------------------------

There is a great answer [here](http://stackoverflow.com/q/14755721/2037637) with some wondrous resources, specifically the list of other Pygments modules. But we're not even to that point yet. First, install and run Pygments.

* Arch Linux
  `pacman -S python-pygments`
* OSX
  `pip install pygments`

Verify you have a working Pygments installation by running `pyhi.py` like so:

```sh
python < pyhi.py
```

If successful, it should print some HTML-looking stuff:

```html
<div class="highlight"><pre><span class="k">print</span> <span class="s">&quot;Hello World&quot;</span>
</pre></div>
```

Next, we want to write a new lexer for Pygments.


Here is some example output:

```html
<div class="highlight"><pre><span class="err">#!/usr/bin/jconsole</span>

<span class="c1">NB. A Script for testing Pygments highlighting for J language</span>

<span class="c1">NB. Here is another comment.</span>

<span class="err">echo</span> <span class="err">1</span> <span class="err">2</span> <span class="err">3</span>
<span class="err">exit&#39;</span><span class="c1">&#39;</span>

<span class="c1">Note some stuff</span>
<span class="err">blah</span> <span class="err">blah</span>
<span class="err">)</span>
</pre></div>
```
