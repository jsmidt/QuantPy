.. _getting_started:


***************
Getting started
***************

Welcome to QuantPy.

**Disclaimer:** This is a *very* alpha project.  It is not ready to be used and
won't be for a while.  In fact, the author is still very much learning what
such a framework needs to entail.  However, if you consider yourself a helpful
soul contributions of any type are more then welcome. Thanks!


Some current capabilities:
   * Portfolio class that can import daily returns from Yahoo.
   * Calculation of optimal weights for Sharpe ratio and efficient frontier
   * Bare bones event profiler

Contributions Welcome.
=========================

Any and all contributions for the project are welcome whether they be feature
requests, bug reports, contributions to documentation, or patches for new
features, bug fixes of other improvements.  Just [fork the
repo](https://help.github.com/articles/fork-a-repo), add some content and [make
a pull request] (https://help.github.com/articles/be-social). If you are new to
 Git [this tutorial](http://learn.github.com/p/intro.html) is nice for futher details.


Also, just downloading the code and providing feedback is also extremely
useful. Sumbit your feedback to the [issues page
here](https://github.com/jsmidt/QuantPy/issues?state=open).  Thanks in advance.


.. _installing-docdir:

Installing QuntPy
=============================

QuantPy may be downloaded from GitHub as::

  > git clone https://github.com/jsmidt/QuantPy.git

To install QuantPy type::

  > cd QuantPy
  > python setup.py install 

The prerequisites for Quantpy are:

* pandas (> 0.10.0) 
* matplotlib (> 0.1.0) 


.. _example-scripts-highlighting-functionality:

Example Scripts Highlighting Functionality
==============================================

Import any portfolio and plot the returns. 
----------------------------------------------

The example script imports a portfolio of stocks and plots the normalized retuns:

.. plot:: ../examples/nplot_ex.py
   :include-source:

Calculate the weighting that gives minimum variance.
------------------------------------------------------

QuantPy can tell you the portfolio weighting that will give you the minimum
variance. (Max sharpe ratio)  This is illustrated in the
min_variance_returns_ex.py script where you compare how your portfolio would
have changed if you bought an equal number of all stocks in the portfolio
versus used optimal sharpe ratio weighting for the same return.

.. plot:: ../examples/min_variance_returns_ex.py
   :include-source:

Plot the Efficient Frontier.
-------------------------------

We can plot the entire efficient frontier as done in
efficient_frontier_plot_ex.py.  This is defined as followed: you tell me what
returns you want and this will tell you the weighting that will generate those
returns with minimum variance.  The relation or risk to return  for such a
weighting is plotted in efficient_frontier.png.  The line showing the optimal
return for risk (optimal share ratio) is also plotted.

.. plot:: ../examples/efficient_frontier_plot_ex.py
   :include-source:

Using an Event Profiler
-------------------------

Event profiler allows you to track what happens to a stock price after
historical events.  Tell me any event, like an EMA cross, and this will plot
how the price historically has changed with such an event with error bars.
This helps us find statistically meaningful events.  

Below is a bare bones version of this demonstrated by running event_ex.py.  It
just asks what happens to the price after it goes up at least $1.  As the plot
event_ex.png shows, nothing meaningful. Notice you must create your own "truth function" describing your event.

.. plot:: ../examples/event_ex.py
   :include-source:

Thanks Again!
=================

We want to thank you for trying out QuantPy.  Any contributions are again very appreciated.

