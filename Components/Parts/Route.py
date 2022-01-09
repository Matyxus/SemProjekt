from Components.Parts.Figure import Figure
from constants import EDGE_DEFAULT_COLOR


class Route(Figure):
    """
        Route is class holding edges, trough which the route goes
    """
    def __init__(self, id: int, edges: list):
        super().__init__(EDGE_DEFAULT_COLOR)
        self.id = id
        self.edge_list: list = edges

    def travel(self) -> list:
        """
        :return: List of edge ids forming route
        """
        return self.edge_list

    def last_edge(self) -> str:
        """
        :return: Id of last edge on route
        """
        return self.edge_list[-1]

    def first_edge(self) -> str:
        """
        :return: Id of first edge on route
        """
        return self.edge_list[0]

    def plot(self, axes, color: str = "") -> None:
        raise NotImplementedError("Error, plotting of route must be called from RouteManager")

    def __or__(self, other):
        """
        :param other:
        :return:
        """
        if isinstance(other, Route):
            for edge_id in other.edge_list:
                self.edge_list.append(edge_id)
        return self

    def __ror__(self, other):
        """
        :param other:
        :return:
        """
        return self.__or__(other)

    def __str__(self) -> str:
        """
        :return:
        """
        return f"Route: {self.id}, path: {self.edge_list}\n"
