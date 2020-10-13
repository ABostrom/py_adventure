from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .world import *

from .io import CommandLineInterface

class GameManager():

    def __init__(self, world: Region) -> None:
        # initialise the command line interface.
        self._cli = CommandLineInterface()
        self._world : Region = world
        self._current_zone : Zone = self._world.get_current_zone()
        self._current_location : Location = None

    def change_zone(self, next_zone : Zone):
        self._current_location = None
        self._current_zone = next_zone

    def change_location(self, next_location: Location):
        self._current_location = next_location

    def run(self):

        if self._current_location  is None:
            self._cli.output(f"You arrive at {self._current_zone}")
            self._cli.output(f"Where would you like to explore?")
            for loc in self._current_zone.get_locations():
                self._cli.output(loc)
        else:
            self._cli.output(f"You arrive at {self._current_location}")
            self._cli.output(self._current_location.get_description())
            for poi in self._current_location.get_points_of_interest():
                self._cli.output(poi)


        current : CommandReceiver = self._current_zone if self._current_location is None else self._current_location

        # get the user input
        success = False
        data = {}
        while not success:
            input = self._cli.request_input(":>")

            # parse the input TODO: need to check parameters against expected args
            success, data = self._cli.parse_input(
                input, current.get_valid_commands())
            if not success:
                self._cli.output("not a valid command")
                continue

            success = current.receive_command(
                data["command"], data, self)
            if not success:
                self._cli.output("nothing appeared to happen")
