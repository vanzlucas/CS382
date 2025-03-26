# Names: James Schorle and Lucas Vanzelli
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Project 2

def instruction_breakdown(line):
    #instructions named after our special people
    instructions = {"KISS":"001", "DIVORCE":"011", "LOG":"110", "SNATCH_IMM": "010", "SNATCH_ADR": "100",}
    #ADD, SUB, STR, LDR (Immediate), LDR (Address) respectively

    #boring registers
    registers = {"X1": "00", "X2": "01", "X3": "10", "X4": "11"}

    #line split
    parts = line.split()
    if len(parts) < 2:
        return None

    #instruction split
    op = parts[0].upper()
    target = registers.get(parts[1].strip(","), "00")

    #instructions

    #loads an immediate
    if op == "SNATCH_IMM":
        if len(parts) == 3:
            opcode = instructions["SNATCH_IMM"]
            immediate = format(int(parts[2], 0), "08b")
            return f"000{opcode}{immediate}{target}"
        
    #loads a value stored at an address
    elif op == "SNATCH_ADR":
        if len(parts) == 3:
            opcode = instructions["SNATCH_ADR"]
            address = format(int(parts[2], 0), "08b")
            return f"000{opcode}{address}{target}"
        
    #stores a value into memory
    elif op == "LOG":
        if len(parts) == 3:
            opcode = instructions["LOG"]
            address = format(int(parts[2], 0), "08b")  
            return f"000{opcode}{address}{target}" 
        
    #addition or subtraction
    elif op in ("KISS", "DIVORCE"):
        if len(parts) == 4:
            input1 = registers.get(parts[2].strip(","), "00") 
            input2 = registers.get(parts[3], "00")  
            opcode = instructions[op]
            return f"000{opcode}0000{input1}{input2}{target}"

    return None

#binary -> hex
def binary_to_hex(binary_str):
    return f"{int(binary_str, 2):04X}"

#makes the output_file from the input_file 
def makes_file(input_file, output_file):
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            line = line.strip()
            if not line or line.startswith(".") or line.endswith(":"):
                continue
            
            #prints instruction
            print(line)
            
            binary_line = instruction_breakdown(line)
            if binary_line:
                hex_line = binary_to_hex(binary_line) 
                print(hex_line)
                outfile.write(hex_line + "\n")

#function call
input = "crankypants.pookie"
output = "poopypants.pookieout"
makes_file(input, output)


