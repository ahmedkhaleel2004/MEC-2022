import time
import random
from tkinter import *

program = int(input("What mode would you like to open the program in? (1 = Normal, 2 = Test):\t")) #Ask the user what mode the program will be opened in (to simulate)

window = Tk() # Open window

while True: # While loop encompasses program code to keep updates going
  time.sleep(3)
  data = []
  for i in range(0,10): # Initialize data list, and simulate all ocean parameters using studied averages and deviations
    
    temp = round(random.normalvariate(14, 4), 3) # Temperature in Celsius
    wind = round(random.normalvariate(6.64, 2), 3) # Velocity in m/s
    uv = round(random.normalvariate(7, 2), 3) # UV index *no units*
    rain = round(random.normalvariate(10, 4), 3) # Precipitation in mm
    pressure = round(random.normalvariate(101, 7), 3) #Pressure in kpa
    seismic = round(random.normalvariate(100, 30), 4) # Generate narrow curve, if less than 1, then rare event
    data.append([temp, wind, uv, rain, pressure, seismic])
    
  print(data) # Data list is now a list containing 9 lists, each with simulated values of bouy measurements
  
  counter = 0
  index = 0
  
  for i in range(0,3): # Begin iterating through rows and columns
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
  
    for j in range(0, 3): # Format each generated frame
      frame = Frame(
          master=window,
          relief=RAISED,
          borderwidth=1
      )
      counter + 1
      frame.grid(row=i, column=j, padx=5, pady=5) # Generate table cells
      frame1 = Label(master=frame, text=f"Bouy {counter + 1}") # Display the Bouy number
      frame1.pack(padx=5, pady=5)
      
      '''

      From now on, we will set if statements that define the ideal ranges of each ocean parameter. Good is green, yellow is less than ideal, red is bad.
      
      '''
      
      colour_temp = ""
      if data[counter][index] < 10: 
        colour_temp = "blue"
      elif data[counter][index] > 18:
        colour_temp = "red"
      else:
        colour_temp = "green"
        
      frame2 = Label(master=frame, text=f"Temperature: {data[counter][index]} °C", bg=colour_temp) # For each parameter, display the value, units, and set frame colour
      frame2.pack(padx=0, pady=0)

      colour_wind = ""
      if data[counter][index + 1] < 4:
        colour_wind = "green"
      elif data[counter][index + 1] > 18:
        colour_wind = "red"
      else:
        colour_wind = "yellow"
      
      frame3 = Label(master=frame, text=f"Wind Velocity: {data[counter][index + 1]} m/s", bg=colour_wind)
      frame3.pack(padx=0, pady=0)

      colour_uv = ""
      if data[counter][index + 2] < 3.5:
        colour_uv = "green"
      elif data[counter][index + 2] > 9.5:
        colour_uv = "red"
      else:
        colour_uv = "yellow"
      
      frame4 = Label(master=frame, text=f"UV Index: {data[counter][index + 2]}", bg=colour_uv)
      frame4.pack(padx=0, pady=0)

      colour_rain = ""
      if data[counter][index + 3] < 5:
        colour_rain = "green"
      elif data[counter][index + 3] > 15:
        colour_rain = "red"
      else:
        colour_rain = "yellow"
      
      frame5 = Label(master=frame, text=f"Percipitation: {data[counter][index + 3]} mm", bg=colour_rain)
      frame5.pack(padx=0, pady=0)

      colour_pressure = ""
      if data[counter][index + 4] < 95 or data[counter][index + 4] > 105:
        colour_pressure = "red"
      elif data[counter][index + 4] < 98 or data[counter][index + 4] > 102:
        colour_pressure = "yellow"
      else:
        colour_pressure = "green"
      
      frame6 = Label(master=frame, text=f"Air Pressure: {data[counter][index + 4]} kPa", bg=colour_pressure)
      frame6.pack(padx=0, pady=0)

      colour_seismic = ""
      seismic_statement = ""
      if data[counter][index + 5] < 50 or data[counter][index + 5] > 150:
        seismic_statement = "Seismic activity detected!"
        colour_seismic = "red"
      else:
        seismic_statement = "No seismic activity"
        colour_seismic = "green"
      
      frame7 = Label(master=frame, text=seismic_statement, bg=colour_seismic)
      frame7.pack(padx=0, pady=0)
      
  
      counter+=1 # This counter makes sure each table cell is taking its respective values from data list
  window.update() # Update the screen
window.mainloop() # Display the screen
