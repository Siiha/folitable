import requests
from datetime import datetime
from tkinter import Tk,ttk
sessio = requests.Session()
start_window = Tk()
w2 = Tk()
def foli(x):
	dt = datetime.now()
	a = sessio.get(f'https://data.foli.fi/siri/sm/{x}')
	a.raise_for_status()
	a = a.json()
	r = []
	for i in a['result'][:3]:
		b = datetime.fromtimestamp(i['expectedarrivaltime'])
		c = b-dt
		d = round(c.total_seconds()/60)
		l = i['lineref']
		r.append((l,d))
	return r
table = ttk.Label(master=w2, font="Cantarell 25")
def output(x):
	start_window.destroy()
	update(x)
def update(x):
	f = foli(x)
	table_text=""
	for (i,j) in f:
		table_text+=f"{i} : {j}\n"
	table.config(text=table_text)
	table.pack()
	w2.after(60000,update,x)
def start(w):
	l1 = ttk.Label(master=start_window,text="Give bus stop id.")
	entry = ttk.Entry(master=start_window)
	b = ttk.Button(master=start_window,text="ok",command=lambda: output(entry.get()))
	l1.pack()
	entry.pack()
	b.pack()
start(start_window)
start_window.mainloop()
w2.mainloop()
