#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 23:02:28 2020

@author: sakurajima
"""
from MonteCarlo import MonteCarlo

# Para poder aplicar el MonteCarlo primero creamos el modelo de negocio en este caso benefits:
def benefits ( price, units, cost, name):
    # benefit = (price * units) - (cost*units) 
    benefit = (price - cost)*units
    return benefit, name

# Definimos las características de la variable input en este caso 'price'
iter = 10000 # número de iteraciones que tendrá el modelo
media_price = 7 
stdv_price = 1.2
cost = 4


# Creamos una instancia de la clase MonteCarlo:
first_input = MonteCarlo(iter, 20, media_price, stdv_price, 'Price') #cuando aumentas los bins la grafica queda la mitad vacía

#Generamos el atribute input_array de la clase MonteCarlo, genera un array
price = first_input.input_array()

# Utilizamos el atribute pdf para graficar la variable input
first_input.normal_pdf()
first_input.lognormal_pdf()
#here we create a second class instance for the units sold:
second_input = MonteCarlo(iter, 30, 500, 75, 'Units')#saca los valores de la ecuacion y crea variables 

units_array = second_input.input_array()
second_input.normal_pdf()


# Corremos el modelo benefits usando el  array generado en price (atribute the input_array)
profit, name = benefits(price, units_array, cost, 'Profit')

MonteCarlo.output(profit, name)#revisar el grafico parece ilogico

#I like to generate a Data Frame with all the scenarios generated
results = MonteCarlo.results_df(price, units_array, 'price', 'units', profit, 'profit')
results.to_csv('results.csv')


print(results)