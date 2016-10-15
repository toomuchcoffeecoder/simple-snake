from datetime import datetime

a = datetime.now()
while True:
    b = datetime.now()
    c = (b-a).microseconds
    print(c)



