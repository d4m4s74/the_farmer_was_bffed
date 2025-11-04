# Simple hamiltonian cycle because the point is to do it  not to do it well
# memory structure: loop0 loop1 loop2 temp0 temp1 move_north move_east move_south move_west dinosaur_hat straw_hat
# initialize standard outputs
>>>>>>>>                          # move to cell 8 to set up hats
+++++++++++[>++++++>++++++<<-]    # set hat cells to 66
>++++                             # set cell 9 to 70 (Dinosaur Hat)
>+++                              # set cell 10 to 69 (Straw Hat)
<<[-]                             # clear cell 8
+++++++                           # set cell 8 to 7 (Move West)
<++++++                           # set cell 7 to 6 (Move South)
<+++++                            # set cell 6 to 5 (Move East)
<++++                             # set cell 5 to 4 (Move North)
<<<<<                             # return to cell 0

+[                                # Outer infinite loop           Memory location 0
>>>>>>>>>.                        # Put on dinosaur hat           Memory location 9
<........                         # Force move to x:0             Memory location 8
<........                         # Force move to y:0             Memory location 7
<<<<<<                            # go to next loop               Memory location 1
+[                                # Full screen loop start        Memory location 1
>>>>>.                            # Move East once                Memory location 6
<<<<                              # go to next loop               Memory location 2
++++[                             # Side to side loop start       Memory location 2
>>>>......                        # move to x 7                   Memory location 6
<.                                # move north once               Memory location 5
>>>......                         # move to x 1                   Memory location 8
<<<.                              # attempt move north once       Memory location 5
<<<-                              # decrement side to side loop   Memory location 2
]
>>>>>>.                           # Move West once                Memory location 8
<.......                          # move to x 0 y 0               Memory location 7
<<<<<<,,                          # Get directions bitmask        Memory location 1
]                                 # End loop if 0                 Memory location 1
>>>>>>>>>.                        # Put on straw hat              Memory location 10
<<<<<<<<<<                        # Return to outer loop          Memory location 0
]
