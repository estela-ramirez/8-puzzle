<!-- Table of Contents -->
# Table of Contents
- [About the Project](#star2-about-the-project)
  * [Search Trace Example](#detective-search-trace-example)
  * [Tech Stack](#space_invader-tech-stack)
  * [Run Locally](#running_woman-run-locally)


<!-- About the Project -->
## :star2: About the Project
<p>This program solves the 8 puzzle using </p>
<ol>
    <li>Uniform Cost Search</li>
    <li>A* with the Misplaced Tile heuristic</li>
    <li>A* with the Euclidean Distance heuristic</li>
</ol>

It shows the steps the algorithm takes to find a solution.
Once the solution is found, the olution path is printed. 

You can use the default puzzle or input your own

Default puzzle:

```bash
[1 2 3 
 4 5 6
 7 0 8]
```

<!-- Search Trace Example -->
### :detective: Search Trace Example
If you enter the puzzle 

```bash
[1 2 3 
 4 8 0
 7 6 5]
```

and select A* with Eudlidian Distance Heursitic

```bash
Expanding state

1 2 3 
4 8 0 
7 6 5 

The best state to expand with g(n) = 1  and  h(n) = 3.414213562373095
Move: down...

1 2 3 
4 8 5 
7 6 0 

The best state to expand with g(n) = 2  and  h(n) = 3.0
Move: left...

1 2 3 
4 8 5 
7 0 6 

The best state to expand with g(n) = 3  and  h(n) = 2.0
Move: up...

1 2 3 
4 0 5 
7 8 6 

The best state to expand with g(n) = 4  and  h(n) = 1.0
Move: right...

1 2 3 
4 5 0 
7 8 6 

The best state to expand with g(n) = 5  and  h(n) = 0.0
Move: down...

1 2 3 
4 5 6 
7 8 0 

Goal!!!


To solve this problem the algorithm expanded a total of 5 nodes.
The maximum number of nodes in the queue at any one time: 7
the depth of the goal node was 5

Printing solution path ... 

1 2 3 
4 8 0 
7 6 5 

Move: down...

1 2 3 
4 8 5 
7 6 0 

Move: left...

1 2 3 
4 8 5 
7 0 6 

Move: up...

1 2 3 
4 0 5 
7 8 6 

Move: right...

1 2 3 
4 5 0 
7 8 6 

Move: down...

1 2 3 
4 5 6 
7 8 0
```

<!-- TechStack -->
### :space_invader: Tech Stack

<details>
  <summary>Client</summary>
   <ul>
     <li><a href="https://www.python.org/downloads/">Python</a></li>
   </ul>
</details>


<!-- Run Locally -->
### :running_woman: Run Locally
Clone the project

```bash
  git clone https://github.com/estela-ramirez/8-puzzle.git
```

Go to the project directory

```bash
  cd 8-puzzle/
```

Run program

```bash
  python main.py
```