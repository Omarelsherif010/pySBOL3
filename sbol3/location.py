import abc
from typing import Union

from . import *

int_property = Union[IntProperty, int]


class Location(Identified, abc.ABC):

    def __init__(self, name: str, type_uri: str) -> None:
        super().__init__(name, type_uri)
        self.orientation = URIProperty(self, SBOL_ORIENTATION, 0, 1)
        self.order = IntProperty(self, SBOL_ORDER, 0, 1)


class Range(Location):

    def __init__(self, name: str, start: int, end: int,
                 *, type_uri: str = SBOL_RANGE, ) -> None:
        super().__init__(name, type_uri)
        self.start: int_property = IntProperty(self, SBOL_START, 1, 1,
                                               initial_value=start)
        self.end: int_property = IntProperty(self, SBOL_END, 1, 1,
                                             initial_value=end)
        self.validate()

    def validate(self) -> None:
        super().validate()
        if self.start < 1:
            raise ValidationError('Start must be greater than 0')
        if self.end < 1:
            raise ValidationError('Start must be greater than 0')
        if self.end < self.start:
            raise ValidationError('End must be >= start')


class Cut(Location):

    def __init__(self, name: str, at: int,
                 *, type_uri: str = SBOL_RANGE, ) -> None:
        super().__init__(name, type_uri)
        self.at: int_property = IntProperty(self, SBOL_START, 1, 1,
                                            initial_value=at)
        self.validate()

    def validate(self) -> None:
        super().validate()
        if self.at < 0:
            raise ValidationError('At must be >= 0')


class EntireSequence(Location):

    def __init__(self, name: str, *, type_uri: str = SBOL_RANGE, ) -> None:
        super().__init__(name, type_uri)
        self.validate()