print("Hello there! Welcome to GoAsULike!")
name=input("Before we start, please enter your name:")
print("Nice to meet you "+name)
occ=input("Is your occasion formal or informal?")
print("That's nice! "+name)
gender=input("May I know your gender? m-Male and f-Female")
typ=input("How would you like to dress? The eye-catching 'Royal' style, the dazzling 'Vintage', the striking 'Streetwear', the breathtaking 'Bohemian' <Please enter the ones in single quotations>")
if occ=="formal" and typ=="Royal"and gender=="m":
    print("Try Lime green trousers with White shirt! or try Gray trousers with Prussian blue shirt!")
elif  occ=="informal" and typ=="Royal"and gender=="m":
    print("Try Dark Blue jeans with Lilac purple shirt! or try Black trousers with Emerald Green shirt ")
elif occ=="formal" and typ=="Vintage"and gender=="m":
    print("Cream trousers with Maroon shirt is all you will need! or Brown cargos with Whire shirt and a Deep Blue jacket over it")
elif occ=="informal" and typ=="Vintage"and gender=="m":  
    print("Brown pants with Orange shirt! or Lime green shirt with Black pants is perfect!")
elif occ=="formal" and typ=="Streetwear"and gender=="m":  
    print("It is advised not to wear streetwear to a formal occasion!")
elif occ=="informal" and typ=="Streetwear"and gender=="m":
    print("Grey pants with Blue shirts or Light green with deep blue jeans is a perfect option!")
elif occ=="formal" and typ=="Bohemian"and gender=="m":
    print("Brown pants with Pink shirt or Cream shirts with Black pants is awesome")    
elif occ=="informal" and typ=="Bohemian"and gender=="m": 
    print("Dark pink shirt with Dark Green pants or Grey pants with Orange shirt will do perfectly")
elif occ=="informal" and typ=="Bohemian"and gender=="f": 
    print("Ochre and greyish-blue is a great colour choice!")
elif occ=="formal" and typ=="Bohemian"and gender=="f":
    print("Peach and burn seinna is a great choice for formal occasions!") 
elif occ=="informal" and typ=="Streetwear"and gender=="f":
    print("Pink shirts with brown overcoats or Light green with deep blue jeans is a perfect option!")
elif occ=="formal" and typ=="Streetwear"and gender=="f":  
    print("It is advised not to wear streetwear to a formal occasion!")
