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

