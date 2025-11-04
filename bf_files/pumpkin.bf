# memory structure: loop0 loop1 loop2 loop3 harvestable_pumpkin value0 value1 temp0 temp1 till harvest plant_pumpkin move_east move_north
# initialize standard outputs
>>>>                                    # move to cell 4
+++++++++++++++++++++++                 # set to value of harvestable pumpkin
>>>>>>>                                 # move to cell 11
<[-]++++++++++++++++[>++++++++<-]>++++  # set to 128 (plant) plus 4 (pumpkin)
>+++++                                  # cell 12: 5 (Move East)
>++++                                   # cell 13: 4 (Move North)
<<<[-]+                                 # cell 10: 1 (harvest)
<[-]                                    # cell 9: 0 (till)
<<<<<<<<<                               # return to cell 0


# Till and plant Only do this once
++++++++[                               # y loop Run 8 times                               memory location 0
>++++++++[                              # x loop Run 8 times                               memory location 1
>>>>>>>>.                               # output till                                      memory location 9
>>.                                     # output plant pumpkin                             memory location 11
>.                                      # output move east                                 memory location 12
<<<<<<<<<<<-                            # decrement x loop                                 memory location 1
]                                       # end x loop                                       memory location 1
>>>>>>>>>>>>.                           # output move east                                 memory location 13
<<<<<<<<<<<<<-                          # decrement y loop                                 memory location 0
]                                       # end y loop                                       memory location 0

+[                                      # infinite loop                                    memory location 0

# Cycle over farm and replace any pumpkin that's not harvestable
>+[-                                    # Outer loop Disable immediately                   memory location 1
>++++++++[                              # y loop Run 8 times                               memory location 2
>++++++++[                              # x loop Run 8 times                               memory location 3
>>[-]>[-]>[-]<<<                        # clear value 0 1 and temp1                        memory location 4
[>+>+<<-]>>[<<+>>-]                     # Copy pumpkin value to value0                     memory location 6
,                                       # Get current entity value                         memory location 6
[-<->]<                                 # Subtract value 1 from value 0                    memory location 5  #note add to interpreter
[>>+<<[-]]                              # if not 0 set replant flag in temp0               memory location 5
>>                                      # try to set replant flag in temp0                 memory location 7
[                                       # start if                                         memory location 7
>>>>.                                   # plant new pumpkin if dead                        memory location 11
<<<<[-]]                                # end if                                           memory loccation 7
>>>>>.                                  # output move east                                 memory location 12
<<<<<<<<<-                              # decrement x loop                                 memory location 3
]                                       # end x loop                                       memory location 3
>>>>>>>>>>.                             # output move north                                memory location 13
<<<<<<<<<<<-                            # decrement y loop                                 memory location 2
]                                       # end y loop                                       memory location 2
# if center measurement != south measurement reenable loop
>>[>+>+<<-]>>[<<+>>-]                   # copy south pumpkin to value0                     memory location 6
,                                       # get entity                                       memory location 6
[-<->]<                                 # Subtract value 1 from value 0                    memory location 5
[>>-<<<<<<+>>>>[-]]                     # if not 0 negate flag in temp0 and set loop flag  memory location 5
>>+                                     # if a == b:                                       memory location 7
[                                       # start if                                         memory location 7
<<                                      # go to value 0                                    memory location 5
,                                       # set value 0 to pumkin ID                         memory location 5
>,,,                                    # set value 1 to south pumpkin ID                  memory location 6
[-<->]<                                 # Subtract value 1 from value 0                    memory location 5
[<<<<+>>>>[-]]                          # reenable loop                                    memory location 5
,                                       # reset pumpkin measurement                        memory location 5
>>[-]]                                  # end if                                           memory location 7
<<<<<<                                  # go to loop flag                                  memory location 1
]                                       # End outer loop                                   memory location 1
# harvest once
>>>>>>>>>.                              # Output harvest                                   memory location 10
<<<<<<<<<                               # return to loop1                                  memory location 1
# Replant after harvest
++++++++[                               # y loop Run 8 times                               memory location 1
>++++++++[                              # x loop Run 8 times                               memory location 2
>>>>>>>>>.                              # output plant pumpkin                             memory location 11
>.                                      # output move east                                 memory location 12
<<<<<<<<<<-                             # decrement x loop                                 memory location 2
]                                       # end x loop                                       memory location 2
>>>>>>>>>>>.                            # output move east                                 memory location 13
<<<<<<<<<<<<-                           # decrement y loop                                 memory location 1
]                                       # end y loop                                       memory location 1
<
]                                       # end infinite loop
