# My Advent of Code 2021 <a name="top"></a>
[Find all the detailed official puzzle descriptions &#8594;](https://adventofcode.com/2021)
<!--
Using the utility library [advent-of-code-data](https://github.com/wimglenn/advent-of-code-data).
-->

<span style="font-size:large">
<p align="center">

<span style="color:green">
.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.
</span>

<span style="color:red">
*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*
</span>

<span style="color:green">
.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.
</span>

</p>


<p align="center">

||||||
|:------:|:------:|:------:|:------:|:------:|
|    [Day 1](#day-1)    |    [Day 2](#day-2)   |    [Day 3](#day-3)    |    [Day 4](#day-4)    |    [Day 5](#day-5)    |
| [Day 6](#day-6) | [Day 7](#day-7) | [Day 8](#day-8) | [Day 9](#day-9) | [Day 10](#day-10) |
| [Day 11](#day-11) | [Day 12](#day-12) | [Day 13](#day-13) | [Day 14](#day-14) | [Day 15](#day-15) |
| [Day 16](#day-16) | [Day 17](#day-17) | Day 18 | Day 19 | Day 20 |
| Day 21 | Day 22 | Day 23 | Day 24 | Day 25 |
||||||

</p>

<!--

|  |  | [Day 18](#day-18) | [Day 19](#day-19) | [Day 20](#day-20) |
| [Day 21](#day-21) | [Day 22](#day-22) | [Day 23](#day-23) | [Day 24](#day-24) | [Day 25](#day-25) |

-->

<p align="center">
<span style="color:green">
.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.
</span>

<span style="color:red">
*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*
</span>

<span style="color:green">
.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.
</span>
</p>

</span>




---
## Day 1
### *Sonar Sweep (Seafloor Depth)*
[code &#8614;](https://github.com/VereLanz/my-advent-2021/blob/main/my_advent/day1.py)
### Part One
You get a seafloor depth scan report. 
Find out how many measurements are larger (deeper) than the previous.

### Part Two
Group the seafloor depth scan values into groups of three (sum) and
find out how many measurement *groups* are larger (deeper) than the previous.


[top &#8593;](#top)


---
## Day 2
### *Dive! (Submarine Steering)*
[code &#8614;](https://github.com/VereLanz/my-advent-2021/blob/main/my_advent/day2.py)
### Part One
Follow the steering instructions given for your submarine (starting at (0, 0)) 
and multiply the final horizontal and vertical positions.

### Part Two
The steering works differently from what was assumed! 
The behaviours of the input commands have changed, calculate the positions anew.

[top &#8593;](#top)



---
## Day 3
### *Binary Diagnostic (Bits Piecing)*
[code &#8614;](https://github.com/VereLanz/my-advent-2021/blob/main/my_advent/day3.py)
### Part One
The submarine's diagnostic report gives you some binary numbers. Figure out the two needed
binary numbers by determining for each bit if more numbers in da report have a 0 or a 1
in that spot. Multiply those two resulting binaries for the submarine's 
power consumption.

### Part Two
From the diagnostic report, first filter out values step by step if they don't 
have the right bit. Then calculate the two new numbers like in Part One.

[top &#8593;](#top)



---
## Day 4
### *Giant Squid (Squid Bingo)*
[code &#8614;](https://github.com/VereLanz/my-advent-2021/blob/main/my_advent/day4.py)
### Part One
You get some bingo boards and a list of numbers that will be drawn in order.
Figure out which of the boards will get bingo first and what its score 
(= sum of non-called numbers) will be.

### Part Two
On second thought you'd make sure that your opponent (a giant squid) wins,
so figure out which board will be the last to bingo and calculate it's score.

[top &#8593;](#top)



---
## Day 5
### *Hydrothermal Venture (Vent Grid)*
[code &#8614;](https://github.com/VereLanz/my-advent-2021/blob/main/my_advent/day5.py)
### Part One
You get coordinates of start and end points for hydrothermal vent lines.
First, figure out spots where at least two horizontal or vertical lines overlap.
(Asked is how many overlaps there are.)

### Part Two
Now also consider diagonal lines and again check where at least two lines overlap.

[top &#8593;](#top)



---
## Day 6
### *Lanternfish (Exponential Spawning)*
[code &#8614;](https://github.com/VereLanz/my-advent-2021/blob/main/my_advent/day6.py)
### Part One
You wonder how many lanternfish will be spawned after 80 days. Calculate this from
some estimated spawn timers and give a simulated number of how many fish there will be.

### Part Two
Now simulate the numbers for 256 days...it gets a bit huge!

[top &#8593;](#top)



---
## Day 7
### *The Treachery of Whales (Crab Submarines)*
[code &#8614;](https://github.com/VereLanz/my-advent-2021/blob/main/my_advent/day7.py)
### Part One
You are trying to blast a hole into the wall to enter a cave to escape from an aggressive whale!
Some crabs in submarines are willing to help you by aligning their submarines, 
but need to minimise their fuel consumption.
From some starting positions, move all submarines horizontally to be in a line while
minimising their total steps needed.

### Part Two
Turns out the crab submarines' fuel consumption is not linear but increasing with each step.
Recalculate the horizontal alignment position while having each crab move as little as possible.

[top &#8593;](#top)



---
## Day 8
### *Seven Segment Search (7-Segment Display Puzzle)*
[code &#8614;](https://github.com/VereLanz/my-advent-2021/blob/main/my_advent/day8.py)
### Part One
Your seven segment displays' signals are all jumbled up!
First, look for the amount of unique digit signals in terms of segment number to work with.

### Part Two
Now considering these uniquely segment-numbered digits, figure out which segment in
your current output corresponds to which actual segment and therefore which numbers 
the display is trying to display! (Answer is sum of all output numbers.)

[top &#8593;](#top)



---
## Day 9
### *Smoke Basin (Cave Local Minima)*
[code &#8614;](https://github.com/VereLanz/my-advent-2021/blob/main/my_advent/day9.py)
### Part One
Inside the cave, some geothermal smoke is coming out of the walls and collecting inside
puddles in the cave tract. Find the local minima in a cave height profile to 
avoid these danger zones, and calculate the risk score for the cave section.

### Part Two
Instead of simple local minima we want to avoid the largest basins, which are basically
areas surrounded by highest points and have lower points in them. 
Multiply the three largest basins' sizes to get a basin risk score.

[top &#8593;](#top)



---
## Day 10
### *Syntax Scoring (Checking Brace-arenthe-ckets)*
[code &#8614;](https://github.com/VereLanz/my-advent-2021/blob/main/my_advent/day10.py)
### Part One
Your submarine threw a syntax error! Find where there was a wrong brace, parenthesis 
or bracket used in a line and calculate the score of the errors.
Do not count missing symbols for now, only wrong ones (corrupt line).

### Part Two
Now ignore the corrupt lines and focus on the incomplete ones. They are missing the
closing symbols at the end of the line. Find the missing symbols in the correct 
order and calculate each line's score and select the middle one for your answer.

[top &#8593;](#top)



---
## Day 11
### *Dumbo Octopus (Flash Waves)*
[code &#8614;](https://github.com/VereLanz/my-advent-2021/blob/main/my_advent/day11.py)
### Part One
You see some luminescent octopi in the dark cave and want to use their light flashes
to navigate the cave. First, find out how many octopi will have lit up after some steps.
Every shining octopus will also increase every neighbour's energy level for its own flash.

### Part Two
They do flash rather dimly, so you want to find the moment they all flash up simultaneously!
Find the first step in which all the octopi light up.

[top &#8593;](#top)



---
## Day 12
### *Passage Pathing (Path Completeness)*
[code &#8614;](https://github.com/VereLanz/my-advent-2021/blob/main/my_advent/day12.py)
### Part One
Before you lies a system of multiple small and big caves. Given the connections of 
each cave, find every possible path from your starting position to the end point, while
visiting smaller caves at most once.

### Part Two
After closer inspection, visiting ONE small cave twice on the way is okay as well, 
how many paths does that give?

[top &#8593;](#top)



---
## Day 13
### *Transparent Origami (Folding Matrices)*
[code &#8614;](https://github.com/VereLanz/my-advent-2021/blob/main/my_advent/day13.py)
### Part One
To figure out instructions for your submarine you need to fold a dotted, transparent 
paper according to some instructions and check the image that is formed by the
dots moving and overlapping.
First, figure out how many dots will be visible after doing the first instruction.

### Part Two
After completing all instructions, you will see an 8 capital letter code on your folded
sheet, this code is your answer!

[top &#8593;](#top)



---
## Day 14
### *Extended Polymerization (Inserting Letters)*
[code &#8614;](https://github.com/VereLanz/my-advent-2021/blob/main/my_advent/day14.py)
### Part One
From a chain of letters and instructions between which two letters a new one should be
inserted, calculate which letter will be there the most and which the least after
inserting letters as instructed for a given amount of steps.

### Part Two
Same as part one, but quadruple the steps!

[top &#8593;](#top)



---
## Day 15
### *Chiton (Lowest Risk Path)*
[code &#8614;](https://github.com/VereLanz/my-advent-2021/blob/main/my_advent/day15.py)
### Part One
The cave's exit is near, but the path ahead has the risk of bumping into Chiton-clad walls.
Calculate the lowest risk path from your top-left position to the bottom-right exit.

### Part Two
Oops, the actual cave is twenty-five times larger than you thought, try again!
(with a bigger map that you need to interpolate yourself)

[top &#8593;](#top)



---
## Day 16
### *Packet Decoder (Hex Bit Madness)*
[code &#8614;](https://github.com/VereLanz/my-advent-2021/blob/main/my_advent/day16.py)
### Part One
You receive a message from your colleagues back on the ship. It's a hexadecimal string
that is encoded crazy complicated, but you will have to unpack it. 
Start by identifying all sub-packets of your packet and summing up the version numbers.

### Part Two
Well that was easy (*cough cough*), now run all the operations given by full the chain
in order to find the desired answer!

[top &#8593;](#top)



---
## Day 17
### *Trick Shot (Probe Trajectory)*
[code &#8614;](https://github.com/VereLanz/my-advent-2021/blob/main/my_advent/day17.py)
### Part One
You want to launch a probe into a given target area inside a trench.
You also want it to look cool. Find the highest possible position your probe can 
reach with a starting velocity while still landing inside the target area.

### Part Two
Okay, maybe a trick shot isn't the smartest idea. What is smart to find out every 
possible start value combination that will land in the target area. Do that now!

[top &#8593;](#top)









<!---Daily Template

---
## Day 
### *name*
[code &#8614;](https://github.com/VereLanz/my-advent-2021/blob/main/my_advent/day.py)
### Part One
Short description...

### Part Two
Short description...

[top &#8593;](#top)

-->

