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

# CSV Parser

CSV (comma separeted values) is a fairly simple standard for storing information that
can easily be represented as a spreadsheet (or a single table of a database),
such as an address book.

    AJ,Alvin,ONeal,coolaj86@gmail.com
    Dave,David,Nelson,davidicus21@gmail.com

It consists of a **column separator** - usually **commas** or tabs.
and a **row separator** - usually a newline, carriage return,
or **[CRLF](http://stackoverflow.com/questions/1279779/what-is-the-difference-between-r-and-n)**.

Sometimes the first row is used as the **header**.

    Nick,First,Last,Email
    AJ,Alvin,ONeal,coolaj86@gmail.com
    Dave,David,Nelson,davidicus21@gmail.com

Since individual **fields** may sometimes contain one of the *separators*
quoting is often used.

    Name,Address
    "Doe, John","123 Nowhere Ave
    Provo, UT"
    "Doe, Jane","321 Somewhere Dr
    Apt #222
    Orem, UT"

Since **fields** may also sometimes contain quotes,
an additonal quote may be used to escape quotes.

> If double-quotes are used to enclose fields,
> then a double-quote appearing inside a field 
> must be escaped by preceding it with another
> double quote. -
> http://stackoverflow.com/a/769675/151312

    Name,Email
    "Alvin ""AJ"" ONeal",coolaj86@gmail.com
    "David ""Dave"" Nelson,davidicus21@gmail.com

## Gotchas

When writing a streaming parser, you may need the next chunk
to determine whether or not a line or field is complete.

Chunk 1

    "Alvin "

Chunk 2

    "AJ"" ONeal"

The row separator is often allowed to be any of `\r`, `\n`, or `\r\n`.

See also

* http://en.wikipedia.org/wiki/Newline
* http://stackoverflow.com/questions/1279779/what-is-the-difference-between-r-and-n
