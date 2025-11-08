def left_shift(x, n):
    return x * (2 ** n)
def right_shift(x, n):
    return x // (2 ** n)

global code6
code = ""
global code_length
code_length = 0
global ptr
ptr = 0
global data_ptr
data_ptr = 0
global memory
memory = [0]
global moves
moves = {4:North,5:East,6:South,7:West}
global swap_moves
swap_moves = {32:North,33:East,34:South,35:West}
global plants_write
plants_write = {128:Entities.Grass,129:Entities.Bush,130:Entities.Tree,131:Entities.Carrot,132:Entities.Pumpkin,133:Entities.Cactus,134:Entities.Sunflower}
global plants_read
plants_read = {None:0,Entities.Grass:1,Entities.Bush:2,Entities.Tree:3,Entities.Carrot:4,Entities.Pumpkin:5,Entities.Cactus:6,Entities.Sunflower:7,Entities.Dead_Pumpkin:8,Entities.Apple:9,Entities.Treasure:10,Entities.Hedge:11}
global items
items = {64:Items.Water,65:Items.Fertilizer,66:Items.Weird_Substance}
global plant_info
plant_info = []
global info_ptr
info_ptr = 0
global plants_with_companions
plants_with_companions = {Entities.Grass,Entities.Bush,Entities.Tree,Entities.Carrot}
global plants_with_values
plants_with_values = {Entities.Cactus,Entities.Sunflower}
global pumpkin_numbers
pumpkin_numbers = dict()
global pumpkins
known_pumpkins = []
global next_pumpkin_number
next_pumpkin_number = 0
global bracket_partners
bracket_partners = dict()
global functions
functions = dict()
global symbols
symbols = dict()
global calc_rejects
calc_rejects = set()
global substance
substance = 0

def qm():
    global ptr
    global memory
    global data_ptr
    ptr += 1
    #set breakpoint here

symbols['?'] = qm

def gt():
    global code
    global code_length
    global ptr
    global memory
    global data_ptr
    global functions
    if code_length >= ptr + 63 and code[ptr+3] == '[' and code[ptr:ptr+63] == ">>>[-]>[-]<<[-]<<[>>>+<<[->>[-]>+<<<]>>[-<+>]>[-<<<+>>>]<<<-<-]":
        def greater():
            global memory
            global ptr
            global data_ptr
            pos0 = 0
            pos1 = memory[data_ptr] - memory[data_ptr+1]
            if memory[data_ptr] > memory[data_ptr+1]:
                pos3 = 1
            else:
                pos3 = 0
            pos4 = 0
            pos5 = 0
            memory[data_ptr] = pos0
            memory[data_ptr+1] = pos1%256
            memory[data_ptr+2] = pos3
            memory[data_ptr+3] = pos4
            memory[data_ptr+4] = pos5
            ptr = ptr + 63
        functions[ptr] = greater
        greater()
        return
    elif code_length >= ptr + 30 and code[ptr+4] == '[' and code[ptr:ptr+30] == ">++<[->>>>>[-<]+<--[++<--]++<]" and memory[data_ptr] < 16 and not memory[data_ptr+1]:
        def splitter():
            global memory
            global data_ptr
            global ptr
            global symbols
            if memory[data_ptr] > 15 or memory[data_ptr+1]:
                symbols['>']()
                return
            if memory[data_ptr] %2 == 1:
                memory[data_ptr+5] = (memory[data_ptr+5] + 1) % 256
                memory[data_ptr] -= 1
            if memory[data_ptr] %4 == 2:
                memory[data_ptr+4] = (memory[data_ptr+4] + 1) % 256
                memory[data_ptr] -= 2
            if memory[data_ptr] %8 == 4:
                memory[data_ptr+3] = (memory[data_ptr+3] + 1) % 256
                memory[data_ptr] -= 4
            if memory[data_ptr] == 8:
                memory[data_ptr+2] = (memory[data_ptr+2] + 1) % 256
            memory[data_ptr] = 0
            ptr = ptr + 30
        functions[ptr] = splitter
        splitter()
        return
    else:
        start = ptr
        data_start = data_ptr
        while code[ptr] == '>':
            data_ptr += 1
            if data_ptr == len(memory):
                memory.append(0)
            ptr += 1
        data_change = data_ptr - data_start
        end_ptr = ptr
        def gt_default():
            global ptr
            global data_ptr
            global memory
            data_ptr += data_change
            ptr = end_ptr
            while len(memory) < data_ptr:
                memory.append(0)
        if start not in functions:
            functions[start] = gt_default
symbols['>'] = gt

def lt():
    global code
    global ptr
    global memory
    global data_ptr
    global functions
    start = ptr
    data_start = data_ptr
    while code[ptr] == '<':
        data_ptr -= 1
        ptr += 1
    end_ptr = ptr
    data_change = data_ptr - data_start
    def lt_default():
        global ptr
        global data_ptr
        data_ptr += data_change
        ptr = end_ptr
    functions[start] = lt_default
symbols['<'] = lt

def p():
    global code
    global ptr
    global memory
    global data_ptr
    global functions
    start = ptr
    change = 0
    while code[ptr] == '+':
        memory[data_ptr] += 1
        change += 1
        ptr += 1
    end_ptr = ptr
    def p_default():
        global memory
        global data_ptr
        global ptr
        memory[data_ptr] = (memory[data_ptr] + change) % 256
        ptr = end_ptr
    functions[start] = p_default
symbols['+'] = p

def m():
    global code
    global ptr
    global memory
    global data_ptr
    global functions
    start = ptr
    change = 0
    while code[ptr] == '-':
        memory[data_ptr] -= 1
        change -= 1
        ptr += 1
    end_ptr = ptr
    def m_default():
        global memory
        global data_ptr
        global ptr
        memory[data_ptr] = (memory[data_ptr] + change) % 256
        ptr = end_ptr
    functions[start] = m_default
symbols['-'] = m

def lb():
    global code
    global code_length
    global ptr
    global memory
    global data_ptr
    global functions
    global bracket_partners
    global calc_rejects
    if not memory[data_ptr]:
        if ptr in bracket_partners:
            ptr = bracket_partners[ptr]+1
        else:
            start = ptr
            open_brackets = 1
            while open_brackets > 0:
                ptr += 1
                if code[ptr] == '[':
                    open_brackets += 1
                elif code[ptr] == ']':
                    open_brackets -= 1
            bracket_partners[start] = ptr
            bracket_partners[ptr] = start
    else:
        if code[ptr+1] == '-' and code[ptr+2] == ']':
            def set_0():
                global memory
                global data_ptr
                global ptr
                memory[data_ptr] = 0
                ptr += 3
            functions[ptr] = set_0
            set_0()
            return
        elif code_length >= ptr + 6 and code[ptr:ptr+6] == '[-<->]':
            def subtract_left():
                global memory
                global data_ptr
                global ptr
                memory[data_ptr - 1] = (memory[data_ptr - 1] - memory[data_ptr]) % 256
                memory[data_ptr] = 0
                ptr += 6
            functions[ptr] = subtract_left
            subtract_left()
            return
        elif code_length >= ptr + 6 and code[ptr:ptr+6] == '[>+<-]':
            def add_right():
                global memory
                global data_ptr
                global ptr
                memory[data_ptr + 1] = (memory[data_ptr + 1] + memory[data_ptr]) % 256
                memory[data_ptr] = 0
                ptr += 6
            functions[ptr] = add_right
            add_right()
            return
        elif code_length >= ptr + 6 and code[ptr:ptr+6] == '[<+>-]':
            def add_left():
                global memory
                global data_ptr
                global ptr
                memory[data_ptr - 1] = (memory[data_ptr-1] + memory[data_ptr]) % 256
                memory[data_ptr] = 0
                ptr += 6
            functions[ptr] = add_left
            add_left()
            return
        elif code_length >= ptr + 19 and code[ptr:ptr+19] == '[>+>+<<-]>>[<<+>>-]':
            def copy_right():
                global memory
                global data_ptr
                global ptr
                memory[data_ptr + 1] = memory[data_ptr] + memory[data_ptr+1]
                memory[data_ptr] = memory[data_ptr] + memory[data_ptr+2]
                memory[data_ptr + 2] = 0
                data_ptr += 2
                ptr += 19
            functions[ptr] = copy_right
            copy_right()
            return
        elif code_length >= ptr + 58 and code[ptr:ptr+58] == "[<<<<[<+>-]>[<+>-]>[<+>-]>[<+>-]<<<<[>>>>+<<<<-]>>>>>>+<-]":
            def shift_4():
                global memory
                global data_ptr
                global ptr
                for _ in range(memory[data_ptr]):
                    memory[data_ptr-4], memory[data_ptr-3], memory[data_ptr-2], memory[data_ptr-1] = memory[data_ptr-3], memory[data_ptr-2], memory[data_ptr-1], memory[data_ptr-4]
                memory[data_ptr+1] += memory[data_ptr]
                memory[data_ptr] = 0
                ptr += 58
            functions[ptr] = shift_4
            shift_4()
            return
        elif ptr not in calc_rejects:
            success = False
            mem_minus = []
            mem_plus = []
            shift = 0
            new_ptr = ptr
            base_changes = 0
            data_start = data_ptr
            while True:
                new_ptr += 1
                if code[new_ptr] == ">":
                    shift += 1
                elif code[new_ptr] == "<":
                    shift -= 1
                elif code[new_ptr] == "+":
                    mem_plus.append(data_ptr+shift)
                elif code[new_ptr] == "-":
                    if not shift:
                        base_changes += 1
                    mem_minus.append(data_ptr+shift)
                elif code[new_ptr] == "]" and not shift and (mem_plus or mem_minus):
                    success = True
                    break
                else:
                    break
            if success:
                actions = dict()
                for cptr in mem_minus:
                    if cptr not in actions:
                        actions[cptr] = -1
                    else:
                        actions[cptr] -= 1
                for cptr in mem_plus:
                    if cptr not in actions:
                        actions[cptr] = 1
                    else:
                        actions[cptr] += 1
                bracket_partners[ptr] = new_ptr
                def calc_brackets():
                    global ptr
                    global memory
                    global data_ptr
                    global symbols
                    global calc_rejects
                    if data_ptr != data_start:
                        calc_rejects.add(ptr)
                        symbols['[']()
                        return
                    value = memory[data_ptr]//base_changes
                    for cptr in actions:
                        while cptr >= len(memory):
                            memory.append(0)
                        memory[cptr] = (memory[cptr] + value * actions[cptr])%256
                    ptr = new_ptr+1
                functions[ptr] = calc_brackets
                calc_brackets()
                return
            
        def lb_default():
            global ptr
            global bracket_partners
            global code
            global memory
            global data_ptr
            if not memory[data_ptr]:
                if ptr in bracket_partners:
                    ptr = bracket_partners[ptr]+1
                else:
                    start = ptr
                    open_brackets = 1
                    while open_brackets > 0:
                        ptr += 1
                        if code[ptr] == '[':
                            open_brackets += 1
                        elif code[ptr] == ']':
                            open_brackets -= 1
                    bracket_partners[start] = ptr
                    bracket_partners[ptr] = start
                    ptr += 1
            else:
                ptr += 1
        functions[ptr] = lb_default
        lb_default()
symbols['['] = lb

def rb():
    global functions
    global ptr
    def rb_default():
        global memory
        global ptr
        global data_ptr
        global code
        global bracket_partners
        if memory[data_ptr]:
            if ptr in bracket_partners:
                ptr = bracket_partners[ptr]
            else:
                start = ptr
                close_brackets = 1
                while close_brackets > 0:
                    ptr -= 1
                    if code[ptr] == '[':
                        close_brackets -= 1
                    elif code[ptr] == ']':
                        close_brackets += 1
                bracket_partners[start] = ptr
                bracket_partners[ptr] = start
        ptr += 1
    functions[ptr] = rb_default
    rb_default()
symbols[']'] = rb

def d():
    global memory
    global data_ptr
    global ptr
    global plant_info
    global info_ptr
    if memory[data_ptr] == 0:
        till()
        plant_info = []
        info_ptr = 0
    elif memory[data_ptr] == 1:
        harvest()
        plant_info = []
        info_ptr = 0
    elif memory[data_ptr] == 2:
        clear()
        plant_info = []
        info_ptr = 0
    elif memory[data_ptr] >= 4 and memory[data_ptr] < 8:
        move(moves[memory[data_ptr]])
        plant_info = []
        info_ptr = 0
    elif memory[data_ptr] >= 128 and memory[data_ptr] < 135:
        plant(plants_write[memory[data_ptr]])
        plant_info = []
        info_ptr = 0
    elif memory[data_ptr] >= 64 and memory[data_ptr] < 67:
        use_item(items[memory[data_ptr]],1)
        plant_info = []
        info_ptr = 0
    elif memory[data_ptr] >= 32 and memory[data_ptr] < 36:
        swap(swap_moves[memory[data_ptr]])
        plant_info = []
        info_ptr = 0
    elif memory[data_ptr] == 68:
        use_item(Items.Weird_Substance, substance)
    elif memory[data_ptr] == 69:
        change_hat(Hats.Straw_Hat)
        plant_info = []
        info_ptr = 0
    elif memory[data_ptr] == 70:
        change_hat(Hats.Dinosaur_Hat)
        plant_info = []
        info_ptr = 0
    ptr += 1
symbols['.'] = d

def c():
    global memory
    global data_ptr
    global ptr
    global plant_info
    global info_ptr
    global moves
    global next_pumpkin_number
    if get_entity_type() == Entities.Dead_Pumpkin:
        plant_info = []
        info_ptr = 0
    if len(plant_info) > 1:
        memory[data_ptr] = plant_info[info_ptr]
        info_ptr = info_ptr + 1
        if len(plant_info) > 1 and info_ptr >= len(plant_info):
            plant_info = []
            info_ptr = 0
        ptr += 1
        return
    elif not plant_info:
        plant_type = get_entity_type()
        if plant_type == Entities.Hedge or plant_type == Entities.Treasure: #in mazes return chest coordinates and available moves
            plant_info.append(left_shift(plants_read[plant_type],2))
            plant_info.append(get_pos_x())
            plant_info.append(get_pos_y())
            plant_info.append(can_move(North)*1+can_move(East)*2+can_move(South)*4+can_move(West)*8)
        elif plant_type == None: #when on an empty tile return move directions for use in dinosaur code
            water_level = get_water() * 4 // 1
            if water_level == 4:
                water_level = 3
            tilled = 1
            harvestable = 0
            water_level_shifted = left_shift(water_level,6)
            plant_type_shifted = 0
            first_byte = water_level_shifted + plant_type_shifted + left_shift(tilled,1) + harvestable
            plant_info.append(first_byte)
            plant_info.append(can_move(North)*1+can_move(East)*2+can_move(South)*4+can_move(West)*8)
        elif plant_type == Entities.Apple: #When on apple first return possible moves to emulate empty tile, then return next location
            water_level = get_water() * 4 // 1
            if water_level == 4:
                water_level = 3
            tilled = 1
            harvestable = 0
            water_level_shifted = left_shift(water_level,6)
            plant_type_shifted = left_shift(plants_read[plant_type],2)
            first_byte = water_level_shifted + plant_type_shifted + left_shift(tilled,1) + harvestable
            plant_info.append(first_byte)
            x, y = measure()
            plant_info.append(can_move(North)*1+can_move(East)*2+can_move(South)*4+can_move(West)*8)
            plant_info.append(x)
            plant_info.append(y)
        else:
            water_level = get_water() * 4 // 1
            if water_level == 4:
                water_level = 3
            tilled = 0
            if get_ground_type() == Grounds.Soil:
                tilled = 1
            harvestable = 0
            if can_harvest():
                harvestable = 1
            water_level_shifted = left_shift(water_level,6)
            plant_type_shifted = left_shift(plants_read[plant_type],2)
            first_byte = water_level_shifted + plant_type_shifted + left_shift(tilled,1) + harvestable
            plant_info.append(first_byte)
        memory[data_ptr] = plant_info[0]
        info_ptr = info_ptr + 1
        ptr += 1
        return

    else:
        plant_type = get_entity_type()
        if plant_type in plants_with_companions:
            companion, (x, y) = get_companion()
            plant_info.append(plants_read[companion])
            plant_info.append(x)
            plant_info.append(y)
        elif plant_type in plants_with_values:
            center = measure()
            north = measure(North)
            east = measure(East)
            south = measure(South)
            west = measure(West)
            plant_info.append(center)
            plant_info.append(north)
            plant_info.append(east)
            plant_info.append(south)
            plant_info.append(west)
        elif plant_type == Entities.Pumpkin:
            center = measure()
            if center not in pumpkin_numbers:
                if len(known_pumpkins) == 256:
                    old_pumpkin = known_pumpkins[next_pumpkin_number]
                    pumpkin_numbers.pop(old_pumpkin)
                    known_pumpkins[next_pumpkin_number] = center
                    pumpkin_numbers[center] = next_pumpkin_number
                else:
                    pumpkin_numbers[center] = next_pumpkin_number
                    known_pumpkins.append(center)
                next_pumpkin_number = (next_pumpkin_number + 1) % 256
            plant_info.append(pumpkin_numbers[center])  
            north = measure(North)
            if north not in pumpkin_numbers:
                if len(known_pumpkins) == 256:
                    old_pumpkin = known_pumpkins[next_pumpkin_number]
                    pumpkin_numbers.pop(old_pumpkin)
                    known_pumpkins[next_pumpkin_number] = north
                    pumpkin_numbers[north] = next_pumpkin_number
                else:
                    pumpkin_numbers[north] = next_pumpkin_number
                    known_pumpkins.append(north)
                next_pumpkin_number = (next_pumpkin_number + 1) % 256
            plant_info.append(pumpkin_numbers[north])  
            east = measure(East)
            if east not in pumpkin_numbers:
                if len(known_pumpkins) == 256:
                    old_pumpkin = known_pumpkins[next_pumpkin_number]
                    pumpkin_numbers.pop(old_pumpkin)
                    known_pumpkins[next_pumpkin_number] = east
                    pumpkin_numbers[east] = next_pumpkin_number
                else:
                    pumpkin_numbers[east] = next_pumpkin_number
                    known_pumpkins.append(east)
                next_pumpkin_number = (next_pumpkin_number + 1) % 256
            plant_info.append(pumpkin_numbers[east])  
            south = measure(South)
            if south not in pumpkin_numbers:
                if len(known_pumpkins) == 256:
                    old_pumpkin = known_pumpkins[next_pumpkin_number]
                    pumpkin_numbers.pop(old_pumpkin)
                    known_pumpkins[next_pumpkin_number] = south
                    pumpkin_numbers[south] = next_pumpkin_number
                else:
                    pumpkin_numbers[south] = next_pumpkin_number
                    known_pumpkins.append(south)
                next_pumpkin_number = (next_pumpkin_number + 1) % 256
            plant_info.append(pumpkin_numbers[south])  
            west = measure(West)
            if west not in pumpkin_numbers: 
                if len(known_pumpkins) == 256:
                    old_pumpkin = known_pumpkins[next_pumpkin_number]
                    pumpkin_numbers.pop(old_pumpkin)
                    known_pumpkins[next_pumpkin_number] = west
                    pumpkin_numbers[west] = next_pumpkin_number
                else:
                    pumpkin_numbers[west] = next_pumpkin_number
                    known_pumpkins.append(west)
                next_pumpkin_number = (next_pumpkin_number + 1) % 256
            plant_info.append(pumpkin_numbers[west])
        memory[data_ptr] = plant_info[info_ptr]
        info_ptr = info_ptr + 1
        if len(plant_info) > 1 and info_ptr >= len(plant_info):
            plant_info = []
            info_ptr = 0
    ptr += 1
symbols[','] = c

def the_farmer_was_brainfucked(input):
    global code
    global code_length
    global ptr
    global symbols
    global functions
    global substance
    substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
    code = input
    code_length = len(code)
    ptr = 0
    while ptr < code_length:
        if ptr in functions:
            functions[ptr]()
        elif code[ptr] in symbols:
            symbols[code[ptr]]()
        if num_items(Items.Gold) == 616448:
            return

if __name__ == "__main__":
    set_world_size(8)
    # hay code
    hay = ">>>>>>>>[-]+++++>[-]++++<<<[-]+<<<<<<+[>++++++++[>,>[-]>[-]<<[>+>+<<-]>>[<<+>>-]<-----[>-<[-]]>+[>>.<<<<[-]>>[-]],<<<>>>>>>>.<<<<<<<-]<>>>>>>>>>.<<<<<<<<<]"
    # trees code
    trees = ">>>>+++++++++++++>+++++++++>>>>++++++++++++++++[>++++++++>++++++++<<-]>++>+>+++++>++++<<<<[-]+<<<<<<<+<<++++++++[>++++++++[>[>>>>>>>>.<<<<<<<-<-]>+[>>>>>>>>.<<<<<<<<<+>-]>>>>>>>>>.<<<<<<<<<<<-]>>>>>>>>>>>>.<<<<<<<<<<<[->+<]>[<->-]<+<<-]+[>++++++++[>>>[>>+>+<<<-]>>>[<<<+>>>-],[-<->]>[-]<<[>>-<<[-]]>>+[>.>.<<-]<<<[>+>+<<-]>>[<<+>>-],,,,[-<->]>[-]<<[>>-<<[-]]>>+[>.>>.<<<-]>>>>.<<<<<<<<<<<-]>>>>>>>>>>>>.<<<<<<<<<<<<<]"
    # carrot code
    carrots = ">>>>>>><[-]++++++++++++++++[>++++++++<-]>+++>[-]+++++>[-]++++<<<[-]+<[-]<<<<<+[>++++++++[>,>[-]>[-]<<[>+>+<<-]>>[<<+>>-]<-------------------[>-<[-]]>+[>>.>.<<<<<[-]>>[-]]<<>[-]>[-]<<[>+>+<<-]>>[<<+>>-]<----[>-<[-]]>+[>.>>.<<<<<[-]>>[-]]<<>[-]>[-]<<[>+>+<<-]>>[<<+>>-]<-----[>-<[-]]>+[>.>>.<<<<<[-]>>[-]]<<<>>>>>>>.<<<<<<<-]<>>>>>>>>>.<<<<<<<<<]"
    # cactus code
    cactus = ">>>>>>>>>>>><[-]++++++++++++++++[>++++++++<-]>+++++>[-]+++++++++++++++++++++++++++++++++>[-]++++++++++++++++++++++++++++++++>[]+++++>[-]++++<<<<<[-]+<[-]<<<<<<<<<<>++++++++[>++++++++[>>>>>>>>.>>.>>>.<<<<<<<<<<<<<-]>>>>>>>>>>>>>>.<<<<<<<<<<<<<<<-]<+[>++++++++[>+[->>>>>>>[-]<<<<<<+++++++[>,,>,,<>>>[-]>[-]<<[-]<<[>>>+<<[->>[-]>+<<<]>>[-<+>]>[-<<<+>>>]<<<-<-]>>[>>>+>>>>.<<<<<<<[-]]>>>>>>>>>.<<<<<<<<<<<<-]>>>>>>>>>>>>.<<<<<<[<<<<<<<+>>>>>>>[-]]<<<<<<<]>>>>>>>>>>>>>>.<<<<<<<<<<<<<<<-]++++++++[>+[->>>>>>>[-]<<<<<<+++++++[>,,>,<>>>[-]>[-]<<[-]<<[>>>+<<[->>[-]>+<<<]>>[-<+>]>[-<<<+>>>]<<<-<-]>>[>>>+>>>>>.<<<<<<<<[-]]>>>>>>>>>>.<<<<<<<<<<<<<-]>>>>>>>>>>>>>.<<<<<<<[<<<<<<<+>>>>>>>[-]]<<<<<<<]>>>>>>>>>>>>>.<<<<<<<<<<<<<<-]>>>>>>>>>>.<<<<<<<<<<++++++++[>++++++++[>>>>>>>>>>.>>>.<<<<<<<<<<<<<-]>>>>>>>>>>>>>>.<<<<<<<<<<<<<<<-]<]"
    # pumpkin code
    pumpkins = ">>>>+++++++++++++++++++++++>>>>>>><[-]++++++++++++++++[>++++++++<-]>++++>+++++>++++<<<[-]+<[-]<<<<<<<<<++++++++[>++++++++[>>>>>>>>.>>.>.<<<<<<<<<<<-]>>>>>>>>>>>>.<<<<<<<<<<<<<-]+[>+[->++++++++[>++++++++[>>[-]>[-]>[-]<<<[>+>+<<-]>>[<<+>>-],[-<->]<[>>+<<[-]]>>[>>>>.<<<<[-]]>>>>>.<<<<<<<<<-]>>>>>>>>>>.<<<<<<<<<<<-]>>[>+>+<<-]>>[<<+>>-],[-<->]<[>>-<<<<<<+>>>>[-]]>>+[<<,>,,,[-<->]<[<<<<+>>>>[-]],>>[-]]<<<<<<]>>>>>>>>>.<<<<<<<<<++++++++[>++++++++[>>>>>>>>>.>.<<<<<<<<<<-]>>>>>>>>>>>.<<<<<<<<<<<<-]<]"
    # dinosaur code
    bones = ">>>>>>>>+++++++++++[>++++++>++++++<<-]>++++>+++<<[-]+++++++<++++++<+++++<++++<<<<<+[>>>>>>>>>.<........<........<<<<<<+[>>>>>.<<<<++++[>>>>......<.>>>......<<<.<<<-]>>>>>>.<.......<<<<<<,,]>>>>>>>>>.<<<<<<<<<<]"
    # maze code
    treasure = ">>>>>>>>>>>>>++++++++[>++++++++++++++++<-]>+>>++++++++[<++++++++>-]<++++>+<<<<<<<<<<<<<<<<+[>>>>>>>>>>>>>>.>.<<<<<<<<<<<<<<,>++++[<---------->-]<[[-]>,,,>++<[->>>>>[-<]+<--[++<--]++<]>[-]>[>>>>>>>+++++++<<<<<<<-]>[>>>>>++++++<<<<<-]>[>>>+++++<<<-]>[>++++<-]>>>>>>[-]<[<<<<[<+>-]>[<+>-]>[<+>-]>[<+>-]<<<<[>>>>+<<<<-]>>>>>>+<-]>[<+>-]<<<<<[.>[-]>[-]>[-]>+++<<<<[-]]>[.>[-]>[-]<<[-]]>[.>[-]>+<<[-]]>[.>++<[-]]>[>+<<<<<<<<<<+>>>>>>>>>-]<<<<<<<<++++<>>>[-]>[-]<<[-]<<[>>>+<<[->>[-]>+<<<]>>[-<+>]>[-<<<+>>>]<<<-<-]>[>-<[-]]>+[>>>>>>>----<<<<<<<[-]]>>>>>>>>[<+>-]<<<<<<<<<<<<,>++++[<---------->-]<]>>>>>>>>>>>>>>>.<<<<<<<<<<<<<<<<]"
    the_farmer_was_brainfucked(pumpkins)
