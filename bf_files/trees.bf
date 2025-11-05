# memory structure: loop0 loop1 tree_flag bush_flag harvestable_tree harvestable_bush value0 value1 temp0 harvest plant_tree plant_bush move_east move_north
# initialize standard outputs
>>>>                            # move to cell 4
+++++++++++++                   # set cell 4 to value of harvestable tree
>+++++++++                      # set cell 5 to value of harvestable bush
>>>>                            # move to cell 9 to set up plant commands
++++++++++++++++[               # repeate 16 times
>++++++++                       # increment cell 10 by 8
>++++++++                       # increment cell 11 by 8
<<-]                            # decrement cell 9 until 0
>++                             # cell 10 = 128 (plant) plus 2 (tree)
>+                              # cell 11 = 128 (plant) plus 1 (bush)
>+++++                          # cell 12 = 4 (move) plus 1 (East)
>++++                           # cell 13 = 4 (move) plus 0 (North)
<<<<[-]+                        # cell 9 = 1 (harvest)
<<<<<<<+                        # set tree flag at 2 to True
<<                              # return to cell 0

# Prep farm  Only do this once 
++++++++[                       # y loop Run 8 times                               memory location 0
>++++++++[                      # x loop Run 8 times                               memory location 1
>                               # move to tree flag                                memory location 2
[                               # if tree flag set                                 memory location 2
>>>>>>>>.                       # output plant tree                                memory location 10
<<<<<<<-                        # pre negate bush flag                             memory location 3
<-                              # disable tree flag                                memory location 2
]                               # end if                                           memory location 2
>+                              # attempt to set bush flag                         memory location 3
[                               # if bush flag set                                 memory location 3
>>>>>>>>.                       # output plant bush                                memory location 11
<<<<<<<<<+                      # enable tree flag                                 memory location 2
>-                              # disable bush flag                                memory location 3
]                               # end if                                           memory location 3
>>>>>>>>>.                      # output move east                                 memory location 12
<<<<<<<<<<<-                    # decrement x loop                                 memory location 1
]                               # end x loop                                       memory location 1
>>>>>>>>>>>>.                   # output move north                                memory location 13
<<<<<<<<<<<                     # go to tree flag                                  memory location 2
[->+<]                          # move tree to bush flag (temporary)               memory location 2
>[<->-]                         # if set pre negate tree flag                      memory location 3
<+                              # attempt to enable tree flag                      memory location 2      
<<-]                            # end y loop                                       memory location 0  

# Infinite loop to harvest and replant
+[                              # infinite loop                                    memory location 0
>++++++++[                      # x loop Run 8 times                               memory location 1
# if harvestable tree replant tree
>>>                             # move to harvestable tree value                   memory location 4
[>>+>+<<<-]>>>[<<<+>>>-]        # copy tree value to value 0                       memory location 7
,                               # get current entity value                         memory location 7
[-<->]                          # subtract value 1 from value 0                    memory location 7
>[-]                            # clear temp0 to use as flag                       memory location 8
<<                              # go to value 0                                    memory location 6
[                               # if not 0                                         memory location 6
>>-                             # pre negate harvestable tree flag                 memory location 8
<<[-]                           # clear value 0                                    memory location 6
]                               # end if                                           memory location 6
>>+                             # go to harvestable tree flag                      memory location 8
[                               # start if harvestable tree                        memory location 8
>.                              # output harvest                                   memory location 9
>.                              # output plant tree                                memory location 10
<<-]                            # end if                                           memory location 8
# if harvestable bush replant bush
<<<                             # move to harvestable bush value                   memory location 5
[>+>+<<-]>>[<<+>>-]             # copy bush value to value 0                       memory location 7
,,,                             # reset plant value to entity type                 memory location 7
,                               # get current entity value                         memory location 7
[-<->]                          # subtract value 1 from value 0                    memory location 7
>[-]                            # clear temp0 to use as flag                       memory location 8
<<                              # go to value 0                                    memory location 6
[                               # if not 0                                         memory location 6
>>-                             # pre negate harvestable bush flag                 memory location 8
<<[-]                           # clear value 0                                    memory location 6
]                               # end if                                           memory location 6
>>+                             # go to harvestable bush flag                      memory location 8
[                               # start if harvestable bush                        memory location 8
>.                              # output harvest                                   memory location 9
>>.                             # output plant bush                                memory location 10
<<<-]                           # end if                                           memory location 8

>>>>.                           # output move east                                 memory location 12
<<<<<<<<<<<-                    # decrement x loop                                 memory location 1
]
>>>>>>>>>>>>.                   # output move north                                memory location 13
<<<<<<<<<<<<<                   # return to main loop                              memory location 0
]
