#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 21:41:32 2021

@author: Hang
"""

import matplotlib
matplotlib.use('TkAgg')
import requests
import bs4
import tkinter
import matplotlib.pyplot
import random
import agentframework # Create a class to give the agents(sheeps) attributes & behaviour
import matplotlib.animation 
from time import process_time

start = process_time()


# Scrapping website data to initiate the model later
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
# print(td_ys) to check whether data is properly scrapped
# print(td_xs) to check whether data is properly scrapped

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

num_of_agents = 10 
num_of_iterations = 100
agents = []
environment = []
neighbourhood = 20

# Read in environment data from in.txt
f = open("in.txt")
for row in f:
    parsed_row = str.split(row,",")
    rowlist = []
    for value in parsed_row:
        rowlist.append(float(value))
    environment.append(rowlist)

# Make the agents(sheeps), get them interact with the environment & initiate them with website data
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment,agents,y,x))

carry_on = True

def update(frame_number):
    
    fig.clear()
    global carry_on
    
    # Make sheeps randomly move, eat the environment and minteract with each other 
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            random.shuffle(agents) 
            """randomise the order in which agents are processed 
            to address model artifactrs"""
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)        
    
    # Plot the position of agents
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

# Create a stopping condition for the animation
def gen_function(b=[0]):
    global carry_on
    for i in range(len(agents)):
        agents[i].store < 4000 
        """stopping condition
        when every sheep has eaten at least 4000 units of grass"""
        yield carry_on
    else:
        carry_on = False

# Display the model as an animation and within a GUI
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Create the menu bar
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run", command=run) 

# Calculate the time to run the code
end = process_time()
time = end - start
print (time)

tkinter.mainloop()


