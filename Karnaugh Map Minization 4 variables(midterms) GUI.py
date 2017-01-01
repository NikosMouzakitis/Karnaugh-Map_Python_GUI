from tkinter import *

root = None
global mlist
tvar = StringVar
tvar = ""
lh = 2
lw = 2
m1 = None
m2 = None
m3 = None
m4 = None
m5 = None
m6 = None
m7 = None
m8 = None
m9 = None
m10 = None
m11 = None
m12= None
m13 = None
m14 = None
m15 = None
m16 = None
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0
cnt6 = 0
cnt7 = 0
cnt8 = 0
cnt9 = 0
cnt10 = 0
cnt11 = 0
cnt12 = 0
cnt13 = 0
cnt14 = 0
cnt15 = 0
cnt16= 0
#label_color = "thistle"
label_color  = "white smoke"
def buttonPushed1():

    global m1
    global cnt1

    cnt1 +=1

    if(cnt1 % 2 ):

        m1.set("0")
    if(cnt1 %2 == 0):

        m1.set("1")

def addTextLabel1(root):

    global m1

    m1 = StringVar()
    m1.set("1")
    label1 = Label(root,textvariable = m1,width = lw,height = lh,background = label_color)
    label1.grid(column = 0 ,row = 0)


def buttonPushed2():
    global m2
    global cnt2

    cnt2 += 1

    if (cnt2 % 2):
        m2.set("0")
    if (cnt2 % 2 == 0):
        m2.set("1")


def addTextLabel2(root):
    global m2

    m2 = StringVar()
    m2.set("1")
    label2 = Label(root, textvariable=m2,width = lw,height = lh,background = label_color)
    label2.grid(column = 1 ,row = 0)

def buttonPushed3():

    global m3
    global cnt3

    cnt3 +=1

    if(cnt3 % 2 ):

        m3.set("0")
    if(cnt3 %2 == 0):

        m3.set("1")

def addTextLabel3(root):

    global m3

    m3 = StringVar()
    m3.set("1")
    label3 = Label(root,textvariable = m3,width = lw,height = lh,background = label_color)
    label3.grid(column = 3 ,row = 0)

def buttonPushed4():

    global m4
    global cnt4

    cnt4 +=1

    if(cnt4 % 2 ):

        m4.set("0")
    if(cnt4 %2 == 0):

        m4.set("1")

def addTextLabel4(root):

    global m4

    m4 = StringVar()
    m4.set("1")
    label4 = Label(root,textvariable = m4,width = lw,height = lh,background = label_color)
    label4.grid(column = 2 ,row = 0)

def buttonPushed5():

    global m5
    global cnt5

    cnt5 +=1

    if(cnt5 % 2 ):

        m5.set("0")
    if(cnt5 %2 == 0):

        m5.set("1")

def addTextLabel5(root):

    global m5

    m5 = StringVar()
    m5.set("1")
    label5 = Label(root,textvariable = m5,width = lw,height = lh,background = label_color)
    label5.grid(column = 0 ,row = 1)


def buttonPushed6():
    global m6
    global cnt6

    cnt6 += 1

    if (cnt6 % 2):
        m6.set("0")
    if (cnt6 % 2 == 0):
        m6.set("1")

def addTextLabel6(root):
    global m6

    m6 = StringVar()
    m6.set("1")
    label6 = Label(root, textvariable=m6,width = lw,height = lh,background = label_color)
    label6.grid(column = 1 ,row = 1)

def buttonPushed7():

    global m7
    global cnt7

    cnt7 +=1

    if(cnt7 % 2 ):

        m7.set("0")
    if(cnt7 %2 == 0):

        m7.set("1")

def addTextLabel7(root):

    global m7

    m7 = StringVar()
    m7.set("1")
    label7 = Label(root,textvariable = m7,width = lw,height = lh,background = label_color)
    label7.grid(column = 3 ,row = 1)

def buttonPushed8():

    global m8
    global cnt8

    cnt8 +=1

    if(cnt8 % 2 ):

        m8.set("0")
    if(cnt8 %2 == 0):

        m8.set("1")

def addTextLabel8(root):

    global m8

    m8 = StringVar()
    m8.set("1")
    label8 = Label(root,textvariable = m8,width = lw,height = lh,background = label_color)
    label8.grid(column = 2 ,row = 1)

def buttonPushed9():

    global m9
    global cnt9

    cnt9 +=1

    if(cnt9 % 2 ):

        m9.set("0")
    if(cnt9 %2 == 0):

        m9.set("1")

def addTextLabel9(root):

    global m9

    m9 = StringVar()
    m9.set("1")
    label9 = Label(root,textvariable = m9,width = lw,height = lh,background = label_color)
    label9.grid(column = 0 ,row = 3)


def buttonPushed10():
    global m10
    global cnt10

    cnt10 += 1

    if (cnt10 % 2):
        m10.set("0")
    if (cnt10 % 2 == 0):
        m10.set("1")


def addTextLabel10(root):
    global m10

    m10 = StringVar()
    m10.set("1")
    label10 = Label(root, textvariable=m10,width = lw,height = lh,background = label_color)
    label10.grid(column = 1 ,row = 3)

def buttonPushed11():

    global m11
    global cnt11

    cnt11 +=1

    if(cnt11 % 2 ):

        m11.set("0")
    if(cnt11 %2 == 0):

        m11.set("1")

def addTextLabel11(root):

    global m11

    m11 = StringVar()
    m11.set("1")
    label11 = Label(root,textvariable = m11,width = lw,height = lh,background = label_color)
    label11.grid(column = 3 ,row = 3)

def buttonPushed12():

    global m12
    global cnt12

    cnt12 +=1

    if(cnt12 % 2 ):

        m12.set("0")
    if(cnt12 %2 == 0):

        m12.set("1")

def addTextLabel12(root):

    global m12

    m12 = StringVar()
    m12.set("1")
    label12 = Label(root,textvariable = m12,width = lw,height = lh,background = label_color)
    label12.grid(column = 2 ,row = 3)

def buttonPushed13():

    global m13
    global cnt13

    cnt13 +=1

    if(cnt13 % 2 ):

        m13.set("0")
    if(cnt13 %2 == 0):

        m13.set("1")

def addTextLabel13(root):

    global m13

    m13 = StringVar()
    m13.set("1")
    label13 = Label(root,textvariable = m13,width = lw,height = lh,background = label_color)
    label13.grid(column = 0 ,row = 2)


def buttonPushed14():
    global m14
    global cnt14

    cnt14 += 1

    if (cnt14 % 2):
        m14.set("0")
    if (cnt14 % 2 == 0):
        m14.set("1")


def addTextLabel14(root):
    global m14

    m14 = StringVar()
    m14.set("1")
    label14 = Label(root, textvariable=m14,width = lw,height = lh,background = label_color)
    label14.grid(column = 1 ,row = 2)

def buttonPushed15():

    global m15
    global cnt15

    cnt15 +=1

    if(cnt15 % 2 ):

        m15.set("0")
    if(cnt15 %2 == 0):

        m15.set("1")

def addTextLabel15(root):

    global m15

    m15 = StringVar()
    m15.set("1")
    label15 = Label(root,textvariable = m15,width = lw,height = lh,background = label_color)
    label15.grid(column = 3 ,row = 2)

def buttonPushed16():

    global m16
    global cnt16

    cnt16 +=1

    if(cnt16 % 2 ):

        m16.set("0")
    if(cnt16 %2 == 0):

        m16.set("1")

def addTextLabel16(root):

    global m16

    m16 = StringVar()
    m16.set("1")
    label16 = Label(root,textvariable = m16,width = lw,height = lh,background = label_color)
    label16.grid(column = 2 ,row = 2)

def minimization(k):
    global la

    mini = []
    combo = []

    multicombo2 = [] #used to solve the bug of overlaping combinations,to make possible to have best minimization.
    multicombo4 = []

    zero_cnt = 0
    prod = 1
    appended = 0  # used to count the times we ve applied a combination of squares in the map.
    print_k(k)    #printing on screen the Karnaugh Map,we are solving.

    for i in range(0, 16):

        prod *= k[i]

        if (k[i] == 0):

            zero_cnt += 1

    if (prod == 1):

        print("F(w,x,y,z) = 1\n")
        la.set("F = 1")
        return

    if (zero_cnt == 16):

        print("F(w,x,y,z) = 0\n")
        la.set("F = 0")
        return

    for i in range(0, 16):

        combo_value = 0  # works as flag to know the most squares for every midterm we can combine.
        combo_flag = 0

        if (k[i] == 0):

            combo.append(0)
            combo_flag = 1

        else:

            for j in range(0, 4):

                if (combo_value > 8):

                    break

                if (k[i] and k[driver_8[i][j][0] + i] and k[driver_8[i][j][1] + i] and k[driver_8[i][j][2] + i] and k[
                        driver_8[i][j][3] + i] and k[driver_8[i][j][4] + i] and k[driver_8[i][j][5] + i] and k[
                        driver_8[i][j][6] + i]):

                    combo_value = 8
                    combo.append(8)
                    combo_flag = 1
                    break

            for j in range(0, 6):

                if (combo_value > 4):

                    break

                if ((k[i] and k[driver_4[i][j][0] + i] and k[driver_4[i][j][1] + i] and k[driver_4[i][j][2] + i])):

                    combo_value = 4
                    combo.append(4)
                    combo_flag = 1
                    break

            for j in range(0, 4):

                if ((k[i] and k[i + driver_2[i][j]])):

                    if (combo_value > 2):

                        break

                    else:

                        combo.append(2)
                        combo_flag = 1

                        break

            if (combo_flag == 0):

                combo.append(1)

#creating multicombo2 and multicombo4 containing the amount of different combinations of 2 and 4 that  midterm can have.


    for i in range(0, 16):
        multicombo2_cnt = 0
        multicombo4_cnt = 0

        combo_value = 0  # works as flag to know the most squares for every midterm we can combine.
        combo_flag = 0

        if (k[i] == 0):

            combo_flag = 1
            multicombo2.append(0)
            multicombo4.append(0)
        else:

            for j in range(0, 4):

                if (combo_value > 8):
                    break

                if (k[i] and k[driver_8[i][j][0] + i] and k[driver_8[i][j][1] + i] and k[
                                driver_8[i][j][2] + i] and k[
                                driver_8[i][j][3] + i] and k[driver_8[i][j][4] + i] and k[driver_8[i][j][5] + i] and k[
                                driver_8[i][j][6] + i]):
                    combo_value = 8
                    #combo.append(8)
                    combo_flag = 1


            for j in range(0, 6):

                if (combo_value > 4):
                    break

                if (
                        (k[i] and k[driver_4[i][j][0] + i] and k[driver_4[i][j][1] + i] and k[driver_4[i][j][2] + i])):
                    combo_value = 4
                    multicombo4_cnt += 1
                    combo_flag = 1


            for j in range(0, 4):

                if ((k[i] and k[i + driver_2[i][j]])):

                    if (combo_value > 2):

                        break

                    else:
                        multicombo2_cnt +=1
                        combo_flag = 1



            multicombo2.append(multicombo2_cnt)
            multicombo4.append(multicombo4_cnt)




                # _calculating  free aces in the map and  position with highest combinable value
                #_free_aces aren't actually the free aces thought the program,just on the beggining.!!
    print(multicombo4)
    already_combined = []
    already_combined = combo
    free_aces = 0
    for element in k:

        if (element == 1):

            free_aces += 1

    k_max = combo[0]
    max_thesis = 0

    for i in range(0, 16):

        if (combo[i] > k_max):

            k_max = combo[i]
            max_thesis = i

    if (k_max == 1):

        print("The is no minimization on this function.")
        la.set("Not possible minimization")
        return
    #                                                        minimization code goes after here.
    map_copy = k
    solution = ""
    timer = 0

    for t in range(0,16):       #preminimization combining the midterms with lower value in multicombo2 first
        if (multicombo2[t] == 1):               #since they cannot combine somehow different.

            for j in range(0, 4):

                if ((k[t] and k[t + driver_2[t][j]]) and ((already_combined[t] != 0)  ) ):

                    duo = []
                    duo.append(t)
                    duo.append(t + driver_2[t][j])
                    duo.sort()
                    print("Combining the following squares: ", duo)
                    solution += solver(duo)
                    zero[t] = 1
                    zero[t + driver_2[t][j]] = 1
                    already_combined[duo[0]] = 0
                    already_combined[duo[1]] = 0
                    free_aces -= 2
                    break

    for t in range(0,16):
        if (multicombo2[t] == 2):

            for j in range(0, 4):


                if ((k[t] and k[t + driver_2[t][j]]) and ((already_combined[t] != 0) and (already_combined[t+driver_2[t][j]] != 0 ) ) ):

                    duo = []
                    duo.append(t)
                    duo.append(t + driver_2[t][j])
                    duo.sort()
                    print("Combining the following squares: ", duo)
                    solution += solver(duo)
                    zero[t] = 1
                    zero[t + driver_2[t][j]] = 1
                    already_combined[duo[0]] = 0
                    already_combined[duo[1]] = 0
                    free_aces -= 2
                    break


    for t in range(0,16):

        if(multicombo4[t] == 1):
            for j in range(0, 6):

                if ((k[t] and k[driver_4[t][j][0] + t] and k[driver_4[t][j][1] + t] and k[driver_4[t][j][2] + t] and (already_combined[t] != 0)  )):

                    quatro = []
                    mini.append(
                        [t, driver_4[t][j][0] + t, driver_4[t][j][1] + t,
                         driver_4[t][j][2] + t])
                    appended += 1
                    quatro.append(t)
                    quatro.append(driver_4[t][j][0] + t)
                    quatro.append(driver_4[t][j][1] + t)
                    quatro.append(driver_4[t][j][2] + t)
                    print("Combining the following squares : ", quatro)
                    print("already combined: ",already_combined)
                    quatro.sort()
                    solution += solver(quatro)
                    zero[t] = 1
                    zero[driver_4[t][j][0] + t] = 1
                    zero[driver_4[t][j][1] + t] = 1
                    zero[driver_4[t][j][2] + t] = 1
                    already_combined[quatro[0]] = 0
                    already_combined[quatro[1]] = 0
                    already_combined[quatro[2]] = 0
                    already_combined[quatro[3]] = 0
                    free_aces -= 4
                    break

    for xl in range(2,6):

        for t in range(0, 16):

            if (multicombo4[t] == xl):

                for j in range(0, 6):
                
                    if ((k[t] and k[driver_4[t][j][0] + t] and k[driver_4[t][j][1] + t] and  k[driver_4[t][j][2] + t] and ( (already_combined[t] != 0) ^ (already_combined[driver_4[t][j][0] + t] != 0) ^ (already_combined[driver_4[t][j][1] + t] != 0) ^ (already_combined[driver_4[t][j][2] + t] != 0)  ))):

                        quatro = []
                        mini.append(
                        [t, driver_4[t][j][0] + t, driver_4[t][j][1] + t,
                         driver_4[t][j][2] + t])
                        appended += 1
                        quatro.append(t)
                        quatro.append(driver_4[t][j][0] + t)
                        quatro.append(driver_4[t][j][1] + t)
                        quatro.append(driver_4[t][j][2] + t)
                        print("Combining the following squares : ", quatro)
                        quatro.sort()
                        solution += solver(quatro)
                        zero[t] = 1
                        zero[driver_4[t][j][0] + t] = 1
                        zero[driver_4[t][j][1] + t] = 1
                        zero[driver_4[t][j][2] + t] = 1
                        already_combined[quatro[0]] = 0
                        already_combined[quatro[1]] = 0
                        already_combined[quatro[2]] = 0
                        already_combined[quatro[3]] = 0
                        free_aces -= 4
                        print("already combined: ",already_combined)
                        break





    while (max(already_combined) >= 1):

        print("\nMINIMIZATION RUNS\n")
        print(combo)
        for i in range(0, 16):
             if (   (combo[i] == 2 )   and (timer > 2)   ):

                for j in range(0, 4):

                    if ((k[i] and k[i + driver_2[i][j]]) and (already_combined[i] != 0) and zero[i + driver_2[i][j]] == 0 ):

                        duo = []
                        duo.append(i)
                        duo.append(i + driver_2[i][j])
                        duo.sort()
                        print("Combining the following squares: ", duo)
                        solution += solver(duo)
                        zero[i] = 1
                        zero[i + driver_2[i][j]] = 1
                        already_combined[duo[0]] = 0
                        already_combined[duo[1]] = 0
                        free_aces -= 2

             elif (combo[i] == 1):

                solution += solver([i])
                already_combined[i] = 0

        if (k_max == 8):  # minimization for eight squares combination.

            for j in range(0, 4):

                if (map_copy[max_thesis] and map_copy[driver_8[max_thesis][j][0] + max_thesis] and map_copy[
                        driver_8[max_thesis][j][1] + max_thesis] and map_copy[
                        driver_8[max_thesis][j][2] + max_thesis] and map_copy[
                        driver_8[max_thesis][j][3] + max_thesis] and map_copy[
                        driver_8[max_thesis][j][4] + max_thesis] and map_copy[
                        driver_8[max_thesis][j][5] + max_thesis] and map_copy[driver_8[max_thesis][j][6] + max_thesis]):

                    octo = []
                    octo.append(max_thesis)
                    octo.append(driver_8[max_thesis][j][0] + max_thesis)
                    octo.append(driver_8[max_thesis][j][1] + max_thesis)
                    octo.append(driver_8[max_thesis][j][2] + max_thesis)
                    octo.append(driver_8[max_thesis][j][3] + max_thesis)
                    octo.append(driver_8[max_thesis][j][4] + max_thesis)
                    octo.append(driver_8[max_thesis][j][5] + max_thesis)
                    octo.append(driver_8[max_thesis][j][6] + max_thesis)
                    octo.sort()
                    print("Combining the following squares  :", octo)
                    solution += solver(octo)
                    zero[max_thesis] = 1
                    zero[driver_8[max_thesis][j][0] + max_thesis] = 1
                    zero[driver_8[max_thesis][j][1] + max_thesis] = 1
                    zero[driver_8[max_thesis][j][2] + max_thesis] = 1
                    zero[driver_8[max_thesis][j][3] + max_thesis] = 1
                    zero[driver_8[max_thesis][j][4] + max_thesis] = 1
                    zero[driver_8[max_thesis][j][5] + max_thesis] = 1
                    zero[driver_8[max_thesis][j][6] + max_thesis] = 1
                    already_combined[octo[0]] = 0
                    already_combined[octo[1]] = 0
                    already_combined[octo[2]] = 0
                    already_combined[octo[3]] = 0
                    already_combined[octo[4]] = 0
                    already_combined[octo[5]] = 0
                    already_combined[octo[6]] = 0
                    already_combined[octo[7]] = 0
                    free_aces -= 8
                    break

        elif (k_max == 2):  # minimization for two squares combination.




            for j in range(0, 4):


                if ((map_copy[max_thesis] and map_copy[max_thesis + driver_2[max_thesis][j]]) and ((already_combined[max_thesis] != 0)  ) ):


                    duo = []
                    duo.append(max_thesis)
                    duo.append(max_thesis + driver_2[max_thesis][j])
                    duo.sort()
                    print("Combining the following squares: ", duo)
                    solution += solver(duo)
                    zero[max_thesis] = 1
                    zero[max_thesis + driver_2[max_thesis][j]] = 1
                    already_combined[duo[0]] = 0
                    already_combined[duo[1]] = 0
                    free_aces -= 2
                    break

        elif (k_max == 4):  # minimization for four squares combination.

            for j in range(0, 6):

                if ((map_copy[max_thesis] and map_copy[driver_4[max_thesis][j][0] + max_thesis] and map_copy[
                        driver_4[max_thesis][j][1] + max_thesis] and map_copy[
                        driver_4[max_thesis][j][2] + max_thesis])):

                    quatro = []
                    mini.append(
                        [max_thesis, driver_4[max_thesis][j][0] + max_thesis, driver_4[max_thesis][j][1] + max_thesis,
                         driver_4[max_thesis][j][2] + max_thesis])
                    appended += 1
                    quatro.append(max_thesis)
                    quatro.append(driver_4[max_thesis][j][0] + max_thesis)
                    quatro.append(driver_4[max_thesis][j][1] + max_thesis)
                    quatro.append(driver_4[max_thesis][j][2] + max_thesis)
                    print("Combining the following squares : ", quatro)
                    quatro.sort()
                    solution += solver(quatro)
                    zero[max_thesis] = 1
                    zero[driver_4[max_thesis][j][0] + max_thesis] = 1
                    zero[driver_4[max_thesis][j][1] + max_thesis] = 1
                    zero[driver_4[max_thesis][j][2] + max_thesis] = 1
                    already_combined[quatro[0]] = 0
                    already_combined[quatro[1]] = 0
                    already_combined[quatro[2]] = 0
                    already_combined[quatro[3]] = 0
                    free_aces -= 4
                    break


        if (max(already_combined) < 2):

            break

        timer += 1
        max_thesis = 0      # calculation of the new k_max and max_thesis
        k_max = already_combined[0]
        found_flag = 0

        for i in range(0, 16):

            if (zero[i] == 0):

                if (k_max < already_combined[i]):

                    k_max = already_combined[i]
                    max_thesis = i
                    found_flag = 1

            else:

                pass

        if (found_flag != 1):

            for i in range(0, 16):

                if (k_max < already_combined[i]):

                    k_max = already_combined[i]
                    max_thesis = i

                else:

                    pass

    print("\nMinimization Results:\n\nF(A,B,C,D)=", solution[:-2])
    la.set(solution[:-2])

def solver(arg):

    sol = ""

    if (len(arg) == 1):

        if(arg == [0]):
            sol += " A'B'C'D' "
        elif (arg == [1]):
            sol += " A'B'C'D "
        elif (arg == [2]):
            sol += " A'B'CD' "
        elif (arg == [3]):
            sol += " A'B'CD "
        elif (arg == [4]):
            sol += " A'BC'D' "
        elif (arg == [5]):
            sol += " A'BC'D "
        elif (arg == [6]):
            sol += " A'BCD' "
        elif (arg == [7]):
            sol += " A'BCD "
        elif (arg == [8]):
            sol += " AB'C'D' "
        elif (arg == [9]):
            sol += " AB'C'D "
        elif (arg == [10]):
            sol += " AB'CD' "
        elif (arg == [11]):
            sol += " AB'CD "
        elif (arg == [12]):
            sol += " ABC'D' "
        elif (arg == [13]):
            sol += " ABC'D "
        elif (arg == [14]):
            sol += " ABCD' "
        elif (arg == [15]):
            sol += " ABCD "

    if (len(arg) == 2 ):

        if(arg == [0,1]):
            sol += " A'B'C' "
        elif(arg == [0,2]):
            sol += " A'B'D' "
        elif arg == [0, 4]:
            sol += " A'C'D' "
        elif(arg == [0,8]):
            sol += " B'C'D' "
        elif(arg == [1,3]):
            sol += " A'B'D "
        elif(arg == [1,5]):
            sol += " A'C'D "
        elif(arg == [1,9]):
            sol += " B'C'D "
        elif(arg == [2,3]):
            sol += " A'B'C "
        elif(arg == [3,7]):
            sol += " A'CD "
        elif(arg == [3,11]):
            sol += " B'CD "
        elif(arg == [2,6]):
            sol += " A'CD' "
        elif(arg == [2,10]):
            sol += " B'CD' "
        elif(arg == [4,5]):
            sol += " A'BC' "
        elif (arg == [4, 12]):
            sol += " BC'D' "
        elif(arg == [4,6]):
            sol += " A'BD' "
        elif(arg == [5,7]):
            sol += " A'BD "
        elif(arg == [5,13]):
            sol += " BC'D "
        elif(arg == [6,7]):
            sol += " A'BC "
        elif(arg == [7,15]):
            sol += " BCD "
        elif(arg == [6,14]):
            sol += " BCD' "
        elif(arg == [12,13]):
            sol += " ABC' "
        elif(arg == [8,12]):
            sol += " AC'D' "
        elif(arg == [12,14]):
            sol += " ABD' "
        elif(arg == [9,13]):
            sol += " AC'D "
        elif(arg == [13,15]):
            sol += " ABD "
        elif(arg == [11,15]):
            sol += " ACD "
        elif(arg == [14,15]):
            sol += " ABC "
        elif(arg == [10,14]):
            sol += " ACD' "
        elif (arg == [8, 9]):
            sol += " AB'C' "
        elif (arg == [8,10]):
            sol += " AB'D' "
        elif (arg == [9,11]):
            sol += " AB'D "
        elif (arg == [10, 11]):
            sol += " AB'C "

    if( len (arg) == 4):
        if( arg == [0,1,2,3]):
            sol += " A'B' "
        elif( arg == [0,1,4,5]):
            sol += " A'C' "
        elif( arg == [0,4,8,12]):
            sol += " C'D' "
        elif( arg == [0,1,8,9]):
            sol += " B'C'"
        elif( arg == [0,2,8,10]):
            sol += " B'D' "
        elif(arg == [0,2,4,6]):
            sol += " A'D' "
        elif( arg == [1,5,9,13]):
            sol += " C'D "
        elif( arg == [1,3,5,7]):
            sol += " A'D "
        elif(arg == [1,3,9,11]):
            sol += " B'D "
        elif(arg == [2,3,6,7]):
            sol += " A'C "
        elif(arg == [2,3,10,11]):
            sol += " B'C "
        elif(arg == [3,7,11,15]):
            sol += " CD "
        elif(arg == [2,6,10,14]):
            sol += " CD' "
        elif(arg == [4,5,6,7]):
            sol += " A'B "
        elif(arg == [4,5,12,13]):
            sol += " BC' "
        elif(arg == [4,6,12,14]):
            sol += " BD' "
        elif(arg == [5,7,13,15]):
            sol += " BD "
        elif(arg == [6,7,14,15]):
            sol += " BC "
        elif(arg == [12,13,14,15]):
            sol += " AB "
        elif(arg == [8,9,12,13]):
            sol += " AC' "
        elif(arg == [8,10,12,14]):
            sol += " AD' "
        elif(arg == [9,11,13,15]):
            sol += " AD "
        elif(arg == [10,11,14,15]):
            sol += " AC "
        elif(arg == [8,9,10,11]):
            sol += " AB' "

    if (len(arg) == 8):
        if(arg == [0,1,2,3,4,5,6,7]):
            sol += " A' "
        elif(arg == [0,1,2,3,8,9,10,11]):
            sol += " B' "
        elif(arg == [0,2,4,6,8,10,12,14]):
            sol += " D' "
        elif(arg == [0,1,4,5,8,9,12,13]):
            sol += " C' "
        elif(arg == [1,3,5,7,9,11,13,15]):
            sol += " D "
        elif(arg == [4,5,6,7,12,13,14,15]):
            sol += " B "
        elif(arg == [2,3,6,7,10,11,14,15]):
            sol += " C "
        elif(arg == [8,9,10,11,12,13,14,15]):
            sol += " A "


    return sol + " + "

def print_k(k):

    line1 = [0,1,3,2]
    line2 = [4,5,7,6]
    line3 = [12,13,15,14]
    line4 = [8,9,11,10]
    print("KARNAUGH   MAP   DISPLAY\n")
    print((str)(k[line1[0]]) +"\t"+(str)(k[line1[1]])+"\t"+(str)(k[line1[2]])+"\t"+(str)(k[line1[3]])+"\n")
    print((str)(k[line2[0]]) +"\t"+(str)(k[line2[1]])+"\t"+(str)(k[line2[2]])+"\t"+(str)(k[line2[3]])+"\n")
    print((str)(k[line3[0]]) +"\t"+(str)(k[line3[1]])+"\t"+(str)(k[line3[2]])+"\t"+(str)(k[line3[3]])+"\n")
    print((str)(k[line4[0]]) +"\t"+(str)(k[line4[1]])+"\t"+(str)(k[line4[2]])+"\t"+(str)(k[line4[3]])+"\n")


def getMap():
    global mlist

    mlist = []

    global m1
    global m2
    global m3
    global m4
    global m5
    global m6
    global m7
    global m8
    global m9
    global m10
    global m11
    global m12
    global m13
    global m14
    global m15
    global m16

    mlist.append((int)(m1.get()))
    mlist.append((int)(m2.get()))
    mlist.append((int)(m3.get()))
    mlist.append((int)(m4.get()))
    mlist.append((int)(m5.get()))
    mlist.append((int)(m6.get()))
    mlist.append((int)(m7.get()))
    mlist.append((int)(m8.get()))
    mlist.append((int)(m9.get()))
    mlist.append((int)(m10.get()))
    mlist.append((int)(m11.get()))
    mlist.append((int)(m12.get()))
    mlist.append((int)(m13.get()))
    mlist.append((int)(m14.get()))
    mlist.append((int)(m15.get()))
    mlist.append((int)(m16.get()))
    print(mlist)
    minimization(mlist)


def result(r) :


    sol_text.setvar("1")



global v
zero = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
k_map = []
combo = []

free_aces = 0
solution = ""
driver_2 = []
driver_4 = []
driver_8 = []
# -------------SETTING UP THE LIST driver_2------------------------------------------------------
driver_2.append([1, 2, 4, 8])
driver_2.append([-1, 2, 4, 8])
driver_2.append([1, -2, 4, 8])
driver_2.append([-1, -2, 4, 8])
driver_2.append([-4, 1, 2, 8])
driver_2.append([-1, -4, 2, 8])
driver_2.append([-2, -4, 1, 8])
driver_2.append([-4, -2, -1, 8])
driver_2.append([-8, 1, 2, 4])
driver_2.append([-8, -1, 2, 4])
driver_2.append([-8, -2, 1, 4])
driver_2.append([-8, -2, -1, 4])
driver_2.append([-8, -4, 1, 2])
driver_2.append([-8, -4, -1, 2])
driver_2.append([-8, -4, -2, 1])
driver_2.append([-8, -4, -2, -1])
# -------------SETTING UP THE LIST driver_4------------------------------------------------------
driver_4.append([[1, 2, 3], [4, 8, 12], [1, 4, 5], [2, 4, 6], [2, 8, 10], [1, 8, 9]])
driver_4.append([[-1, 1, 2], [4, 8, 12], [-1, 3, 4], [2, 4, 6], [-1, 7, 8], [2, 8, 10]])
driver_4.append([[-2, -1, 1], [4, 8, 12], [-2, 6, 8], [1, 4, 5], [-2, 2, 4], [1, 8, 9]])
driver_4.append([[-1, -2, -3], [4, 8, 12], [-1, 3, 4], [-2, 2, 4], [-2, 6, 8], [-1, 7, 8]])
driver_4.append([[1, 2, 3], [-4, 4, 8], [1, 8, 9], [-4, -3, 1], [-4, -2, 2], [2, 8, 10]])
driver_4.append([[-1, 1, 2], [-4, 4, 8], [2, 8, 10], [-4, -2, 2], [-5, -4, -1], [-1, 7, 8]])
driver_4.append([[-4, 4, 8], [-2, -1, 1], [-4, -3, 1], [1, 8, 9], [-2, 6, 8], [-6, -4, -2]])
driver_4.append([[-4, 4, 8], [-3, -2, -1], [-2, 6, 8], [-6, -4, -2], [-5, -4, -1], [-1, 7, 8]])
driver_4.append([[-8, -4, 4], [1, 2, 3], [-8, -6, 2], [6, 4, 2], [5, 4, 1], [-8, -7, 1]])
driver_4.append([[-8, -4, 4], [-1, 1, 2], [-1, 3, 4], [-9, -8, -1], [-8, -6, 2], [6, 4, 2]])
driver_4.append([[-2, -1, 1], [-8, -4, 4], [-10, -8, -2], [-2, 2, 4], [1, 4, 5], [-8, -7, 1]])
driver_4.append([[-3, -2, -1], [-4, -8, 4], [-9, -8, -1], [-1, 3, 4], [-2, 2, 4], [-10, -8, -2]])
driver_4.append([[1, 2, 3], [-12, -8, -4], [-4, -3, 1], [-4, -2, 2], [-8, -6, 2], [-8, -7, 1]])
driver_4.append([[-1, 1, 2], [-12, -8, -4], [-8, -6, 2], [-5, -4, -1], [-4, -2, 2], [-9, -8, -1]])
driver_4.append([[1, -1, -2], [-12, -8, -4], [1, -3, -4], [-6, -4, -2], [1, -7, -8], [-10, -8, -2]])
driver_4.append([[-3, -2, -1], [-12, -8, -4], [-5, -4, -1], [-6, -4, -2], [-10, -8, -2], [-9, -8, -1]])
# -------------SETTING UP THE LIST driver_8------------------------------------------------------
driver_8.append([[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 8, 9, 10, 11], [1, 4, 5, 8, 9, 12, 13], [2, 4, 6, 8, 10, 12, 14]])
driver_8.append(
        [[-1, 1, 2, 3, 4, 5, 6], [-1, 1, 2, 7, 8, 9, 10], [-1, 3, 4, 7, 8, 11, 12], [2, 4, 6, 8, 10, 12, 14]])
driver_8.append(
        [[-2, -1, 1, 2, 3, 4, 5], [-2, -1, 1, 6, 7, 8, 9], [1, 4, 5, 8, 9, 12, 13], [-2, 2, 4, 6, 8, 10, 12]])
driver_8.append(
        [[-3, -2, -1, 1, 2, 3, 4], [-3, -2, -1, 5, 6, 7, 8], [-2, 2, 4, 6, 8, 10, 12], [-1, 3, 4, 7, 8, 11, 12]])
driver_8.append(
        [[-4, -3, -2, -1, 1, 2, 3], [1, 2, 3, 8, 9, 10, 11], [-4, -2, 2, 4, 6, 8, 10], [-4, -3, 1, 4, 5, 8, 9]])
driver_8.append(
        [[-5, -4, -3, -2, -1, 1, 2], [-1, 1, 2, 7, 8, 9, 10], [-5, -4, -1, 3, 4, 7, 8], [-4, -2, 2, 4, 6, 8, 10]])
driver_8.append(
        [[-6, -5, -4, -3, -2, -1, 1], [-2, -1, 1, 6, 7, 8, 9], [-4, -3, 1, 4, 5, 8, 9], [-6, -4, -2, 2, 4, 6, 8]])
driver_8.append(
        [[-7, -6, -5, -4, -3, -2, -1], [-3, -2, -1, 5, 6, 7, 8], [-5, -4, -1, 3, 4, 7, 8], [-6, -4, -2, 2, 4, 6, 8]])
driver_8.append(
        [[7, 6, 5, 4, 3, 2, 1], [3, 2, 1, -5, -6, -7, -8], [5, 4, 1, -3, -4, -7, -8], [6, 4, 2, -2, -4, -6, -8]])
driver_8.append(
        [[6, 5, 4, 3, 2, 1, -1], [2, 1, -1, -6, -7, -8, -9], [4, 3, -1, -4, -5, -8, -9], [6, 4, 2, -2, -4, -6, -8]])
driver_8.append(
        [[5, 4, 3, 2, 1, -1, -2], [1, -1, -2, -7, -8, -9, -10], [5, 4, 1, -3, -4, -7, -8], [4, 2, -2, -4, -6, -8, -10]])
driver_8.append([[4, 3, 2, 1, -1, -2, -3], [-1, -2, -3, -8, -9, -10, -11], [4, 2, -2, -4, -6, -8, -10],
                     [4, 3, -1, -4, -5, -8, -9]])
driver_8.append([[3, 2, 1, -1, -2, -3, -4], [3, 2, 1, -5, -6, -7, -8], [2, -2, -4, -6, -8, -10, -12],
                     [1, -3, -4, -7, -8, -11, -12]])
driver_8.append([[2, 1, -1, -2, -3, -4, -5], [2, 1, -1, -6, -7, -8, -9], [-1, -4, -5, -8, -9, -12, -13],
                     [2, -2, -4, -6, -8, -10, -12]])
driver_8.append([[1, -1, -2, -3, -4, -5, -6], [1, -1, -2, -7, -8, -9, -10], [1, -3, -4, -7, -8, -11, -12],
                     [-2, -4, -6, -8, -10, -12, -14]])
driver_8.append([[-1, -2, -3, -4, -5, -6, -7], [-1, -2, -3, -8, -9, -10, -11], [-1, -4, -5, -8, -9, -12, -13],
                     [-2, -4, -6, -8, -10, -12, -14]])

root = Tk()
#MAXW = 780
#MAXH =590
MAXW = 420
MAXH = 250

root.maxsize(MAXW,MAXH)
root.minsize(MAXW,MAXH)

root.title("Karnaugh Map Minimizator")
root.tk_setPalette( "azure")

mapframe = Frame(root)

mapframe.grid(row = 0,column = 1)

setframe = Frame(root)
setframe.grid(row = 0,column = 0)
selectionframe = Frame(root)
selectionframe.grid(row = 0,column = 2)
sol_frame = Frame(root)
sol_frame.grid(row = 1 )
global la
la = StringVar()



la.set("Karnaugh Minimization")



sol_text = Entry(root,bg = "floral white",fg = 'black',textvariable=la)
sol_text.config(width = 47)

root.tk_focusFollowsMouse()
result_label = Label(sol_frame,text = "Result:")
result_label.grid()
sol_text.grid()
solve = Button(selectionframe,bg="lavender",text = "Solve",fg = "black",command = getMap)
solve.grid(row =0 ,column =3)


button_color = "white"
b1 = Button(setframe,bg=button_color,text= "Set  0",command = buttonPushed1)
b1.grid(row= 0,column = 10)
b2 = Button(setframe,bg=button_color, text="Set  1", command=buttonPushed2)
b2.grid(row= 0,column = 11)
b3 = Button(setframe,bg=button_color, text="Set  2", command=buttonPushed3)
b3.grid(row= 0,column = 13)
b4 = Button(setframe,bg=button_color, text="Set  3", command=buttonPushed4)
b4.grid(row= 0,column = 12)
b5 = Button(setframe, bg=button_color,text="Set  4", command=buttonPushed5)
b5.grid(row=1, column=10)
b6 = Button(setframe,bg=button_color, text="Set  5", command=buttonPushed6)
b6.grid(row=1, column=11)
b7 = Button(setframe,bg=button_color, text="Set  6", command=buttonPushed7)
b7.grid(row=1, column=13)
b8 = Button(setframe,bg=button_color, text="Set  7", command=buttonPushed8)
b8.grid(row=1, column=12)
b9 = Button(setframe,bg=button_color, text="Set  8", command=buttonPushed9)
b9.grid(row=3, column=10)
b10 = Button(setframe,bg=button_color, text="Set  9", command=buttonPushed10)
b10.grid(row=3, column=11)
b11 = Button(setframe,bg=button_color, text="Set 10", command=buttonPushed11)
b11.grid(row=3, column=13)
b12 = Button(setframe,bg=button_color, text="Set 11", command=buttonPushed12)
b12.grid(row=3, column=12)
b13 = Button(setframe,bg=button_color, text="Set 12", command=buttonPushed13)
b13.grid(row=2, column=10)
b14 = Button(setframe,bg=button_color, text="Set 13", command=buttonPushed14)
b14.grid(row=2, column=11)
b15 = Button(setframe,bg=button_color, text="Set 14", command=buttonPushed15)
b15.grid(row=2, column=13)
b16 = Button(setframe,bg=button_color, text="Set 15", command=buttonPushed16)
b16.grid(row=2, column=12)



addTextLabel1(mapframe)
addTextLabel2(mapframe)
addTextLabel3(mapframe)
addTextLabel4(mapframe)
addTextLabel5(mapframe)
addTextLabel6(mapframe)
addTextLabel7(mapframe)
addTextLabel8(mapframe)
addTextLabel9(mapframe)
addTextLabel10(mapframe)
addTextLabel11(mapframe)
addTextLabel12(mapframe)
addTextLabel13(mapframe)
addTextLabel14(mapframe)
addTextLabel15(mapframe)
addTextLabel16(mapframe)

root.mainloop()
