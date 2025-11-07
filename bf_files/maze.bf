# Proof of concept extremely slow
# Memory layout: loop0 loop2 value0 copy0 value1 temp0 temp1 temp2 dir0 dir1 dir2 dir3 shift shift_temp plant_bush gen_maze harvest
# first generate standard outputs
>>>>>>>>>>>>>                    # move to cell 13
++++++++[>++++++++++++++++<-]>+  # cell 14 = 128 (plant) plus 1 (bush)
>>++++++++[<++++++++>-]<++++     # cell 15 = 64 (use_item) plus 4 (generate maze)
>+                               # cell 16 = 1 (harvest)
<<<<<<<<<<<<<<<<                 # return to cell 0 to start loop

+[                               # start outer infinite loop                    Memory location 0
>>>>>>>>>>>>>>.                  # output plant bush                            Memory location 14
>.                               # output generate maze                         Memory location 15
<<<<<<<<<<<<<<                   # go to start of loop                          Memory location 1

,                                # read entity type into loop counter           Memory location 1
>++++[<---------->-]<            # subtract 40 (treasure) from entity           Memory location 1
[[-]                             # start maze traverse loop and zero            Memory location 1
>,,,                            # read available directions into value0         Memory location 2
# bit splitter: This version changes the direction bit to movement opcodes

#binary counter borrowed from gnvr on esotultles discord
>++<[->>>>>[-<]+ <--[++<--]++<]                                                  Memory location 2
set directions to correct locations
>>[>>>>>>>+++++++<<<<<<<-]        # West                                          Memory location 4
>[>>>>>++++++<<<<<-]                # South                                         Memory location 5
>[>>>+++++<<<-]                   # East                                          Memory location 6
>[>++++<-]                        # North                                         Memory location 7
<<<<[-]<[-]

# example result: 1 0 0 0 0 0 0 0 4 5 6 7
>>>>>>>>>>                          # move to shift cell                                            Memory location 12
>[-]<                               # clear shift temp                                              Memory location 12
[                                   # start shift loop                                              Memory location 12
<<<<[<+>-]                          # shift dir0 into temp2                                         Memory location 8
>[<+>-]                             # shift dir1 into dir0                                          Memory location 9
>[<+>-]                             # shift dir2 into dir1                                          Memory location 10
>[<+>-]                             # shift dir3 into dir2                                          Memory location 11
<<<<[>>>>+<<<<-]                    # shift temp2 into dir3                                         Memory location 7
>>>>>>+<-                           # decrement shift counter storing in shift_temp                 Memory location 12
]                                   # end shift loop                                                Memory location 12
>[<+>-]<                            # move shifted value back to shift cell                         Memory location 12
<<<<                                # go to dir0 (basically left)                                   Memory location 8

[                                   # if direction is set                                           Memory location 8
.                                   # output move left                                              Memory location 8
>[-]>[-]>[-]                        # clear all other directions                                    memory location 11
>+++                                # add 3 to shift cell                                           Memory location 12
<<<<[-]]                            # go back to dir0 and end if                                    Memory location 8
>                                   # go to dir1 (forward)                                          Memory location 9

[                                   # if direction is set                                           Memory location 9
.                                   # output move forward                                           Memory location 9
>[-]>[-]                            # clear all other directions                                    memory location 11
<<[-]]                              # go back to dir1 and end if                                    Memory location 9
>                                   # go to dir2 (right)                                            Memory location 10

[                                   # if direction is set                                           Memory location 10
.                                   # output move right                                             Memory location 10
>[-]                                # clear all other directions                                    memory location 11
>+                                  # go to shift cell and add 1                                    Memory location 12
<<[-]]                              # go back to dir2 and end if                                    Memory location 10
>                                   # go to dir3 (backward)                                         Memory location 11

[                                   # if direction is set                                           Memory location 11
.                                   # output move back                                              Memory location 11
>++                                 # add 2 to shift cell                                           Memory location 12
<[-]]                               # go back to dir3 and end if                                    Memory location 11

>                                   # go to shift cell                                              Memory location 12

[>+<<<<<<<<<<+>>>>>>>>>-]           # move shift counter to value1 for math and temp for storage    Memory location 12

<<<<<<<<                            # go to temp0                                                   Memory location 4
++++<                               # set value to 4 for comparison                                 Memory location 3
>>>[-]>[-]<<[-]<<[>>>+<<[->>[-]>+<<<]>>[-<+>]>[-<<<+>>>]<<<-<-]>[>-<[-]]>+                          Memory location 5
[>>>>>>>----<<<<<<<[-]]             # If number is equal or more than 4 subtract 4                  Memory location 5
>>>>>>>>[<+>-]<                     # move back to shift cell                                       Memory location 12

<<<<<<<<<<<                         # go back to loop counter                                       Memory location 1
,                                   # read entity type into loop counter                            Memory location 1
>++++[<---------->-]<               # subtract 40 (treasure) from entity                            Memory location 1
]                                   # go back if no treasure found                                  Memory location 1
>>>>>>>>>>>>>>>.                    # output harvest                                                Memory location 16
<<<<<<<<<<<<<<<<                    # return to outer loop                                          Memory location 0
]                                   # do it all again                                               Memory location 0
