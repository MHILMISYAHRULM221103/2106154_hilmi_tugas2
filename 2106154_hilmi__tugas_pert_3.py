# -*- coding: utf-8 -*-
"""2106154_hilmi_ tugas pert 3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/101y2u_2Q0u9tnWrKrnnSP6G1hZR4d-G5
"""

from traitlets.config import T
def astar(startNode, heuristics, graph, goalNode="Bucharest"):
  priorityQueue = queue.priorityQueue()
  distance = 0
  path = []

  priorityQueue.put((heuristics[startNode] + distance, [startNode, 0]))

  while priorityQueue.empty() == False:
    current = priorityQueue.get()[1]
    distance += int(current [1])

    if current [0] == goalNode:
      break

    priorityQueue = queue.priorityQueue()

    for i in graph[current[0]]:
        if i [0]not in path:
             priorityQueue.put((heuristics[i[0]] + int(i[1]) + distance, i))

  return path

def drawMap(city, gbfs, astar, graph):
    for i, j in city.items():
        plt.plot(j[0], j[1], "ro")
        plt.annotate(i, (j[0] + 5, j[1]))

    for k in graph[i]:
          n = city[k[0]]
          plt.plot([j[0], n[0]], n[1], "gray")
    for i in range(len(gbfs)):
     try:
        first = city[gbfs[i]]
        secend = city[gbfs[i + 1]]

        plt.plot([first[0], secent[0]], [first[1]], "green")
     except:
        continue
    for i in range(len(astar)):
     try:
        first = city[astar[i]]
        secend = city[astar[i + 1]]

        plt.plot([first[0], secend[0]], [first[1], [secend]], "blue")
     except:
        continue

    plt.errorbar(1, 1, label="GBFS", color="green")
    plt.errorbar(1, 1, label="ASTAR", color="blue")
    plt.legend(loc="lower left")

    plt.show()

def main():
    heuristic = getHeuristics()
    graph = createGraph()
    city, citiesCode = getCity()

    for i, j in citiesCode.items():
       print(i, j)

    while True:
       inputCode = int(input("masukan nomor asal (0 untuk keluar):"))

       if inputCode == 0:
        break  

    cityName = citiesCode[inputCode]

    gbfs = GBFS(cityName, heuristic, graph)
    astar = astar(cityName, heuristic, graph)
    print("GBFS => ", gbfs)
    print("ASTAR => ", astar)

    drawMap(city, gbfs, astar, graph)

    main()

import queue
import matplotlib.pyplot as plt

def gerHeuristics():
    heuristics = {}
    f = open("heuristics.txt")
    for i in f.readlines():
      node_heuristic_val = i.split()
      heuristics[node_heuristic_val[0]] = int (node_heuristic_val[1])

    return heuristic

def getCity():
    city ={}
    citiesCode = {}
    f = open("cities.txt")
    j = 1
    for i in f.readlines():
        node_city_val = i.split()
        city[node_city_val[0]] = [int(node_city_val[1]), int(node_city_val[2])]

        citiesCode[j] = node_city_val[0]
        j += 1

    return city,citiesCode

def createGraph():
    graph = {}
    file = open("citiesGraph.txt")
    for i in file.readlines():
        node_val = i.split()

        if node_val[0] in graph and node_val[1] in graph:
          c = graph.get(node_val[0])
          c.append([node_val[1], node_val[2]])
          graph.update({node_val[0]: c})

          c = graph.get(node_val[1])
          c.append([node_val[0], node_val[2]])
          graph.update({node_val[1]: c})

        elif node_val[0] in graph:
          c = graph.get(node_val[0])
          c.append([node_val[1], node_val[2]])
          graph.update({node_val[0]: c})

          graph[node_val[1]] = [[node_val[2]]]   

        elif node_val[1] in graph:
          c = graph.get(node_val[1])
          c.append([node_val[0], node_val[2]])
          graph.update({node_val[1]: c}) 

          graph[node_val[0]] = [[node_val[1], node_val[2]]]

    else:
         graph[node_val[0]] = [[node_val[1], node_val[2]]]
         graph[node_val[1]] = [[node_val[0], node_val[2]]]

    return graph

def GBFS(satrNode, heuristics, graph, goalNode="Bucharest"):
    priorityQueue = queue.priorityQueueu()
    priorityQueue.put((heuristics[startNode], starNode))

    path = []

    while priorityQueue.empty() == False:
      current = priorityQueue.get()[1]
      path.append(current)

      if current == goalNode:
          break

      priorityQueue = Queue.priorityQueue()

      for i in  graph [current]:
        if i[0] not in path:
            priorityQueue.put((heuristics[i[0]], i [0]))

    return path

def drawMap(city, gbfs, graph):
  for i, j in city.items():
    plt.plot(j[0], j[1], "ro")
    plt.annotate(i, (j[0] + 5, j[1]))

  for k in graph[i]:
    n = city[k[0]]
    plt.annotate([j[0], n[0]], [j[1], n[1]],"gray")

  for i in range(len(gbfs)):
    try:
        firs = city[gbfs[i]]
        secend = city[gbfs[i + 1]]

        plt.plot([first[0], secend[0]], [first[1], secend[1]], "green")
    except:
        continue

        plt.errorbar(1, 1, label="GBFS", color="green")
        plt.legend(loc="lower left")

        plt.show()
def main():
    heuristic = getHeuristics()
    graph = createGraph()
    city, citiesCode = getCity()

    for i, j in citiesCode.items():
        print(i, j)

    while True:
        inputCode = int(input("Masukan nomor kota asar (0 untuk keluar): "))

        if inputCode == 0:
          break
     
 
    cityName = citiesCode[inputCode]

    gbfs = GBFS(cityName, heuristic, graph)
    print("GBFS => ", gbfs)

    drawMap(city, gbfs, graph)

    main()