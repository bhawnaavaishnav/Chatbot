# only one person details

print("Welcome")
print("Do you want to know Bhawna's details?")
answer=input("Enter your answer in yes or no: ")
if answer=="yes":
	print("Nice")
	name=input("Enter the name: ")
	if name=="Bhawna":
		print("Details of",name)
		favourite_movie=input(name+"'s favourite movie do you want to know? ")
		if favourite_movie=="yes":
			print("Ghajini is bhawna's favourite movie")
			favourite_colour=input(name+"'s favourite colour do you want to know? ")
			if favourite_colour=="yes":
				print("Bhawna's favourite colour is black")
				hobbise=input(name+"'s hobbise do you want to no? ")
				if hobbise=="yes":
					print("Writing , Photography and Dancing")
					colour=input(name+"'s colour you want to know about? ")
					if colour=="yes":
						print("Bhawna's colour is fair")
						weight=input(name+"'s weight you want to know? ")
						if weight=="yes":
							print("Bhawna's weight is 44 kg")
						elif weight=="no":
							print("Ok")
						else:
							print("Don't understand")
					elif colour=="no":
						print("Ok")
					else:
						print("Don't understand")
				elif hobbise=="no":
					print("Ok")
				else:
					print("Don't understand")
			elif favourite_colour=="no":
				print("Ok")
			else:
				print("Don't understand")
		elif favourite_movie=="no":
			print("Ok")
		else:
			print("Don't understand")
	else:
		print("not found this name")
elif answer=="no":
    print("Ok")
else:
	print("Don't Understand")

# one more person details

print("Welcome")
print("Do you want to know about bhawna and shital")
x=input("Enter your answer in yes or no: ")
if x=="yes":
    print("Nice")
    name=input("Enter name (Bhawna/Shital): ")
    if name=="Bhawna" or name=="Shital":
        print("Deatils of",name)
        favourite_movie=input(name+"'s favourite movie do you want to know? ")
        if favourite_movie=="yes":
            if name=="bhawna":
                print("Ghajini is bhawna's favourite movie")
            elif name=="shital":
                print("Shersha is shital's favourite movie")
            favourite_colour=input(name+"'s favourite colour do you want to know? ")
            if favourite_colour=="yes":
                if name=="bhawna":
                    print("Bhawna's favourite colour is black")
                elif name=="shital":
                    print("Shital's favourite colour is black and blue")
                hobbise=input(name+"'s hobbise do you want to no? ")
                if hobbise=="yes":
                    if name=="bhawna":
                        print("Writing , Photography and Dancing")
                    elif name=="shital":
                        print("Travelling and Trekking")
                    weight=input(name+"'s weight you want to know? ")
                    if weight=="yes":
                        if name=="bhawna":
                            print("Bhawna's weight is 44 kg")
                        elif name=="shital":
                            print("Shital's weight is 43kg")
                    elif weight=="no":
                        print("Ok")
                    else:
                        print("Don't understand")
                elif hobbise=="no":
                    print("Ok")
                else:
                    print("Don't understand")
            elif favourite_movie=="no":
                print("Ok")
            else:
                print("Don't understand")
        elif favourite_movie=="no":
            print("Ok")
        else:
            print("Don't understand")
    else:
        print("Don't understand")
elif x=="no":
    print("Ok")
else:
    print("Don't understand")
