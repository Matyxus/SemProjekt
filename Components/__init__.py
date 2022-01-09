from typing import Dict, Set, List
from Components.Parts.Route import Route
from Components.Parts.Edge import Edge
from Components.Parts.Junction import Junction
from copy import deepcopy


class Struct:
    """ Skeleton on Graph, defines junctions, edges, routes """

    def __init__(self):
        self.junctions: Dict[str, Junction] = {}
        self.edges: Dict[str, Edge] = {}
        self.routes: Dict[int, Route] = {}
        self.starting_junctions: Set[str] = set()
        self.ending_junctions: Set[str] = set()

    def get_skeleton(self):
        """
        :return: Struct, self
        """
        return self

    def load(self, other) -> None:
        """
        Loads attributes from other struct

        :param other: Struct Class
        :return: None
        """
        if isinstance(other, Struct):
            self.junctions = deepcopy(other.junctions)
            self.edges = deepcopy(other.edges)
            self.routes = deepcopy(other.routes)
            self.starting_junctions = deepcopy(other.starting_junctions)
            self.ending_junctions = deepcopy(other.ending_junctions)

    # ------------------------------ Utils ------------------------------

    def remove_junction(self, junction_id: str) -> None:
        """
        :param junction_id: to be removed
        :return: None
        """
        if junction_id not in self.junctions:
            return
        self.junctions.pop(junction_id, None)
        if junction_id in self.starting_junctions:
            self.starting_junctions.remove(junction_id)
        if junction_id in self.ending_junctions:
            self.ending_junctions.remove(junction_id)

    def remove_edge(self, edge_id: str) -> None:
        """
        :param edge_id: to be removed
        :return: None
        """
        if edge_id in self.edges:
            self.edges.pop(edge_id)
