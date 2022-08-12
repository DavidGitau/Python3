import dec

@dec.Dec2
def convert():
        choice = eval(input(
"""To convert enter the following options:
1 : Celcius to Fah 
2 : Fah to celcius 
Enter any other input to terminate.                -  
"""))
        return choice

convert()