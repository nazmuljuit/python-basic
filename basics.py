seconds = [1.2323442655, 1.4534345567, 1.023458894]
current = 1.10001399445
#append a value
seconds.append(current)
print(seconds)
#remove a value
seconds.remove(1.4534345567)
seconds.remove(1.023458894)
seconds.remove(1.10001399445)
print(seconds)
#list number
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])
#find specific value
print(serials[0], serials[2], serials[5])
#append the first item of weekend to workdays
workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])