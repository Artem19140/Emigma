import random
import string

def SteckerbrettMachen():
    random_alphabet = list(string.ascii_uppercase)  
    random.shuffle(random_alphabet)  
    random_order = ''.join(random_alphabet)
    return(random_order)

def LetterChanger(List1, List2, msg, increment):
    Index = List1.index(msg[increment])
    Buchstabe = List2[Index]
    return Buchstabe 

def RotorStartPosition(Position):
    Order = []
    for i in range(0, len(Position)):
        Order.append(int(Position[i]))
    return Order

Eintrittswalze = ""

def Steckerbrett(PlugPosition):
    PPZwei =PlugPosition[::-1]

    PlugOrder = []
    for l in range(0, len(PlugPosition), 2):
        PlugOrder.append((PlugPosition[l], PlugPosition[l+1]))
    for k in range(0, len(PPZwei), 2):
        PlugOrder.append((PPZwei[k], PPZwei[k+1]))
    return PlugOrder

def replaceElements(msg, PlugOrder):
    msg_list = list(msg)
    
    for i in range(len(msg_list)):
        for pair in PlugOrder:
            if msg_list[i] == pair[0]: 
                msg_list[i] = pair[1] 
                break  
    return ''.join(msg_list)

def Cipher(msg, Position, Nummer1, Nummer2, Nummer3, PlugPosition):
    Umkehrwalze = "AYBRCUDHEQFSGLIPJXKNMOTZVW"
    
    rotorEinz = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotorEinzNotch = "Q"
    
    rotorZwei = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    rotorZweiNotch = "E"
    
    rotorDrei = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    rotorDreiNotch = "V"

    rotors = [rotorEinz,rotorZwei,rotorDrei, rotorEinzNotch,  rotorZweiNotch,
               rotorDreiNotch, Umkehrwalze]
    
    UmkehrwalzeList = []
    for i in range(len(Umkehrwalze)//2):
        UmkehrwalzeList.append((Umkehrwalze[i], Umkehrwalze[i+13] ))
        UmkehrwalzeList.append((Umkehrwalze[i+13], Umkehrwalze[i] ))
    
    RSP = list(str(int(Position)-111))
    if len(RSP) <3:
        RSP.insert(0, '0')
    
    
    cipher_msg = msg
    Plugs = Steckerbrett(PlugPosition)
    cipher_msg = replaceElements(cipher_msg, Plugs)
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    STRList = list(rotors[int(RSP[0])])
    R1R2List = list(rotors[int(RSP[1])])
    R2R3List = list(rotors[int(RSP[2])])
    ALIST = list(ALPHABET)
    old_msg = []
    new_msg = []
    for i in range(0, len(msg)):
        if cipher_msg[i] == " ":
            old_msg.append(" ")
        else:
            old_msg.append(LetterChanger(ALIST, STRList, cipher_msg, i))
            old_msg[i] = (LetterChanger(STRList, R1R2List, old_msg, i))
            old_msg[i] = (LetterChanger(R1R2List, R2R3List, old_msg, i))
        STRList = STRList[-13:] + STRList[:-13]
        R1R2List = R1R2List[-13:] + R1R2List[:-13]
        R2R3List = R2R3List[-13:] + R2R3List[:-13]
        if old_msg[i] == " ":
            new_msg.append(" ")
        else:
            new_msg.append(LetterChanger(R2R3List, R1R2List, old_msg, i))
            R2R3List = R2R3List[-1:] + R2R3List[:-1]
            if Nummer3 != len(rotorDrei)-1:
                Nummer3 += 1
            else:
                Nummer3 = 0
            if rotors[int(RSP[2])][Nummer3] != rotors[int(RSP[2])+3]:
                if Nummer2  != len(rotorDrei)-1:
                    Nummer2 +=1
                else:
                    Nummer2 = 0
            else:
                if rotors[int(RSP[1])][Nummer2] != rotors[int(RSP[1])+3]:
                    if Nummer1  != len(rotorEinz)-1:
                        Nummer1 +=1
                    else:
                        Nummer1 = 0
                    if Nummer3 != len(rotorEinz)-1:
                        Nummer3 += 1
                    else:
                        Nummer3 = 0
            new_msg[i] = (LetterChanger(R1R2List, STRList, new_msg, i))
            R1R2List = R1R2List[-1:] + R1R2List[:-1]
            if rotors[int(RSP[1])][Nummer2] != rotors[int(RSP[1])+3]:
                if Nummer1  != len(rotorEinz)-1:
                    Nummer1 +=1
                else:
                    Nummer1 = 0
            new_msg[i] = (LetterChanger(STRList, ALIST, new_msg, i))
            STRList = STRList[-1:] + STRList[:-1]
            
    preResult = ""
    for l in range (0, len(new_msg)):
        preResult = preResult + str(new_msg[l])
    cipher_msg = preResult
    
    cipher_msg = replaceElements(cipher_msg, Plugs)
    
    return cipher_msg

def Decipher(msg, Position, Nummer1, Nummer2, Nummer3, PlugPosition):

    Umkehrwalze = "AYBRCUDHEQFSGLIPJXKNMOTZVW"
    rotorEinz = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotorEinzNotch = "Q"
    rotorZwei = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    rotorZweiNotch = "E"
    rotorDrei = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    rotorDreiNotch = "V"

    rotors = [rotorEinz,rotorZwei,rotorDrei, rotorEinzNotch,  rotorZweiNotch,
               rotorDreiNotch, Umkehrwalze]
    
    UmkehrwalzeList = []
    for i in range(len(Umkehrwalze)//2):
        UmkehrwalzeList.append((Umkehrwalze[i], Umkehrwalze[i+13] ))
        UmkehrwalzeList.append((Umkehrwalze[i+13], Umkehrwalze[i] ))
    
    RSP = list(str(int(Position)-111))
    if len(RSP) <3:
        RSP.insert(0, '0')
    
    
    cipher_msg = msg
    Plugs = Steckerbrett(PlugPosition)
    cipher_msg = replaceElements(cipher_msg, Plugs)
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    STRList = list(rotors[int(RSP[0])])
    R1R2List = list(rotors[int(RSP[1])])
    R2R3List = list(rotors[int(RSP[2])])
    STRList = STRList[13:] + STRList[:13]
    R1R2List = R1R2List[-13:] + R1R2List[:-13]
    R2R3List = R2R3List[-13:] + R2R3List[:-13]
    ALIST = list(ALPHABET)
    old_msg = []
    new_msg = []
    for i in range(0, len(msg)):
        if cipher_msg[i] == " ":
            old_msg.append(" ")
        else:
            old_msg.append(LetterChanger(ALIST, STRList, cipher_msg, i))
            old_msg[i] = (LetterChanger(STRList, R1R2List, old_msg, i))
            old_msg[i] = (LetterChanger(R1R2List, R2R3List, old_msg, i))
        STRList = STRList[13:] + STRList[:13]
        R1R2List = R1R2List[13:] + R1R2List[:13]
        R2R3List = R2R3List[13:] + R2R3List[:13]
        if old_msg[i] == " ":
            new_msg.append(" ")
        else:
            new_msg.append(LetterChanger(R2R3List, R1R2List, old_msg, i))
            R2R3List = R2R3List[-1:] + R2R3List[:-1]
            if Nummer3 != len(rotorDrei)-1:
                Nummer3 += 1
            else:
                Nummer3 = 0
            if rotors[int(RSP[2])][Nummer3] != rotors[int(RSP[2])+3]:
                if Nummer2  != len(rotorDrei)-1:
                    Nummer2 +=1
                else:
                    Nummer2 = 0
            else:
                if rotors[int(RSP[1])][Nummer2] != rotors[int(RSP[1])+3]:
                    if Nummer1  != len(rotorEinz)-1:
                        Nummer1 +=1
                    else:
                        Nummer1 = 0
                    if Nummer3 != len(rotorEinz)-1:
                        Nummer3 += 1
                    else:
                        Nummer3 = 0
            new_msg[i] = (LetterChanger(R1R2List, STRList, new_msg, i))
            R1R2List = R1R2List[-1:] + R1R2List[:-1]
            if rotors[int(RSP[1])][Nummer2] != rotors[int(RSP[1])+3]:
                if Nummer1  != len(rotorEinz)-1:
                    Nummer1 +=1
                else:
                    Nummer1 = 0
            new_msg[i] = (LetterChanger(STRList, ALPHABET, new_msg, i))
            STRList = STRList[-1:] + STRList[:-1]    
    preResult = ""
    for l in range (0, len(new_msg)):
        preResult = preResult + str(new_msg[l])
    cipher_msg = preResult
    cipher_msg = replaceElements(cipher_msg, Plugs)
    return cipher_msg