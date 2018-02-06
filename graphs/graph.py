"""
graph: Graphs for python 2 and 3.
"""

import StringIO

class Graph(object):
    """
    Represents a (possibly weighted) undirected graph.
    """

    def __init__(self, V, weighted = False):

        assert V > 0
        
        # the adjacency matrix
        self._adj = [ [ None ] * V for v in range(V) ]
        self._weighted = weighted
        
    @classmethod
    def from_file(cls, filename):
        """
        Creates a graph by reading the node and edge set
        from a file.
        """
        with open(filename, "rt") as f:
            lines = [ line.rstrip('\n') for line in f ]

            num_nodes, weighted = map(int, StringIO.StringIO(lines.pop(0)).getvalue().split())
            g = Graph(V=num_nodes, weighted=bool(weighted))
            
            for l in lines:
                if not l: continue

                edge = l.split()
                edge[0] = int(edge[0])
                edge[1] = int(edge[1])
                if weighted and len(edge) > 2:
                    edge[2] = float(edge[2])

                g.add_edge(*edge)
                
            return g
        
    def add_edge(self, source, target, weight=1):
        """
        Adds the edge (source, target) to the graph.
       
        Optional argument is the weight of the graph
        """
        assert weight != None
        
        try:
            self._adj[source-1][target-1] = weight
            self._adj[target-1][source-1] = weight
        except:
            if source <=0 or source > len(self._adj):
                print 'Invalid node: %d' % source
            if target <= 0 or target > len(self._adj):
                print 'Invalid node: %d' % target
        
    def __str__(self):
        edges = ''
        num_edges = 0
        for u in range(len(self._adj)):
            for v in range(u, len(self._adj)): # self edges included
                if self._adj[u][v] == None:
                    continue
                num_edges += 1
                edges += '(%d, %d)' % (u+1, v+1)
                if self._weighted:
                    edges += ', w = %.2f' % self._adj[u][v]
                edges += '\n'

        return '|V| = {}\n|E| = {}\n\n'.format(len(self._adj), num_edges) + edges
    
if __name__ == '__main__':
    g = Graph.from_file("test_graph.txt")
    print g
