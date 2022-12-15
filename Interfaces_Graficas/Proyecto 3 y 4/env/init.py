from flask import Flask, render_template, request
import telepot
import time
import json
import folium
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route("/",methods=['GET'])
def inicio():
    return render_template('home.html')

global data1 
data1 = []
global Dtime
Dtime = []

sc =[[],[],[],[],[]]

@app.route("/data",methods=['GET', 'POST'])
def hello():

    if request.method == 'POST':
        if len(Dtime)> 50:
            Dtime.pop(0)
            data1.pop(0)
        data1.append(request.form)
        Dtime.append({
            "time": time.strftime("%H:%M:%S")
            })
        print(Dtime)

        return {"success": True}

@app.route("/data2",methods=['GET', 'POST'])
def data2():

    if request.method == 'POST':
        if len(Dtime)> 10:
            Dtime.pop(0)
            sc[0].pop(0)
            sc[1].pop(0)
            sc[2].pop(0)
            sc[3].pop(0)
            sc[4].pop(0)
        sc[int(request.form["id"])].append(request.form)
        if len(Dtime) != 0:
            if (Dtime[len(Dtime)-1]["time"] != time.strftime("%H:%M:%S")):
                Dtime.append({
                "time": time.strftime("%H:%M:%S")
                })
        else:
            Dtime.append({
                "time": time.strftime("%H:%M:%S")
            })

        return {"success": True}

@app.route("/getdata",methods=['GET', 'POST'])
def getdata():

    if request.method == 'POST':
        print(data1)
        return [data1, Dtime]
    else:
        return render_template('test.html')

@app.route("/getdata2",methods=['GET', 'POST'])
def getdata2():

    if request.method == 'POST':
        return [sc[json.loads(request.data)["id"]],Dtime]
    else:
        return render_template('test.html')

@app.route('/Telebot',methods=['POST'])
def Telebot():
    if request.method == 'POST':

        img = request.files.get('imagen')
        img.save('test.png')
        bot = telepot.Bot('5890117421:AAH4SL5DoBZuXvMR7z9poV51f4dT_1C0JzE')
        
        #id de telegram
        bot.sendPhoto(1552297914, photo=open('test.png', "rb")) 
        bot.sendPhoto(5212849344, photo=open('test.png', "rb"))
        
        return {"success": True}

@app.route("/mapa",methods=['GET', 'POST'])
def mapa():

    if request.method == 'POST':
        return [data, Dtime]
    else:
        return render_template('test2.html')



conex = sqlite3.connect('gps.db')
c=conex.cursor()
c.execute("SELECT * FROM data ORDER BY fecha")
dt = c.fetchall()

data = pd.DataFrame.from_records(dt[1:],columns=dt[0])

place_lat = data.iloc[:,2].values.astype(float).tolist()
place_lng = data.iloc[:,3].values.astype(float).tolist()
ids = data.iloc[:,1].values.astype(int).tolist()
vel = data.iloc[:,5].values.astype(int).tolist()

@app.route("/carro")
def home():
    map = folium.Map(
        location=[-38.739596, -72.601606],
        zoom_start=12
    )
    map.get_root().html.add_child(folium.Element("""
    <input type=button onClick="enviar(1)" value='carro 1'>
    <input type=button onClick="enviar(2)" value='carro 2'>
    <input type=button onClick="enviar(3)" value='carro 3'>
    <input type=button onClick="enviar(4)" value='carro 4'>
    <input type=button onClick="enviar(5)" value='carro 5'>
    <input type=button onClick="enviar(6)" value='carro 6'>
    <input type=button onClick="enviar(7)" value='carro 7'>
    <input type=button onClick="enviar(8)" value='carro 8'>
    <input type=button onClick="enviar(9)" value='carro 9'>
    <input type=button onClick="enviar(10)" value='carro 10'>

    <script>
    function delay(milliseconds){
    return new Promise(resolve => {
      setTimeout(resolve, milliseconds);
    });
    }
    async function enviar(data){
        console.log(JSON.stringify({'id': data}));
      fetch('/Dcarro',{
        method : 'POST',
        body: JSON.stringify({"id": data})
      }).then(response =>{
        return response.json();
      }).catch(error =>console.error(error));
      await delay(200);
      console.log("redireccionando");
      location.replace("http://127.0.0.1:5000/Dcarro")
       
    }
    </script>
    """))
    map.save("templates/out.html")
    return map._repr_html_()

@app.route("/Dcarro",methods=['POST', 'GET'])
def carro():
    if request.method == 'POST':
        id = json.loads(request.data)["id"]
        points = []
        for i in range(len(ids)):
            if ids[i]==id:
                points.append([place_lat[i], place_lng[i]])
        map = folium.Map(
            location=[-38.739596, -72.601606],
            zoom_start=12
        )
        folium.Marker(
            location=points[0],
            tooltip="Punto de partida",
            icon=folium.Icon(color='green')
        ).add_to(map)
        folium.Marker(
            location=points[-1],
            tooltip="Destino",
            icon=folium.Icon(color='black')
        ).add_to(map)
    
        folium.PolyLine(points, color='red',dash_array='5',opacity ='.85',
            tooltip ='Trayectoria'
            ).add_to(map)
    
        map.get_root().html.add_child(folium.Element("""
        <input type=button onClick="enviar(1)" value='carro 1'>
    <input type=button onClick="enviar(2)" value='carro 2'>
    <input type=button onClick="enviar(3)" value='carro 3'>
    <input type=button onClick="enviar(4)" value='carro 4'>
    <input type=button onClick="enviar(5)" value='carro 5'>
    <input type=button onClick="enviar(6)" value='carro 6'>
    <input type=button onClick="enviar(7)" value='carro 7'>
    <input type=button onClick="enviar(8)" value='carro 8'>
    <input type=button onClick="enviar(9)" value='carro 9'>
    <input type=button onClick="enviar(10)" value='carro 10'>

    <script>
    function delay(milliseconds){
    return new Promise(resolve => {
      setTimeout(resolve, milliseconds);
    });
    }
    async function enviar(data){
        console.log(JSON.stringify({'id': data}));
      fetch('/Dcarro',{
        method : 'POST',
        body: JSON.stringify({"id": data})
      }).then(response =>{
        return response.json();
      }).catch(error =>console.error(error));
      await delay(200);
      console.log("redireccionando");
      location.replace("http://127.0.0.1:5000/Dcarro")
       
    }
    </script>
    """))
        map.save("templates/out.html")
        return {"success": True}
    if request.method == 'GET':
        return render_template('out.html')

    
if __name__ == "__main__":
    app.run(debug=True)
