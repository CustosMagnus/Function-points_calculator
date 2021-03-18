def get_num(x_value, domain, steps):
    points = []
    for i in range(int(domain[0]/steps+1), int(domain[1]/steps)+1):
        x_v = round((i*steps), 2)
        points.append(round(float(x_value[0] * x_v ** 3 + x_value[1] * x_v ** 2 + x_value[2] * x_v + x_value[3]), 7))
    o = open("points.txt", "a")
    text = str()
    for i in range(len(points)):
        text = text+str(points[i])+"\n"
    o.write(text)
    o.close()
    return points

if __name__ == "__main__":
    ### Variabler Bereich ###
    x_value = [0,-0.1,2,-4.4] # a*x^3+b*x^2+c*x+d -> x_value = [a,b,c,d]
    domain = [10,17.5] # Bereich der Zahlen zumbeispiel vom x=12 bis x=18 alle Punkte
    steps = 0.05 # schritte pro ganze Zahl also wenn steps=0.1 dann werden 10 punkte in der Domain x=1 bis x=2
    ### /Variabler Bereich/ ###

    print(get_num(x_value, domain, steps))

