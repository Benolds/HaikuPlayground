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


haiku_inspiration_tiles.swf
---------------------------
Open the .swf file or the .html file to run the "game"

The dictionary of words and frequencies used has been extracted from Jane’ Reichhold’s “A Dictionary of Haiku” http://www.ahapoetry.com/aadoh/adofinde.htm, and can be viewed in Utils/haiku_dictionary_reduced.txt

Code can be examined by opening Utils/main_timeline_code.txt, or by opening the .fla file and viewing the Actions for Frame 1, as well as Tile.as