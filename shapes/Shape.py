import abc


class Shape(abc.ABC):

    @abc.abstractmethod
    def random_init(self):
        pass
