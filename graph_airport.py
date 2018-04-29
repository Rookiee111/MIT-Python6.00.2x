class Airport(object):
  def __init__(self, airport_name):
    self.airport_name = airport_name
  
  def getName(self):
    return self.airport_name
  
  def __str__(self):
    return self.airport_name
  
class Flights(object):
  def __init__(self, src, dest):
    self.src = src
    self.dest = dest
  
  def getSource(self):
    return self.src
  
  def getDestination(self):
    return self.dest
  
  def __str__(self):
    return self.src.getName() + "->" + self.dest.getName()
  

class connectingFlight(object):
  def __init__(self):
    self.routes = {}
  
  def addAirport(self, airport):
    if airport in self.routes:
      raise ValueError("Airport already added")
    self.routes[airport] = []
  
  def addflights(self, routes):
    src = routes.getSource()
    dest = routes.getDestination()
    if src in self.routes and dest in self.routes[src]:
      raise ValueError("Route already added")
    self.routes[src].append(dest)
  
  def connectingAirport(self, airport):
    return self.routes[airport]
  
  def hasAirport(self, airport):
    return airport in self.routes
  
  def getAirport(self, airport_name):
    for name in self.routes:
      if name.getName() == airport_name:
        return name
    raise NameError(airport_name)
  
  def __str__(self):
    result = ''
    for src in self.routes:
      for dest in self.routes[src]:
        result = result + src.getName() + "->" + dest.getName() + "\n"
    return result[:-1]
  
class buildRoutes(connectingFlight):
  def addRoutes(self, routes):
    connectingFlight.addflights(self, routes)
    rev = Flights(routes.getDestination(), routes.getSource())
    connectingFlight.addflights(self, rev)

def buildGraph(graphType):
  g = graphType()
  
  for name in ("A1", "A2", "A3", "A4", "A5"):
        g.addAirport(Airport(name))

    g.addRoutes(flights(g.getAirport("A1"), g.getAirport("A2")))
    g.addRoutes(flights(g.getAirport("A1"), g.getAirport("A3")))
    g.addRoutes(flights(g.getAirport("A1"), g.getAirport("A4")))
    g.addRoutes(flights(g.getAirport("A2"), g.getAirport("A3")))
    g.addRoutes(flights(g.getAirport("A2"), g.getAirport("A4")))
    g.addRoutes(flights(g.getAirport("A2"), g.getAirport("A1")))
    g.addRoutes(flights(g.getAirport("A3"), g.getAirport("A4")))
    g.addRoutes(flights(g.getAirport("A4"), g.getAirport("A1")))
    g.addRoutes(flights(g.getAirport("A4"), g.getAirport("A2")))
    g.addRoutes(flights(g.getAirport("A4"), g.getAirport("A3")))
    g.addRoutes(flights(g.getAirport("A4"), g.getAirport("A5")))
    g.addRoutes(flights(g.getAirport("A5"), g.getAirport("A2")))
    g.addRoutes(flights(g.getAirport("A5"), g.getAirport("A3")))

    return g
  
 def printRoutes(path):
  result = ''
  for i in range(len(path)):
    result = result + path[i]
    if i != len(path) - 1:
      result = result + "->"
  return result 

def findPath(graph, start, end, path, shortest, toPrint = False):
  path = path + [start]
  if start == end:
    return path
  for airport in self.routes:
    if airport not in path:
      if shortest == None or if len(path) < len(shortest):
        newpath = Findflight(graph, airport, end, path, shortest, toPrint)
        if newpath != None:
          shortest = newpath
    elif toPrint:
      print("no flights found")
  return shortest 

def SP(graph, start, end, toPrint = False):
  return Findflight(graph, start, end, [], None, toPrint)

def testSP(source, destination):
  g = buildGraph(connectingFlight)
  sp = SP(g, g.getAirport(source), g.getAirport(destination), toPrint=True)
  if sp != None:
    print("flight from:", source, "to", destination, ":", printRoutes(sp))
  else:
    print("no flight from:", source, "to", destination)
  

  testSP("A1", "A5")
  
  
