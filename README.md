# Puzzles

This is a repo for homework assignments / interview puzzles / programming excercizes.


# Hotplate

The scenario is that you have a grid of some sort in which certain cells are *hot*
and others are *cold*.

The hot cells stay at a constant 100º and the cold are always 0º.

The configuration can vary (from semester to semester, employee, kata iteration, etc),
but this demonstration it is always the centermost cells that are hot and the cornermost cells that are cold,
like so (6x6 grid):

    0, *, *, *, *, 0
    *, *, *, *, *, *
    *, *, 1, 1, *, *
    *, *, 1, 1, *, *
    *, *, *, *, *, *
    0, *, *, *, *, 0

Each turn the new temperature of a cell is calculated by averaging it's previous value with the values of the 4 cells
up, down, left, and right of it.

The objective of the program is to find how many turns it takes before the difference in value of all cells is less
than some amount (i.e. finding the 'limit' *Δ < 0.01*)

For each cell with a `*` it doesn't matter whether the starting value is 0 or 100.
Each cell will eventually stabalize at the same value no matter which value it starts with,
but if the starting value of each cell were 50, the program would finish slightly sooner.

## Gotchas

TBD
