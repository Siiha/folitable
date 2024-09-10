import requests
from datetime import datetime
from tkinter import Tk,ttk
s = requests.Session()
w = Tk()
w2 = Tk()
def foli(x):
	dt = datetime.now()
	a = s.get(f'https://data.foli.fi/siri/sm/{x}')
	a.raise_for_status()
	a = a.json()
	r = []
	for i in range(3):
		b = datetime.fromtimestamp(a['result'][i]['expectedarrivaltime'])
		c = b-dt
		d = round(c.total_seconds()/60)
		l = a['result'][i]['lineref']
		r.append((l,d))
	return r
table = ttk.Label(master=w2, font="Cantarell 25")
def output(x):
	w.destroy()
	update(x)
def update(x):
	f = foli(x)
	table_text=""
	for i in range(3):
		table_text+=f"{f[i][0]} : {f[i][1]}\n"
	table.config(text=table_text)
	table.pack()
	w2.after(60000,update,x)
def start(w):
	l1 = ttk.Label(master=w,text="Give bus stop id.")
	entry = ttk.Entry(master=w)
	b = ttk.Button(master=w,text="ok",command=lambda: output(entry.get()))
	l1.pack()
	entry.pack()
	b.pack()
start(w)
w.mainloop()
w2.mainloop()
