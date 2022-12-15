import requests as req, time as ti, random as ra

sURL = 'http://127.0.0.1:5000/data'

def Generate():
    dData = {
        '01': ra.randint(+5,+20),
        '25': ra.randint(+5,+20),
        '10': ra.randint(+5,+20),
        'te': ra.randint(-10,+10),
    }
    return dData

while 1:
    dData = Generate()
    print(dData)
    rq =  req.post(sURL,data=dData)
    ti.sleep(5)
rq.close() 

print(rq.txt)