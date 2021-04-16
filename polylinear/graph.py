from typing import (
    Callable, Iterator,
    List,
    Any,
    Optional,
    NoReturn,
    Dict
)
from dataclasses import dataclass


class MissingVertexException (Exception):
    """ MissingVertexException
    ==============================
    Exception for when there is an edge or vertex that miss completes the
    -----------
    network in a graph.
    -----------
    """
    ...


class ExistingVertexException (Exception):
    """ ExistingVertexException
    ===============================
    Thrown only when there is already an exising vertex for a give graph
    -----------
    """
    ...


@dataclass
class Vertex:
    Id: Any
    Value: Optional[Any] = None

    def __hash__(self) -> int:
        return hash(self.Id)


class Graph:
    """ Graph
    =============
    Implementation of the a graph class in python for use of interconnectivity
    between vertex indexing of edges.
    """

    def __init__(self, directed: bool = False) -> NoReturn:
        self.adjMap: Dict[Vertex, Dict[Vertex, Any]] = None
        self.isDirected: bool = directed
        self.__size = 0

    def __contains__(self, instance: Vertex) -> bool:
        ''' __contains__ (in)
        =========================
        uses pythons integrated search to see if the element is already a part of
        the edges connection list.
        '''
        return instance in self.adjMap.keys()

    def __iter__(self) -> Iterator[Vertex]:
        return iter(self.adjMap.keys())

    def Size(self) -> bool:
        return self.__size

    def isEmpty(self) -> bool:
        return self.__size == 0

    def getGraph(self) -> Dict[Vertex, Dict[Vertex, Any]]:
        return self.adjMap

    def add_vertex(
        self,
        id: Any,
        value: Optional[Any] = None
    ) -> None:
        """ add_vertex
        ==================
        Adds brand new vertex to the graph, no edges are added to the graphs new
        vertex unless defined.
        """
        if self.isEmpty():
            self.adjMap = {Vertex(id, value): {}}
        else:
            if Vertex(id, value) in self.adjMap.keys():
                raise ExistingVertexException()
            self.adjMap.update({Vertex(id, value): {}})
        self.__size += 1

    def remove_vertex(self, id: Any) -> Vertex:
        return

    def remove_edge(self) -> Any:
        return

    def add_edge(
        self,
        vertex_start: Vertex,
        vertex_end: Vertex,
        weight: Optional[Any] = None
    ) -> None:
        """ add_edge
        ================
        Addes an edge to the list of nodes and if the graph is bi-directional
        it adds the edge to both vertex's.
        """
        if self.isEmpty():
            raise MissingVertexException()
        if (vertex_start not in self.adjMap
                or vertex_end not in self.adjMap):
            raise MissingVertexException()

        if self.isDirected:
            self.adjMap[vertex_start].update({vertex_end: weight})
            self.adjMap[vertex_end].update({vertex_start: weight})
        else:
            self.adjMap[vertex_start].update({vertex_end: weight})

    def run_algo(func: Callable, *args, **kwargs) -> Any:
        """ run_algo
        ================
        runs surface level non changing algorithms on the graph to extract
        deep level information from paths.
        ### Params:
            * func (Callable): functional algorithm to differ size of object
            * *args (tuple): variadic parameter pack for the function use
            * **kwargs (dict): variadic parameter dictionary for function use \n
        ### Returns:
            * Any: return value of whatever the function is.
        """
        return func(*args, **kwargs)


if __name__ == '__main__':
    graph: Graph = Graph(directed=True)
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_edge(Vertex('A'), Vertex('A'), 10)
    graph.add_edge(Vertex('A'), Vertex('B'), 20)
    graph.add_edge(Vertex('A'), Vertex('C'), 30)
    print("Actual data:")
    print(graph.adjMap)

    '''
    {
        Vertex(Id='A', Value=None): {
            Vertex(Id='A', Value=None): 10,
            Vertex(Id='B', Value=None): 20,
            Vertex(Id='C', Value=None): 30
        },
        Vertex(Id='B', Value=None): {
            Vertex(Id='A', Value=None): 20
        },
        Vertex(Id='C', Value=None): {
            Vertex(Id='A', Value=None): 30
        }
    }
    '''
