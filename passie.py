import os, random, time

x = False
while x == False:
    print ("-- Passie --")
    print ("\n")
    print ("1) Create")
    print ("2) About")
    print ("\n")
    selection = input ("Select an option by typing 1 or 2: ")
    selection
    if selection == "1":
        x = True
    elif selection == "2":
        x = True
# This is more or less a menu. Kinda bad, but it works.

if selection == "1":
    x = False
    while x == False:
        print ("-- Passie --")
        print ("\n")
        print ("To create your new password, we will use the two step method. To do this we will use a KEY.\nA key can be anything memorable but it is recommended you use a combination of special characters,\nletters and numbers.")
        print ("\n")
        print ("EG: I<3PA. - meaning I love, symbolised by the text heart, Peter Andre.")
        print ("\n")
        key = input ("Please input your desired key: ")
        key
        if len(key) >= 4:
            x = True
        else:
            os.system ("cls")
            print ("-- Passie --")
            print ("\n")
            print ("Invalid key: key is too short")
            time.sleep (1)
    # This is more or less asking for the key.

    x = False
    while x == False:
        print ("-- Passie --")
        print ("\n")
        print ("It's time to input the name of the service you intend to create a password for!")
        print ("\n")
        service = input ("Please input the service: ")
        service
        og_service = service
        y = 0
        service = list(service)
        chars = len(service)
        while y != chars:
            service[y] = service[y].replace(".","/")
            service[y] = service[y].replace(",",".")
            service[y] = service[y].replace("m",",")
            service[y] = service[y].replace("n","m")
            service[y] = service[y].replace("b","n")
            service[y] = service[y].replace("v","b")
            service[y] = service[y].replace("c","v")
            service[y] = service[y].replace("x","c")
            service[y] = service[y].replace("z","x")
            service[y] = service[y].replace("'","#")
            service[y] = service[y].replace(";","'")
            service[y] = service[y].replace("l",";")
            service[y] = service[y].replace("k","l")
            service[y] = service[y].replace("j","k")
            service[y] = service[y].replace("h","j")
            service[y] = service[y].replace("g","h")
            service[y] = service[y].replace("f","g")
            service[y] = service[y].replace("d","f")
            service[y] = service[y].replace("s","d")
            service[y] = service[y].replace("a","s")
            service[y] = service[y].replace("[","]")
            service[y] = service[y].replace("p","[")
            service[y] = service[y].replace("o","p")
            service[y] = service[y].replace("i","o")
            service[y] = service[y].replace("u","i")
            service[y] = service[y].replace("y","u")
            service[y] = service[y].replace("t","y")
            service[y] = service[y].replace("r","t")
            service[y] = service[y].replace("e","r")
            service[y] = service[y].replace("w","e")
            service[y] = service[y].replace("q","w") 
            y = y + 1
        join_by = ""
        service = join_by.join(service)
        x = True
    # Jesus this took a while to figure out.. This shifts the characters and joins them back together.

    x = False
    while x == False:
        print ("-- Passie --")
        print ("\n") 
        print ("According to the algorithm, your generated password is as follows;\n")
        print ("Key: {}".format(key))
        print ("Service : {}".format(og_service))
        print ("Shifted : {}\n".format(service))
        print ("Complete password: {}".format(key + service))
        file = open(og_service + ".txt","w") 
        file.write ("Key: {}\n".format(key))
        file.write ("Service : {}\n".format(og_service))
        file.write ("Shifted : {}\n\n".format(service))
        file.write ("Complete password: {}".format(key + service))
        file.close() 
        input()
        x = True
    # Displays the new password using the key and the service name shifted.

elif selection == "2":
    x = False
    while x == False:
        print ("-- Passie --")
        print ("\n")
        print ("Passie is a password generator based upon the 'Fletch' method.")
        print ("A while ago a friend told me how he keeps passwords, using a key that's memoriable\nto start then shifting the service he's logging into one key to the right, making it easy to remember and enter.")
        print ("\nEG: !ligbw>hpph;r")
        print ("EX: KEY=(! = random char, Linux is good but Windows is greater), SERVICE=(Google == hpph;r)")
        print ("\n")
        print ("Passie by Da532, inspired by Regan and Haden.")
        input()
        x = True
