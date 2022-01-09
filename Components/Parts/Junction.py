from typing import Tuple, List, Dict
from constants import JUNCTION_ATTRIBUTES, JUNCTION_DEFAULT_COLOR
from Components.Parts.Figure import Figure


class Junction(Figure):
    """ Class representing junction from .net.xml file """

    def __init__(self, attributes: dict):
        super().__init__(JUNCTION_DEFAULT_COLOR)
        # Main attributes of Junction
        self.attributes: dict = {key: value for key, value in attributes.items() if key in JUNCTION_ATTRIBUTES}
        # Mapping incoming routes to possible out-coming routes
        self.neighbours: Dict[int, List[int]] = {}
        self.marker_size: int = 5
    
    def add_connection(self, from_route_id: int, route_id: int) -> None:
        """
        :param from_route_id: incoming route to this node
        :param route_id: route going from this node (if we came into junction using from_route)
        :return: None
        """
        if from_route_id not in self.neighbours:
            self.neighbours[from_route_id] = []
        self.neighbours[from_route_id].append(route_id)

    def remove_out_route(self, route_id: int) -> None:
        """
        :param route_id: of route to be removed
        :return: None
        """
        for in_route_id, out_routes in self.neighbours.items():
            if route_id in out_routes:
                # Remove mapping from list
                out_routes.remove(route_id)

    def remove_in_route(self, route_id: int) -> None:
        """
        :param route_id: to be removed
        :return: None
        """
        assert (route_id in self.neighbours)
        self.neighbours.pop(route_id)

    def replace_in_route(self, in_route_id: int, new_in_route_id: int) -> None:
        """
        :param in_route_id: to be replaced
        :param new_in_route_id: replacing
        :return: None
        """
        assert (in_route_id in self.neighbours)
        assert (new_in_route_id not in self.neighbours)
        self.neighbours[new_in_route_id] = self.neighbours.pop(in_route_id)

    def travel(self, from_route: int) -> List[int]:
        """
        :param from_route: one of incoming routes, if equal to 0, returns all routes
        :return: list of routes
        """
        if not from_route:  # Return all possible out routes
            return self.get_out_routes()
        assert (from_route in self.neighbours)
        return self.neighbours[from_route]

    def get_position(self) -> Tuple[float, float]:
        """
        :return: Tuple containing (x, y) coordinates
        """
        return (float(self.attributes["x"]), float(self.attributes["y"]))

    def get_in_routes(self) -> List[int]:
        """
        :return: List of in_edge_id's
        """
        return list(self.neighbours.keys())

    def get_out_routes(self) -> List[int]:
        """
        :return: List of route_id's
        """
        return [route for route_list in self.neighbours.values() for route in route_list]

    def plot(self, axes, color: str = "") -> None:
        if self.render:
            color = (color if color != "" else self.color)
            pos: Tuple[float, float] = self.get_position()
            axes.plot(pos[0], pos[1], marker="o", markersize=self.marker_size, color=color)

    def __or__(self, other):
        """
        Merges with another junction (of same attributes), but with different connections

        :param other: junction
        :return: self
        """
        assert (isinstance(other, Junction))
        assert (self.attributes["id"] == other.attributes["id"])
        for in_route, out_routes in other.neighbours.items():
            if in_route not in self.neighbours:  # Add new mapping
                self.neighbours[in_route] = out_routes
            else:  # Merge out_routes
                for out_route_id in out_routes:
                    if out_route_id not in self.neighbours[in_route]:
                        self.neighbours[in_route].append(out_route_id)
        return self

    def __ror__(self, other):
        """
        :param other: junction
        :return: self.__or__(other)
        """
        return self.__or__(other)
