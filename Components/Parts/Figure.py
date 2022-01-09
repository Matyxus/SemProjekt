

class Figure:
    """ Super class for objects, that can be drawn """

    def __init__(self, color: str):
        self.color: str = color
        self.render: bool = True  # Default

    def plot(self, axes, color: str = "") -> None:
        """

        :param axes: pyplot axes on which plotting should be drawn
        :param color: that should be drawn (if none, default will be chosen)
        :return: None
        """
        raise NotImplementedError("Error, this functions serves as interface, and should be implemented by children")

    def set_color(self, color: str) -> None:
        """
        :param color: to be set
        :return: None
        """
        self.color = color

    def set_render(self, render: bool) -> None:
        """
        :param render: true if object can be drawn, false otherwise
        :return: None
        """
        self.render = render
