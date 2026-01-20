def convertBinToHex(bin):
    hex =" "
    if bin == "0000":
        hex = "0"
    elif bin == "0001":
        hex = "1"
    elif bin == "0010":
        hex = "2"
    elif bin == "0011":
        hex = "3"
    elif bin == "0100":
        hex = "4"
    elif bin == "0101":
        hex = "5"
    elif bin == "0110":
        hex = "6"
    elif bin == "0111":
        hex = "7"
    elif bin == "1000":
        hex = "8"
    elif bin == "1001":
        hex = "9"
    elif bin == "1010":
        hex = "A"
    elif bin == "1011":
        hex = "B"
    elif bin == "1100":
        hex = "C"
    elif bin == "1101":
        hex = "D"
    elif bin == "1110":
        hex = "E"
    elif bin == "1111":
        hex = "F"
    elif bin == "00000":
        hex = "0"
    elif bin == "00001":
        hex = "1"
    elif bin == "00010":
        hex = "2"
    elif bin == "00011":
        hex = "3"
    elif bin == "00100":
        hex = "4"
    elif bin == "00101":
        hex = "5"
    elif bin == "00110":
        hex = "6"
    elif bin == "00111":
        hex = "7"
    elif bin == "01000":
        hex = "8"
    elif bin == "01001":
        hex = "9"
    elif bin == "01010":
        hex = "A"
    elif bin == "01011":
        hex = "B"
    elif bin == "01100":
        hex = "C"
    elif bin == "01101":
        hex = "D"
    elif bin == "01110":
        hex = "E"
    elif bin == "01111":
        hex = "F"
    return hex


#check opcode
def checkInstruction(inst):
    convertInstruction = " "
    if inst == "addi":
        convertInstruction = "0001"
    elif  inst == "beq":
        convertInstruction = "0010"
    elif inst == "bne":
        convertInstruction = "0011"
    elif inst == "sw":
        convertInstruction = "0100"
    elif inst == "jmp":
        convertInstruction = "0101"
    elif inst == "lw":
        convertInstruction = "0110"
    else:
        convertInstruction = "Invalid instrcutions"
    return convertInstruction

#create function to check rtype function bit 
def checkFunction(func):
    convertInstruction = " "
    if func == "nop":
        convertInstruction = "0001"
    elif  func == "nor":
        convertInstruction = "0010"
    elif func == "or":
        convertInstruction = "0011"
    elif func == "add":
        convertInstruction = "0100"
    elif func == "srl":
        convertInstruction = "0101"
    elif func == "slt":
        convertInstruction = "0110"
    elif func == "sll":
        convertInstruction = "0111"
    elif func == "sub":
        convertInstruction = "1000"
    elif func == "and":
        convertInstruction = "1001"
    else:
        convertInstruction = "Invalid instrcutions"
    return convertInstruction

#change register number to r0 to r15
def checkRegister(reg):
    convertReg = ""
    if  reg == "$r0": 
        convertReg ="00000" 
    elif reg == "$r1":
        convertReg ="00001"
    elif reg == "$r2":
        convertReg ="00010"
    elif reg == "$r3":
        convertReg ="00011"
    elif reg == "$r4":
        convertReg ="00100"
    elif reg == "$r5":
        convertReg ="00101"
    elif reg == "$r6":
        convertReg ="00110"
    elif reg == "$r7":
        convertReg ="00111"
    elif reg == "$r8":
        convertReg ="01000"
    elif reg == "$r9":
        convertReg ="01001"
    elif reg == "$r10":
        convertReg ="01010"
    elif reg == "$r11":
        convertReg ="01011"
    elif reg == "$r12":
        convertReg ="01100"
    elif reg == "$r13":
        convertReg ="01101"
    elif reg == "$r14":
        convertReg ="01110"
    elif reg == "$r15":
        convertReg ="01111"
    elif reg == "$r16":
        convertReg ="10000"
    elif reg == "$r17":
        convertReg ="10001"
    elif reg == "$r18":
        convertReg ="10010"
    elif reg == "$r19":
        convertReg ="10011"
    elif reg == "$r20":
        convertReg ="10100"
    elif reg == "$r21":
        convertReg ="10101"
    elif reg == "$r22":
        convertReg ="10110"
    elif reg == "$r23":
        convertReg ="10111"
    else:
        convertReg =="Invalid Register"
    return convertReg


def decimalToBinary(num):
    if num < 0:
        num = 1024 + num  # Handle negative numbers using 10-bit two's complement (1024 = 2^10)

    ext = ""
    result = ""
    
    while num > 0:
        if num % 2 == 0:
            result = "0" + result
        else:
            result = "1" + result
        num = num // 2

    for i in range(10 - len(result)):  # Pad with leading zeros to make it 10 bits
        ext = "0" + ext

    result = ext + result
    return result

def decimalToBinary20Bits(num):
    if num < 0 or num > 1048575:  # Ensure the number is within the valid range for 20 bits
        raise ValueError("Input must be a non-negative integer within the range 0 to 1048575.")

    # Convert the number to binary and pad with leading zeros to make it 20 bits
    result = bin(num)[2:]  # Remove the '0b' prefix from binary representation
    result = result.zfill(20)  # Pad with leading zeros to ensure it's 20 bits long
    
    return result


readf = open("inputs", "r")
writef = open("outputs", "w")
writef.write("v2.0 raw\n")

# Process each line in the input file
for i in readf:
    splitted = i.split()

    # Handle R-type instructions
    if splitted[0] in ["sub", "and", "nop", "nor", "or", "add", "srl", "slt", "sll"]:
        # Construct the 24-bit binary representation
        opcode = "0000"  # Default opcode for R-type
        rs = checkRegister(splitted[2])  # 5-bit binary for rs
        rt = checkRegister(splitted[3])  # 5-bit binary for rt
        rd = checkRegister(splitted[1])  # 5-bit binary for rd
        shampt = "1"  # Default 1-bit shampt
        func = checkFunction(splitted[0])  # 4-bit binary for function

        # Combine to form the complete 24-bit binary string
        r_binary = opcode + rs + rt + rd + shampt + func

        # Divide the binary string into 4-bit chunks and convert to hex
        hex_output = ""
        for j in range(0, 24, 4):  # Iterate over the 24-bit binary string in steps of 4 bits
            binary_chunk = r_binary[j:j+4]
            hex_output += convertBinToHex(binary_chunk)  # Convert the 4-bit binary to hex

        # Write the hex output to the file
        print(hex_output)
        writef.write(hex_output + "\n")



    # for i type instruction
    elif(splitted[0] == "lw" or splitted[0] == "addi" or splitted[0] == "beq" or splitted[0] == "bne" or splitted[0] == "sw"):
        conv_inst = checkInstruction(splitted[0])
        conv_rt = checkRegister(splitted[1])
        conv_rs = checkRegister(splitted[2])
        conv_im = decimalToBinary(int(splitted[3]))

        i_binary = conv_inst + conv_rs + conv_rt + conv_im

        # Divide the binary string into 4-bit chunks and convert to hex
        hex_output = ""
        for j in range(0, 24, 4):  # Iterate over the 24-bit binary string in steps of 4 bits
            binary_chunk = i_binary[j:j+4]
            hex_output += convertBinToHex(binary_chunk)  # Convert the 4-bit binary to hex

        # Write the hex output to the file
        print(hex_output)
        writef.write(hex_output + "\n")  
     
    #  for j type instruction
    elif(splitted[0] == "jmp"):
        conv_inst = checkInstruction(splitted[0])
        address = decimalToBinary20Bits(int(splitted[1]))
        # Combine to form the complete 24-bit binary string
        j_binary = conv_inst + address
        # Divide the binary string into 4-bit chunks and convert to hex
        hex_output = ""
        for j in range(0, 24, 4):  # Iterate over the 24-bit binary string in steps of 4 bits
            binary_chunk = j_binary[j:j+4]
            hex_output += convertBinToHex(binary_chunk)  # Convert the 4-bit binary to hex
        # Write the hex output to the file
        print(hex_output)
        writef.write(hex_output + "\n")