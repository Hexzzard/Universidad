import requests as req, time as ti, random as ra

sURL = 'http://127.0.0.1:5000/data2'

def Generate(id):

    for i in range(5):
        dData = {
        '01': ra.randint(+5,+20),
        '25': ra.randint(+5,+20),
        '10': ra.randint(+5,+20),
        'id': id
        }
    return dData

while 1:
    for i in range(5):
        dData = Generate(i)
        print(dData)
        rq =  req.post(sURL,data=dData)
    ti.sleep(5)
rq.close() 

print(rq.txt)