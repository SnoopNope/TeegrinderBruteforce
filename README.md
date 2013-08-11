TeegrinderBruteforce
====================
[Teegrinder](http://www.designbyhumans.com/TeeGrinder/) is a little service by the online store [Design By Humans](http://www.designbyhumans.com/) that allows you to buy 3 randomly selected shirts for a discounted price of USD$30. The shirts come from a limited pool, so not all the shirts on the store are available for grinding.

It's a good deal, so the drawback here is that the shirts are selected at random, and it can (read: will) take a long time to get 2, maybe 3 shirts that you want. This is where this script comes in.

First off, let me say that original credit for the method goes to Sawboo from YouTube ([video](http://www.youtube.com/watch?v=SGiDvmCYASE)). I updated the script to work on Python versions below 2.7.5. Also made the output a little neater. Mostly still the same script though.

Anyway, what `teegrinder.py` does is simply constantly send grind requests to the website and check the responses for the shirts that you select. Once the required number of shirts is matched, the teegrinder bundle is added to your cart.

Requirements
=======
* Python
* A tiny bit of knowledge of Python

Instructions
=======
Full instructions are found in the script's comments. You'll need to provide some variables, like your browser cookies, user agent, and a list of the shirts you want.

