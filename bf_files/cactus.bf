# memory structure: 1 loop0 loop1 loop2 value1 value2 comparison_flag temp0 temp1 swap_flag till harvest plant_cactus swap_east swap_north move_east move_north
#initialize standard outputs
>>>>>>>>>>>>            #move to cell 12
<[-]++++++++++++++++[>++++++++<-]>+++++  # cell 12 = 128 (plant) plus 5 (cactus)
>[-]+++++++++++++++++++++++++++++++++    # cell 13 = 32 (swap) plus 1 (East)
>[-]++++++++++++++++++++++++++++++++     # cell 14 = 32 (swap) plus 0 (North)
>[]+++++                                 # cell 15 = 4 (move) plus 1 (East)
>[-]++++                                 # cell 16 = 4 (move) plus 0 (North)
<<<<<                                    # go back to cell 116
[-]+                                     # set cell 11 to 1 (harvest)
<[-]                                     # set cell 10 to 0 (till)
<<<<<<<<<<                               # go back to 0 to start loop



# till and plant loop Run only once
>++++++++[                    # y loop (8)
>++++++++[                    # x loop (8)
>                             # skip extra loop cell
# We start with a full untilled field  First loop: till all cells and plant cactus  no measuring necessary
>>>>>>>.                      # output till
>>.                           # output plant cactus
>>>.                          # output move east
<<<<<<<<<<<<<-                # decrement x
]
>>>>>>>>>>>>>>.<<<<<<<<<<<<<< # output move north
<-                # decrement y
]

<+[                           # infinite loop
# swap loops
# x axis swaps
>++++++++[                                                          # y loop (8)                       memory location 1
>+[-                                                                # start swap loop and disable flag memory location 2
>>>>>>>[-]                                                          # clear swap flag                  memory location 9
<<<<<<                                                              # go to x loop cell                memory location 3
+++++++[                                                            # x loop (7)                       memory location 3
>,,>,,<                                                             # read in cactus values            memory location 4
>>>[-]>[-]<<[-]<<[>>>+<<[->>[-]>+<<<]>>[-<+>]>[-<<<+>>>]<<<-<-]     # compare values a greater than b  memory location 4  code from esolangs wiki
>>                                                                  # go to result cell                memory location 6
[                                                                   # start if greater                 memory location 6
>>>+                                                                # increment swap flag cell         memory location 9
>>>>.                                                               # output swap east                 memory location 13
<<<<<<<                                                             # return to result cell            memory location 6
[-]                                                                 # clear result cell                memory location 6
]                                                                   # end if greater                   memory location 6
>>>>>>>>>.                                                          # output move east                 memory location 15
<<<<<<<<<<<<-                                                       # decrement x loop                 memory location 3
]                                                                   # end x loop                       memory location 3
>>>>>>>>>>>>.                                                       # output move east                 memory location 15
<<<<<<                                                              # go to swap flag cell             memory location 9
[                                                                   # start if swapped                 memory location 9
<<<<<<<+                                                            # reenable loop                    memory location 2
>>>>>>>[-]                                                          # clear swap flag                  memory location 9
]                                                                   # end if swapped                   memory location 9
<<<<<<<                                                             # return to swap loop              memory location 2
]                                                                   # end swap loop                    memory location 2
>>>>>>>>>>>>>>.                                                     # output move north                memory location 16
<<<<<<<<<<<<<<<-                                                    # decrement y loop                 memory location 1
]                                                                   # end y loop                       memory location 1
# y axis swaps
++++++++[                                                           # x loop (8)                       memory location 1
>+[-                                                                # start swap loop and disable flag memory location 2
>>>>>>>[-]                                                          # clear swap flag                  memory location 9
<<<<<<                                                              # go to y loop cell                memory location 3
+++++++[                                                            # y loop (7)                       memory location 3
>,,>,<                                                              # read in cactus values            memory location 4
>>>[-]>[-]<<[-]<<[>>>+<<[->>[-]>+<<<]>>[-<+>]>[-<<<+>>>]<<<-<-]     # compare values a greater than b  memory location 4  code from esolangs wiki
>>                                                                  # go to result cell                memory location 6
[                                                                   # start if greater                 memory location 6
>>>+                                                                # increment swap flag cell         memory location 9
>>>>>.                                                              # output swap north                memory location 13
<<<<<<<<                                                            # return to result cell            memory location 6
[-]                                                                 # clear result cell                memory location 6
]                                                                   # end if greater                   memory location 6
>>>>>>>>>>.                                                         # output move north                memory location 15
<<<<<<<<<<<<<-                                                      # decrement y loop                 memory location 3
]                                                                   # end y loop                       memory location 3
>>>>>>>>>>>>>.                                                      # output move north                memory location 15
<<<<<<<                                                             # go to swap flag cell             memory location 9
[                                                                   # start if swapped                 memory location 9
<<<<<<<+                                                            # reenable loop                    memory location 2
>>>>>>>[-]                                                          # clear swap flag                  memory location 9
]                                                                   # end if swapped                   memory location 9
<<<<<<<                                                             # return to swap loop              memory location 2
]                                                                   # end swap loop                    memory location 2
>>>>>>>>>>>>>.                                                      # output move east                 memory location 16
<<<<<<<<<<<<<<-                                                     # decrement x loop                 memory location 1
]                                                                   # end x loop                       memory location 1
>>>>>>>>>>.                                                         # output harvest                   memory location 11
<<<<<<<<<<                                                          # go to start of plant loop        memory location 1
# plant loop
++++++++[                     # y loop (8)
>++++++++[                    # x loop (8)
>                             # skip extra loop cell
# We start with a tilled but empty field plant cactus  no measuring necessary
>>>>>>>>>.                    # output plant cactus
>>>.                          # output move east
<<<<<<<<<<<<<-                # decrement x
]
>>>>>>>>>>>>>>.<<<<<<<<<<<<<< # output move north
<-                            # decrement y
]
<]
