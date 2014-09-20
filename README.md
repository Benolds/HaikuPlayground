Haiku Playground
================

A series of playful code experiments relating to the art of Haikus.

Contents
========

oulipian_lipogram_haiku_generator.py
------------------------------------
Inspired my the mid-20th century Oulipo movement, this generates Haiku poems using a dictionary of the most frequent words in the English language, with the additional constraint of not using a specified vowel in any words.

Approximates the syllable decomposition of each word using Ned Batchelder's 2007 hyphenation implementation, based on Frank Liang's algorithm.

haiku_evolution.py
------------------
A brainstorming tool. A collaboration between man and machine. The prosthetic mind. Randomly generates alternate versions of each haiku line, which you can selectively choose to be passed on to the next generation. In this manner, the user directs the evolution of the Haiku, but all text is generated randomly by the program.