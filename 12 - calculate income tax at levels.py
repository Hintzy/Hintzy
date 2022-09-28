#define two separate functions for calculating tax at the various levels
def tento20(income):
    tento20tax = int(0)
    tento20tax = (income-10000)*0.1
    tento20tax = "{:.2f}".format(tento20tax)
    return str(tento20tax)

def twenplus(income):
    twenplustax = 1000 + (income-20000)*0.2
    twenplustax = "{:.2f}".format(twenplustax)
    return str(twenplustax)

#define the income tax function based on user input
def calc_tax(income):

    #determine tax for the less than $10000 bracket
    if income < 10001:
        print ("The income level is not great enough to incur income tax.")
    
    #determine tax for the greater than $10000, but less than $20000 bracket
    #referencing previously created functions
    if income >= 10001 and income <= 20000:
        print ("Total taxable income = $"+tento20(income))
        
    if income >= 20001:
        print ("Total taxable income = $"+twenplus(income))   

income = int(input("Please provide an annual income: "))
calc_tax(income)