import requests
from datetime import datetime
from tkinter import Tk,ttk
dt = datetime.now()
dt.microsecond
s = requests.Session()
w = Tk()
w2 = Tk()
def foli(x):
	dt = datetime.now()
	a = s.get(f'https://data.foli.fi/siri/sm/{x}').json()
	r = []
	for i in range(3):
		b = datetime.fromtimestamp(a['result'][i]['expectedarrivaltime'])
		c = b-dt
		d = round(c.total_seconds()/60)
		l = a['result'][i]['lineref']
		r.append((l,d))
	return r
l = [ttk.Label(master=w2,text="",font=("Liberation Sans",25)) for i in range(3)]
def output(x):
	w.destroy()
	update(x)
def update(x):
	f = foli(x)
	for i in range(3):
		l[i].config(text=f"{f[i][0]} : {f[i][1]}")
		l[i].pack()
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
