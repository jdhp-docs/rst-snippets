.. _about:

About this demo
===============

-  `Source code <https://github.com/jdhp-docs/rst-snippets>`__
-  `Online version <http://www.jdhp.org/docs/rst_snippets/rst_snippets.html>`__


Online documentation
====================

See:

- http://docutils.sourceforge.net/rst.html
- http://docutils.sourceforge.net/docs/user/rst/quickstart.html
- http://docutils.sourceforge.net/docs/user/rst/quickref.html
- http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt
- https://aful.org/wikis/interop/ReStructuredText
- https://en.wikipedia.org/wiki/ReStructuredText
- https://docs.python.org/3.1/documenting/rest.html
- https://docs.python.org/devguide/documenting.html
- http://docutils.sourceforge.net/docs/user/links.html


Tools (on Debian Gnu/Linux)
===========================

Docutils
--------

The main distribution of reStructuredText is the python-docutils package. It
contains several conversion tools:

- rst2html
- rst2latex
- rst2man
- rst2odt
- rst2s5 (S5, a Simple Standards-based Slide Show System)
- rst2beamer (generates a LaTeX source that uses the Beamer document class) http://docutils.sourceforge.net/sandbox/rst2beamer/

Other tools
-----------

rst2pdf
~~~~~~~

Usage::

  rst2pdf test.rst

Pandoc
~~~~~~

Pandoc is a document converter that can write Markdown, reStructuredText, HTML,
LaTeX, RTF, DocBook XML, and S5::

   pandoc -o output.html input.rst

Pandoc can be used to convert a Markdown document in reStructuredText::

   pandoc -o output.rst input.md

More tools
~~~~~~~~~~

More tools are listed at http://docutils.sourceforge.net/docs/user/links.html

Emphasis
========

*Emphasis* (aka italics)

**Strong emphasis** (aka bold)

Horizontal rule
===============

Hello

----

World

Blockquotes
===========

As Descartes said

    Cogito, ergo sum

Literal blocks
==============

As Descartes said::

    Cogito, ergo sum

Lists
=====

Unordered lists
---------------

-  item 1
-  item 2
-  item 3

-  item 1
-  item 2
-  item 3

Nested unordered lists
----------------------

-  item 1

   -  item 1.1
   -  item 1.2
   -  item 1.3

-  item 2

   -  item 2.1
   -  item 2.2
   -  item 2.3

-  item 3

   -  item 3.1
   -  item 3.2
   -  item 3.3

Ordered lists
-------------

1. item 1
2. item 2
3. item 3

Definition lists
----------------

Word1
  Definition of word1

*Word2*
  Definition of word2

Nested ordered lists
--------------------

1. item 1

   1. item 1.1
   2. item 1.2
   3. item 1.3

2. item 2

   1. item 2.1
   2. item 2.2
   3. item 2.3

3. item 3

   1. item 3.1
   2. item 3.2
   3. item 3.3

Nested ordered and unordered lists
----------------------------------

1. item 1

   1. item 1.1
   2. item 1.2
   3. item 1.3

2. item 2

   -  item 2.1
   -  item 2.2
   -  item 2.3

3. item 3

   -  item 3.1
   -  item 3.2
   -  item 3.3

Links
=====

External links
--------------

`JDHP <http://www.jdhp.org>`__

Internal links and anchors
--------------------------

about_

`about`_

Images
======

.. TODO: fails with PDF generator (don't know SVG format!)

SVG images
----------

.. figure:: figs/logos/python/python.svg
   :alt: Logo

PNG images
----------

.. figure:: figs/plot2d.py.png
   :alt: Plot

Maths and LaTeX
===============

.. TODO: fails with PDF generator

Basics
------

See http://sphinx-doc.org/latest/ext/math.html

When :math:`a \ne 0`, there are two solutions to :math:`ax^2 + bx + c = 0` and they are
:math:`x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}.`

.. math::
    
    (a + b)^2 = a^2 + 2ab + b^2

    (a - b)^2 = a^2 - 2ab + b^2

.. math::

    n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k

Inline maths with :math:`\LaTeX` : :math:`x \lt y`

.. math::

    \int_a^b f(x)dx

    V(x) = \max_{a \in \Gamma (x) } \{ F(x,a) + \beta V(T(x,a)) \}

Equation array
--------------

.. math::

    \begin{eqnarray*}
        \mbox{Expectation of N} & = & \sum_{i=1}^{n} \mathbb{E}(Z_i) \\
                                & = & \sum_{i=1}^{n} \frac{\gamma}{d^{\beta/2}} \frac{ c(d)^\beta }{i^{\alpha\beta}} \\
                                & = & \frac{\gamma}{d^{\beta/2}} c(d)^\beta \sum_{i=1}^{n} \frac{1}{i^{\alpha\beta}} \\
                                & = & z
    \end{eqnarray*}

Arrays
------

.. math::

    \begin{array}{cc}
        a & b \\
        c & c
    \end{array}

Matrices
--------

.. math::

    A= \begin{pmatrix}
        a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
        a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
        \vdots  & \vdots  & \ddots & \vdots  \\
        a_{m,1} & a_{m,2} & \cdots & a_{m,n}
    \end{pmatrix}

    A= \begin{bmatrix}
        a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
        a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
        \vdots  & \vdots  & \ddots & \vdots  \\
        a_{m,1} & a_{m,2} & \cdots & a_{m,n}
    \end{bmatrix}

Mathematical programming
------------------------

.. math::

    \begin{align}
        \max        & \quad z = 4 x_1 + 7 x_2    \notag \\
        \text{s.t.} & \quad 3 x_1 + 5 x_2 \leq 6 \label{constraint1}\\
                    & \quad   x_1 + 2 x_2 \leq 8 \label{constraint2}\\
                    & \quad   x_1, x_2 \geq 0    \notag
    \end{align}

Systems of equation array
-------------------------

.. math::

    f(n) = \left\{
        \begin{array}{ll}
            n/2      & \text{if $n$ is even} \\
            -(n+1)/2 & \text{if $n$ is odd}
        \end{array}
    \right.

:math:`\LaTeX` fonts
--------------------

mathbb
~~~~~~

.. math::

    \mathbb{ABCDEFGHIJKLMNOPQRSTUVWXYZ}

mathbf
~~~~~~

.. math::

    \mathbf{ABCDEFGHIJKLMNOPQRSTUVWXYZ}

    \mathbf{abcdefghijklmnopqrstuvwxyz}

mathtt
~~~~~~

.. math::

    \mathtt{ABCDEFGHIJKLMNOPQRSTUVWXYZ}

    \mathtt{abcdefghijklmnopqrstuvwxyz}

mathrm
~~~~~~

.. math::

    \mathrm{ABCDEFGHIJKLMNOPQRSTUVWXYZ}

    \mathrm{abcdefghijklmnopqrstuvwxyz}

mathsf
~~~~~~

.. math::

    \mathsf{ABCDEFGHIJKLMNOPQRSTUVWXYZ}

    \mathsf{abcdefghijklmnopqrstuvwxyz}

mathcal
~~~~~~~

.. math::

    \mathcal{ABCDEFGHIJKLMNOPQRSTUVWXYZ}

    \mathcal{abcdefghijklmnopqrstuvwxyz}

mathfrak
~~~~~~~~

.. math::

    \mathfrak{ABCDEFGHIJKLMNOPQRSTUVWXYZ}

    \mathfrak{abcdefghijklmnopqrstuvwxyz}

Algorithms
==========

PNG
---

.. figure:: figs/algo.tex.png
   :align: center
   :width: 600px
   :alt: Plot

SVG
---

.. figure:: figs/algo.tex.svg
   :align: center
   :width: 600px
   :alt: Plot

Source code
===========

Python
------

.. code:: python

    for text in ("Hello", "world"):
        print(text)

Shell
-----

.. code:: sh

    echo "Hello world"

C programming language
----------------------

.. code:: c

    printf("%s", "Hello world\n");

Inline code
-----------

Inline without syntax highlighting (generic code) :code:`print("hello")`.

.. See http://stackoverflow.com/questions/10870719/inline-code-highlighting-in-restructuredtext

.. role:: python(code)
   :language: python

Inline :python:`print("hello")`.

Inline without syntax highlighting (generic code) :code:`print("hello")`.

Unformat
========

This is an example of ``<html>`` tag.

::

    <p>Hello</p>
    <p>World</p>

Verbatim (HTML)
===============

.. raw:: html

   <pre>

            .--.
           |o_o |
           |:_/ |
          //   \ \
         (|     | )
         /'\_   _/`\
         \___)=(___/

   </pre>

Tables
======

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| *(1,1)*    | **(1,2)**  | (1,3)     |
+------------+------------+-----------+
| (2,1)      | Multi-column cell      |
+------------+------------+-----------+
| (3,1)      | Multi-row  | (3,3)     |
+------------+ cell       +-----------+
| (4,1)      |            | (4,3)     |
+------------+------------+-----------+

Inline HTML
===========

.. raw:: html

   <dl>
       <dt>

Foo

.. raw:: html

       </dt>
       <dd>

blablabla

.. raw:: html

       </dd>


.. raw:: html

   </dl>

