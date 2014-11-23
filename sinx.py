#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Autor: Damian Giebas
Nr. indeksu: U-1203
Studia: Stacjonarne II stopień
Przedmiot: Metody numeryczne
Program jest pokazem różnicy między implementacją sinusa z biblioteki standardowej
a własną implementacją poprzez zliczenia iteracyjne, rekurencyjne i poprzez użycie
zliczenie wartości schematem hornera w danym punkcie
"""
import operator
import math

def silnia(n):
  """Implementacja funkcji silnia pochodzi ze strony http://pl.wikisource.org/wiki/Silnia/kod#Funkcjonalnie
  """
  return reduce(operator.mul, range(1, n+1)) if n>1 else 1
    
def step(x, w):
  return pow(x, w)/silnia(w)

def iteration(x, n, w=3):
  suma = x - step(x, w)
  w += 2
  plus = True
  for i in range(1, n):
    if plus:
      suma += step(x, w)
    else:
      suma -= step(x, w)
    plus = not plus
    w += 2
  return suma
  
def recuration(x, n, w=3, suma=0.0, plus=True):
  if n == 0:
    return suma
  if suma == 0.0:
    suma = x - step(x, w)
    w += 2
  if plus:
    suma += step(x, w)
  else:
    suma -= step(x, w)
  n -= 1
  w += 2
  return recuration(x, n, w, suma, not plus)
  
def horner(x, n, w=3, plus=False):
  max_w = w+n*2
  value_list = [ 1.0/silnia(v) for v in range(w, max_w, 2) ]
  
  def horner_sequence(x, value_list):
    if len(value_list) == 1:
      return value_list[0]
      
    last = value_list.pop()
    value_list[-1] -= pow(x, 2) * last
    return horner_sequence(x, value_list)
    
  return x - pow(x, 3) * horner_sequence(x, value_list)

x = float(raw_input("Podaj x: "))
n = int(raw_input("Podaj n: "))

print "Iteracyjnie: " + str(iteration(x, n))
print "Rekurencyjnie: " + str(recuration(x, n))
print "Horner: " + str(horner(x, n))
print "STDLIB sin: " + str(math.sin(x))
