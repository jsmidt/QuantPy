QuantPy
==========

A framework for quantitative finance in python.

**Disclaimer:** This is a *very* alpha project.  It is not ready to be used and
won't be for a while.  In fact, the author is still very much learning what
such a framework needs to entail.  However, if you consider yourself a helpful
soul contributions of any type are more then welcome. Thanks!


Some current capabilities:
   * Portfolio class that can import daily returns from Yahoo.
   * Calculation of optimal weights for Sharpe ratio and efficient frontier
   * Bare bones event profiler

Documentation:
--------------

The main documentation can be read at [Read The Docs](https://quantpy.readthedocs.org/en/latest/).  Please start their for more information.

Contributions Welcome.
----------------------

Any and all contributions for the project are welcome whether they be feature
requests, bug reports, contributions to documentation, or patches for new
features, bug fixes of other improvements.  Just [fork the
repo](https://help.github.com/articles/fork-a-repo), add some content and [make
a pull request] (https://help.github.com/articles/be-social).  If you are new
to Git [this tutorial](http://learn.github.com/p/intro.html) is nice for further
details.

Also, just downloading the code and providing feedback is also extremely
useful. Submit your feedback to the [issues page
here](https://github.com/jsmidt/QuantPy/issues?state=open).  Thanks in advance.

You may also join us at #quantpy on irc.freenode.net.

How To Install.
---------------

QuantPy may be downloaded from GitHub as::

  > git clone https://github.com/jsmidt/QuantPy.git

To install QuantPy type::

  > cd QuantPy
  > python setup.py install 

The prerequisites for Quantpy are:

* pandas (> 0.10.0)
* matplotlib (> 0.1.0)
* PyGObject (> 3.8.2, only needed for GUI)

Why Python?
-----------

Python is popular, easy to use, cross-platform, contains many helpful
numerical, statistical and visualization libraries and in reality can be made
as fast as C/C++ through Cython extensions. I know of no other language that
meets *all* of these requirements. 

Why BSD license?
----------------

It is a desire that QuantPy is as useful as possible, including for those who
want to incorporate QuantPy into their proprietary software. The BSD license is
an open source license that permits this. Please see the attached LICENSE file
and http://www.linfo.org/bsdlicense.html for more information which states "Due
to the extremely minimal restrictions of BSD-style licenses, software released
under such licenses can be freely modified and used in proprietary (i.e.,
commercial) software for which the source code is kept secret."

Why Git and GitHub?
-------------------

There are a few great distributed revision control systems. Git was chosen for
the simple reason that git was designed with the ability to create many
anonymous untracked branches where code can be pushed and pulled from without
revealing the anonymous history.  We feel this design choice is important for
entities with proprietary code who want to make contributions but keep their
branches anonymous.  Github was chosen because it seems to give the most user
friendly git experience across all platforms: Windows, Mac and Linux. 


Is Non-Commercial/Proprietary Use allowed?
------------------------------------------

Yes.  Though this is an open source project, it was understood from day one
that there may be a need to incorporate QuantPy into proprietary software. The
above sections regarding the BSD licence and the use of Git discuss how we
have addressed these concerns.  We hope, however, entities repay the generosity
by submitting patches for new features, bug fixes, and other improvements. 


With that said, I hope you very much enjoy Quantpy.  I hope it meets your
needs, makes you happy and that your retrun the favor through the types of
contributions mentioned above. 
