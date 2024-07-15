#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 19:29:04 2020

@author: sakurajima
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
sns.set_style("white")
#Este proyecto hace  genera un Montecarlo con un modelo de beneficio de venta de un producto, tomando como
#variable input el precio del producto y como output el beneficio final

#Pendientes
# 
# 2. Señalar los intervalos de probabilidad
# 4. Replicar el modelo con otros tipos de distribución:
    # https://en.wikipedia.org/wiki/Log-normal_distribution 
    # PDF
#  Incluir:
    # Pearson https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearson3.html
    # Logistic
    # Student
    # numpy.random.Generator.lognormal
    # numpy.random.Generator.pareto
    # numpy.random.Generator.poisson
    # numpy.random.Generator.rayleigh
    # numpy.random.poisson
    # numpy.random.Generator.logistic
# 8. Verificar las interacciones entre los array de las variables input.
#tiene que permanecer una fija y la otra variar
    
#TERMINADO
# 6. Convertirlo en class
# 3. Entender la línea 26 la formula dentro de graph: es la pdf de la normal
# 7. lograr introducir dos variables input
# 1. Mejorar el aspecto de los gráficos
# 4. Agregar numpy.random.Generator.lognormal
    

class MonteCarlo:
    
    def __init__(self, iter, bins, mean, stdv, name):
        self.bins = bins
        self.stdv = stdv
        self.mean = mean
        self.iter = iter
        self.name = name
    
    #Creamos el array de la variable input con características de uns dist normal
    def input_array(self):#propongo llamarlo normal_array
        return np.random.normal(self.mean, self.stdv, self.iter)
    
    #Creamos el gráfico de la input
    def normal_pdf(self):#propongo llamarlo normal_pdf
    #encontré un problema le estamos en la siguiente linea estamos creando un array cuando ya hay un atributo input_array que lo genera.
        self.array_variable = np.random.normal(self.mean, self.stdv, self.iter)
        count, bins, ignored = plt.hist(self.array_variable, self.bins, density=True, color='c')
        
        plt.plot(bins, 1/(self.stdv* np.sqrt(2 * np.pi)) * np.exp( - (bins - self.mean)**2 / (2 * self.stdv**2) ), linewidth=2)
        # plt.plot(self.bins, 1/(self.stdv* np.sqrt(2 * np.pi)) * np.exp( - (self.bins - self.mean)**2 / (2 * self.stdv**2) ), linewidth=2)
        # after self.bins is the equation for the normal distribution statistics again!
        

        #https://stackoverflow.com/questions/20214497/annoying-white-space-in-bar-chart-matplotlib-python
        # plt.xlim([0,self.bins])
        plt.title('Normal Distribution input: {}'.format(self.name))
        plt.xlabel(self.name)
        # plt.xticks(np.arange(0, max(self.array_variable)))
        return plt.show()    

    def lognormal_pdf(self):
        rng = np.random.default_rng()
        self.s = rng.lognormal(self.mean, self.stdv, self.iter) #tengo duda que sea self.iter el ultimo argumento
        count, bins, ignored = plt.hist(self.s, 100, density=True, align='mid', color='c')  
        x = np.linspace(min(bins), max(bins), 10000)
        pdf = (np.exp(-(np.log(x) - self.mean)**2 / (2 * self.stdv**2)) / (x * self.stdv* np.sqrt(2 * np.pi)))
        plt.plot(x, pdf, linewidth=2)
        plt.axis('tight')
        plt.show()
    
    
    
    #Graficamos el output resultante
    def output(output_array, name):
        kwargs = dict(hist_kws={'alpha':.6}, kde_kws={'linewidth':2})
        sns.displot (output_array, color='c', kind='hist')
        #plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')
        plt.title('Results chart variable: {}'.format(name)) #cambiarlo al nombre del variable
        plt.xlabel(name)
        plt.xticks(np.arange(0, np.max(output_array), step=((np.max(output_array)-(np.min(output_array)))/(50/10))))
        plt.show()   



#Se genera un DF con los datos de inputs y outputs de la simulación
    def results_df(input1_array, input2_array, input1_name, input2_name, output_array, output_name):
        big_array = [input1_array, input2_array, output_array]
        big_array
        df = pd.DataFrame(big_array)
        dft = df.T
        dft.columns = [str(input1_name), str(input2_name), str(output_name)]
        return dft
        
