import sys
def doubl(ipadd):
    octet = [0] * 8
    for i in range(1, len(octet) + 1):
        if ipadd % 2 == 0:
            octet[-i] = 0
        else:
            octet[-i] = 1
        ipadd = ipadd // 2
    return (octet)
def mask_doubl(mask, maskDouble):
    for i in range(0, len(maskDouble)):
        if i < mask:
            maskDouble[i] = 1
        else:
            maskDouble[i] = 0

def mask_apply(octet, maskDouble):
    for i in range(0,8):
        if octet[i] == maskDouble[i]:
            continue
        else:
            octet[i] = 0
def broadcast(octet, maskDouble):
    for i in range(0,8):
        if maskDouble[i] == 1:
            continue
        else:
            octet[i] = 1
def undouble(octet):
    add = 0
    for i in range (1,9):
        add += (2 ** (i - 1)) * octet[-i]
    return (add)
def console(user_input):
    if user_input == 'exit' or user_input == 'EXIT':
        sys.exit()
while True:
    print('Enter source IPv4 Address in format: x.x.x.x or type exit to leave')
    IPaddress = input()
    console(IPaddress)
    try:
        a, b, c, d = map(int, IPaddress.split('.'))
        if a > 255 or b > 255 or c > 255 or d > 255:
            print ('Wrong value, octets cannot be higher than 255')
            continue
    except ValueError:
        print ('Wrong value')
        continue
    octet1 = doubl(a)
    octet2 = doubl(b)
    octet3 = doubl(c)
    octet4 = doubl(d)
    print('Subnet source mask in format /x')
    while True:
        try:
            maskstart = input()
            console(maskstart)
            if maskstart[0] == '/' or maskstart[0] == ':':
                maskstart = str.replace(maskstart, '/', '')
                maskstart = str.replace(maskstart, ':', '')
            mask = int(maskstart)
        except ValueError:
            print ('Wrong value, try again')
            continue
        if int(mask) < 32:
            maskDouble = [0] * 32
            maskDouble1 = [0] * 8
            maskDouble2 = [0] * 8
            maskDouble3 = [0] * 8
            maskDouble4 = [0] * 8
            mask_doubl(mask, maskDouble)
            for i in range(0, 32):
                if i <= 7:
                    maskDouble1 [i] = maskDouble [i]
                elif i <= 15:
                    maskDouble2 [i - 8] = maskDouble [i]
                elif i <= 23:
                    maskDouble3 [i - 16] = maskDouble [i]
                elif i <= 32:
                    maskDouble4 [i - 24] = maskDouble [i]
            e = undouble(maskDouble1)
            f = undouble(maskDouble2)
            g = undouble(maskDouble3)
            h = undouble(maskDouble4)
            print ('IP address: ')
            print(a, b, c, d, sep='.')
            print ('Mask:')
            print (e,f,g,h, sep = '.')
            mask_apply(octet1, maskDouble1)
            mask_apply(octet2, maskDouble2)
            mask_apply(octet3, maskDouble3)
            mask_apply(octet4, maskDouble4)
            subnetOctet1 = undouble(octet1)
            subnetOctet2 = undouble(octet2)
            subnetOctet3 = undouble(octet3)
            subnetOctet4 = undouble(octet4)
            print('Subnet: ')
            print(subnetOctet1, subnetOctet2, subnetOctet3, subnetOctet4, sep = '.')
            print('Hostmin: ')
            print(subnetOctet1, subnetOctet2, subnetOctet3, subnetOctet4 + 1, sep ='.')
            print('Hostmax: ')
            broadcast(octet1, maskDouble1)
            broadcast(octet2, maskDouble2)
            broadcast(octet3, maskDouble3)
            broadcast(octet4, maskDouble4)
            broadcastOctet1 = undouble(octet1)
            broadcastOctet2 = undouble(octet2)
            broadcastOctet3 = undouble(octet3)
            broadcastOctet4 = undouble(octet4)
            print(broadcastOctet1, broadcastOctet2, broadcastOctet3, broadcastOctet4 - 1, sep ='.')
            print('Broadcast: ')
            print(broadcastOctet1, broadcastOctet2, broadcastOctet3, broadcastOctet4, sep ='.')
            print('Number of usable hosts: ')
            if mask == 31:
                print(2)
            else:
                numberOfHosts = ((2 ** (32 - mask)) - 2)
                print(numberOfHosts)
        elif mask == 32:
            print('nothing to subtract')
        else:
            print('Wrong mask value try again')
            continue
        break
    print('Enter  IPv4 Address to subtract in format: x.x.x.x or type exit to leave')
    IPaddress_subtract = input()
    console(IPaddress_subtract)
    try:
        a_subtract, b_subtract, c_subtract, d_subtract = map(int, IPaddress_subtract.split('.'))
        if a_subtract > 255 or b_subtract > 255 or c_subtract > 255 or d_subtract > 255:
            print('Wrong value, octets cannot be higher than 255')
            continue
    except ValueError:
        print('Wrong value')
        continue
    octet1_subtract = doubl(a_subtract)
    octet2_subtract = doubl(b_subtract)
    octet3_subtract = doubl(c_subtract)
    octet4_subtract = doubl(d_subtract)
    print('Subnet source mask in format /x')
    while True:
        try:
            maskstart_subtract = input()
            console(maskstart_subtract)
            if (maskstart_subtract[0] == '/' or maskstart_subtract[0] == ':'):
                maskstart_subtract = str.replace(maskstart_subtract, '/', '')
                maskstart_subtract = str.replace(maskstart_subtract, ':', '')
            mask_subtract = int(maskstart_subtract)
        except ValueError:
            print('Wrong value, try again')
            continue
        if int(mask_subtract) < 32:
            maskDouble_subtract = [0] * 32
            maskDouble1_subtract = [0] * 8
            maskDouble2_subtract = [0] * 8
            maskDouble3_subtract = [0] * 8
            maskDouble4_subtract = [0] * 8
            mask_doubl(mask_subtract, maskDouble_subtract)
            for i in range(0, 32):
                if i <= 7:
                    maskDouble1_subtract[i] = maskDouble_subtract[i]
                elif i <= 15:
                    maskDouble2_subtract[i - 8] = maskDouble_subtract[i]
                elif i <= 23:
                    maskDouble3_subtract[i - 16] = maskDouble_subtract[i]
                elif i <= 32:
                    maskDouble4_subtract[i - 24] = maskDouble_subtract[i]
            e_subtract = undouble(maskDouble1_subtract)
            f_subtract = undouble(maskDouble2_subtract)
            g_subtract = undouble(maskDouble3_subtract)
            h_subtract = undouble(maskDouble4_subtract)
            mask_apply(octet1_subtract, maskDouble1_subtract)
            mask_apply(octet2_subtract, maskDouble2_subtract)
            mask_apply(octet3_subtract, maskDouble3_subtract)
            mask_apply(octet4_subtract, maskDouble4_subtract)
            subnetOctet1_subtract = undouble(octet1_subtract)
            subnetOctet2_subtract = undouble(octet2_subtract)
            subnetOctet3_subtract = undouble(octet3_subtract)
            subnetOctet4_subtract = undouble(octet4_subtract)
            broadcast(octet1_subtract, maskDouble1_subtract)
            broadcast(octet2_subtract, maskDouble2_subtract)
            broadcast(octet3_subtract, maskDouble3_subtract)
            broadcast(octet4_subtract, maskDouble4_subtract)
            broadcastOctet1_subtract = undouble(octet1_subtract)
            broadcastOctet2_subtract = undouble(octet2_subtract)
            broadcastOctet3_subtract = undouble(octet3_subtract)
            broadcastOctet4_subtract = undouble(octet4_subtract)
        elif int(mask_subtract) == 32:
            broadcastOctet1_subtract = a_subtract
            broadcastOctet2_subtract = b_subtract
            broadcastOctet3_subtract = c_subtract
            broadcastOctet4_subtract = d_subtract
            subnetOctet1_subtract = a_subtract
            subnetOctet2_subtract = b_subtract
            subnetOctet3_subtract = c_subtract
            subnetOctet4_subtract = d_subtract
        else:
            print('Wrong mask value try again')
            continue
        break
    #проверяем, входит ли подсеть subtract в source подсети
    if (a_subtract <= broadcastOctet1 and b_subtract <= broadcastOctet2 and c_subtract <= broadcastOctet3 and d_subtract <= broadcastOctet4 and a_subtract >= subnetOctet1 and b_subtract >= subnetOctet2 and c_subtract >= subnetOctet3 and d_subtract >= subnetOctet4):
        if (mask > mask_subtract):
            print ('Error: second subnet is bigger than first')
            continue
        if (mask == mask_subtract):
            print('Nothing to subtract, the second subnet is equal to the first')
            continue
        else:
            print(subnetOctet1, subnetOctet2, subnetOctet3, subnetOctet4, sep='.', end='')
            print('/', mask, sep='')
            print('-')
            print(subnetOctet1_subtract, subnetOctet2_subtract, subnetOctet3_subtract, subnetOctet4_subtract, sep='.', end='')
            print('/', mask_subtract, sep='')
            print('=')
            KarmanLeft = 1
            NewOctet4Left = subnetOctet4
            while NewOctet4Left < subnetOctet4_subtract:
                masknew = 33
                while NewOctet4Left + KarmanLeft <= subnetOctet4_subtract:
                    masknew = masknew - 1
                    KarmanLeft = KarmanLeft * 2
                if KarmanLeft != 1:
                    KarmanLeft = KarmanLeft / 2
                if NewOctet4Left == subnetOctet4_subtract:
                    masknew = 32
                    break
                print(subnetOctet1, subnetOctet2, subnetOctet3, int(NewOctet4Left), sep='.', end='')
                print(' /', masknew, sep='')
                NewOctet4Left = NewOctet4Left + KarmanLeft
                KarmanLeft = 1
            KarmanRight = 1
            NewOctet4Right = broadcastOctet4
            NewOctet4RightSet = []
            NewMaskRightSet = []
            while NewOctet4Right > broadcastOctet4_subtract:
                masknew = 33
                while NewOctet4Right - KarmanRight >= broadcastOctet4_subtract:
                    masknew = masknew - 1
                    KarmanRight = KarmanRight * 2
                if KarmanRight != 1:
                    KarmanRight = KarmanRight / 2
                NewOctet4Right = NewOctet4Right - KarmanRight
                NewOctet4RightSet.append(NewOctet4Right)
                NewMaskRightSet.append(masknew)
                KarmanRight = 1
            NewOctet4RightSet.reverse()
            NewMaskRightSet.reverse()
            for i in range (len(NewOctet4RightSet)):
                print(subnetOctet1, subnetOctet2, subnetOctet3, int(NewOctet4RightSet[i]) + 1, sep='.', end='')
                print(' /', NewMaskRightSet[i], sep='')
    else:
        print ('Subnet 2 is not part of the subnet 1')
    while True:
        print('Wish to continue? (y/n)')
        answer = str(input())
        if answer == 'y' or answer == 'Y':
            break
        elif answer == 'n' or answer == 'N':
            sys.exit()
        else:
            continue
