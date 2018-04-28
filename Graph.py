#this is the implementation of the graph algorithm, In this we are going to build nodes and edges
#second part of this is, we are going find the shortest path using Depth First Search
#Creating a class for Node, this contains some basic methods to define the node
class Node(Object):
  
  def __init__(self, name):
    self.name = name
  
  def getName(self):
    return self.name
  
  def __str__(self):
    return self.name
  
 #Next creating a class for edges, this basically defines source and destination
class Edge(object):
  
  def __init__(self, src, dest):
    self.src = src
    self.dest = dest
  
  def getSource(self):
    return self.src
  
  def getDestination(self):
    return self.destination
  
  # The string representation of edges
  def __str__(self):
    return self.src.getName() + "->" + self.dest.getName()
  
  #Next we are going to build the Graph
  class Directed_graph(object):
    
    # we are going to define a dictionary, this will store the node ( parent ) as key and connecting nodes as values in a list
    def __init__(self):
      self.edges = {}
    
    # Next we are going to add a method to add the node to the dictionary
    def addNode(self, node):
      if node in self.edges:
        raise ValueError("node already exists")
      self.edges[node] = []
    
    #Next adding a method to add an edge
    def addEdge(self, edges):
      src = edges.getSource()
      dest = edges.getDestination()
      #check if the edge already exists
      if src in self.edges and dest in self.edges[src]:
        raise ValueError("Edge already exists")
      else:
        self.edges[src].append(dest) #adding the edge
    
    #Method to fetch the child node for each parent node
    def childOf(self, node):
      return self.edges[node]
    
    #method to check if the node exists
    def hasNode(self, node):
      return node in self.edges
    
    def getNode(self, name):
      for node in self.edges:
        if node.getName() == name:
          return name
      raise NameError(name)
   
    def __str__(self):
      result = ''
      for src in self.edges:
        for dest in self.edges[src]:
          result = result + src.getName() + "->" + dest.getName() + "\n
      return result[:-1]
    
   #class to create graphs  
  class Graph(Directed_graph):
    def addEdges(self, edges):
      Directed_graph(self, edges)
      reverse = Edge(edges.getDestination(), edges.getSource())
      Directed_graph(self, reverse)
  
  def buildGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'NewYork', 'Chicago', 'Denver', 'Phoenix', 'Los Angeles'):
          g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('NewYork')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('NewYork')))
    g.addEdge(Edge(g.getNode('NewYork'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('NewYork')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    
    return g
  
  print(buildCity(Directed_graph))
  
    
    
    
