 # first generate standard outputs
>>>>>>>>                               # move to cell 8
[-]+++++                               # cell 8 = 4 (move) plus 1 (East)
>[-]++++                               # cell 9 = 4 (move) plus 0 (North)
<<<                                    # go back to cell 6
[-]+                                   # set to 1 (harvest)
<<<<<<                                 # go back to 0 to start loop


+[>++++++++[>,              # start outer infinite loop and inner 8x8 loop and read input into cell 2

# check for value 5 (harvestable grass)
>[-]>[-]<<                   # first clear helper cells
[>+>+<<-]                    # move value to helper cells 1 and 2
>>[<<+>>-]                   # move value back to value cell
<-----                       # subtract test number (5) from value cell
[>-<[-]]                     # if the value is not 0 pre negate the test flag
>+                           # set flag to indicate loop
[>>.<<<<[-]>>[-]]            # print cell 6 (harvest), clear value then reset flag
<<                           # return to value cell and end elif


# Reset inner loop
<                            # go to counter cell
# output move east
>>>>>>>.<<<<<<<              # output 5
-                            # decrement counter
]<                           # end loop and go to outer loop

reset outer loop
>>>>>>>>>.<<<<<<<<<           # output 4
]                             # end outer infinite loop
