def get_num(x_value, domain, steps): # defining the function
    points = [] # initiate the list "points"
    for i in range(int(domain[0]/steps+1), int(domain[1]/steps)+1): # Calculating the number of repetitions needed, to cover the whole domain.
        x_v = round((i*steps), 2) # rounds the x-values to more or less normal values because of the problem that is explained below
        points.append(round(float(x_value[0] * x_v ** 3 + x_value[1] * x_v ** 2 + x_value[2] * x_v + x_value[3]), 7)) # calculating the y-values of the x-values according to the function
    o = open("points.txt", "a") # Opens the file points.txt and appends all the y-values separated by a line break.
    text = str() # defines "text" as a string, "text" will later contain the packed y-values
    for i in range(len(points)): # for loop with as many repetitions as there are y-values
        text = text+str(points[i])+"\n" # changing the list-data into a string and organize it beautifully
    o.write(text) # writes text in file
    o.close() # closes the file so it gets saved and the file updates
    return points # returns the list "points" as an first impression for the user in the interface

if __name__ == "__main__":
    ### Variabler Bereich ###
    x_value = [0,-0.1,2,-4.4] # a*x^3+b*x^2+c*x+d -> x_value = [a,b,c,d]
    domain = [10,17.5] # Bereich der Zahlen zumbeispiel vom x=12 bis x=18 alle Punkte
    steps = 0.05 # schritte pro ganze Zahl also wenn steps=0.1 dann werden 10 punkte in der Domain x=1 bis x=2
    ### /Variabler Bereich/ ###

    print(get_num(x_value, domain, steps)) # execute the function


### Problem ###
# If you divide 1.4 by 7 you will not get 0.2 (what you would normally expect) but you get 0.19999999999999998
# because of the way a float number is saved in the computer.
# This may lead to little aberrances in the float-number calculated.
# The following link will explain it in more depth:
# https://docs.python.org/3/tutorial/floatingpoint.html
### /Problem/ ###