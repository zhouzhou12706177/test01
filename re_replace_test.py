import re


with open("./txt") as file:
    data = file.read()
    print data
    data = re.sub(r'defualtCuttentUnit "film"','defualtCuttentUnit "pal"',data)
    print data

properties = open("./txt","w")
properties.truncate()
properties.write(data)
properties.close()