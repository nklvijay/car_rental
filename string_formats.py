price=56
item="pen"
nos=1

order="I want {0} piece of {1}"  #--pass argumnets in format
print(order.format(nos,item))

order1="I want {} piece of {}"
print(order1.format(nos,item))

#--named index
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

