from Components.Parts.Figure import Figure
from constants import EDGE_ATTRIBUTES, LANE_ATTRIBUTES, EDGE_DEFAULT_COLOR


class Edge(Figure):
    """ Class describing edge from .net.xml file, subclass of Figure """

    def __init__(self, attributes: dict):
        super().__init__(EDGE_DEFAULT_COLOR)
        self.attributes = {key: value for key, value in attributes.items() if key in EDGE_ATTRIBUTES}
        self.lanes: dict = {}

    def add_lane(self, lane: dict) -> None:
        """

        :param lane: dictionary holding attributes of lane
        :return: None
        """
        self.lanes[lane["id"]] = {key: lane[key] for key in lane if key in LANE_ATTRIBUTES}
        self.attributes["length"] = float(lane["length"])

    def travel(self) -> tuple:
        """
        :return: Tuple containing destination junction id and length
        """
        return (self.attributes["to"], self.attributes["length"])

    def get_lane_shape(self, lane_id: str) -> list:
        """
        :param lane_id: of lane
        :return: list of lists containing pairs of x,y coordinates
        """
        points: list = self.lanes[lane_id]["shape"].split()
        points = [list(map(float, i.split(","))) for i in points]
        return points

    def plot(self, axes, color: str = "") -> None:
        if self.render:
            color = (color if color != "" else self.color)
            for lane_id in self.lanes:
                # [[x, y], [x, y], ...]
                points: list = self.get_lane_shape(lane_id)
                for i in range(1, len(points)):
                    x: list = [points[i-1][0], points[i][0]]
                    y: list = [points[i-1][1], points[i][1]]
                    axes.plot(x, y, linewidth=1, color=color)
