# Pathogen!: A Text Based Disease Simulator/Game

## By Sandip S Panesar MD MSc (w200 Summer 2020 Cohort)

### Introduction

This was created as an object-oriented programming assignment for my Python class for the 
UC Berkeley Master of Information and Data Science course. 
The program had to solely utilize class-based objects that interacted with one another. 


I created a semi-educational, text-based simulation entitled “Pathogen!”
The inspiration for this game came from the COVID-19 pandemic occurring in the first half of 2020.
As I am a physician by background, another reason why I wanted to create a health-based,
object-oriented program is that I hope it will serve me as a very rough template of how I may
approach similar situations in my future professional work in medical data science. What
emerged was a simplistic simulation of a pathogen as it interacts with a human host. The
user plays the role of the pathogen, and can choose between either a virus or bacteria. The goal
of the pathogen (player) is to kill the host by invading certain organs, defeating the immune
defenses and then replicating within the organ.

### User Instructions
1. From the command line, enter the folder which the Pathogen.py file is contained, and
run using Python 3. The entire program is contained within the .py file without requiring
any external modules.
2. The player can choose between two classes to play between - a virus or bacteria.
3. Read the intro text, press enter to scroll.
4. The pathogen initially enters the host’s bloodstream (“vasculature”). The vasculature
acts as a central corridor or map that the pathogen can use to travel between the
organs. The user will be presented with a menu of actions - 1. Invade an organ, 2. Quit
or 3. Get health stats. This menu is unique to the vasculature.
5. If “invade an organ is selected” the user will be presented with a list of possible organs to
invade.
6. Once in the organ, you are presented with a series of options. The player must select to
battle before being able to replicate. Once the immune defenses are defeated, the player
can replicate within the organ and damage its health. If the organ’s health is damaged,
the overall body health score is also reduced.
7. You can damage an organ to 0%, but not below this.
8. Once the overall body health is <60%, the host dies and the player wins.
9. From an organ, you can invade an adjacent organ without having to re-enter the
bloodstream, but only a single adjacent organ. To travel to a distant organ, you must use
the bloodstream.
10. There is a health stats option to view health stats of the user, individual organs and
overall body health.
