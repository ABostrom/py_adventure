from typing import Dict, List
from py_adventure import Entity

class Event:

    def __init__(self, event_id: str, event_type: str, event_contents: str) -> None:
        self._event_id = event_id
        self._event_type = event_type

        # nature of this to be decided on exactly in future. maybe event types
        # do need to be in an inheritance hierarchy?
        # combat events want source, target, damage, etc
        # travel events want character, to, from etc
        # for now just strings.
        self._event_contents = event_contents

    def get_event_id(self) -> str:
        return self._event_id

    def get_event_type(self) -> str:
        return self._event_type

    def get_event_contents(self) -> str:
        return self._event_contents

    def __str__(self) -> str:
        return self._event_contents


class EventMonitor:

    def __init__(self, event_types_monitored: List[str]) -> None:
        self._event_types_monitored = event_types_monitored

    def handle(self, event: Event) -> None:
        pass

    def get_types_monitored(self) -> List[str]:
        return self._event_types_monitored

class EventLog:

    def __init__(self) -> None:
        # maintains eventid -> event for quick lookup by exact id
        self._events : Dict[str, Event] = {}

        # maintains eventids in order of addition
        self._eventids_ordered : List[str] = []

        # maintains dict of event_types to list of event_ids for quick lookup by type
        self._events_by_type : Dict[str, List[str]] = {}

        # maintains dict of event types to list of entities that want to monitor events of that type
        self._event_type_monitors : Dict[str, List[EventMonitor]] = {}

    def log(self, event: Event) -> None:
        self._events[event.get_event_id()] = event
        self._eventids_ordered.append(event.get_event_id())

        if event.get_event_type() not in self._events_by_type:
            self._events_by_type[event.get_event_type()] = []
        self._events_by_type[event.get_event_type()].append(event.get_event_id())

        self._notify(event)

    def _notify(self, event : Event) -> None:
        if event.get_event_type() in self._event_type_monitors:
            for monitor in self._event_type_monitors[event.get_event_type()]:
                monitor.handle(event)

    def register_monitor(self, monitor : EventMonitor):
        for type in monitor.get_types_monitored():
            if type not in self._event_type_monitors:
                self._event_type_monitors[type] = []

            self._event_type_monitors[type].append(monitor)

    def get(self, event_id: str) -> Event:
        return self._events[event_id]

    def get_last(self) -> Event:
        return self._events[self._eventids_ordered[-1]]

    def get_last_of_type(self, event_type: str) -> Event:
        return self._events[self._events_by_type[event_type][-1]]

    def __str__(self) -> str:
        sb = []
        for event_id in self._eventids_ordered:
            event = self._events[event_id]
            sb.append(event.get_event_id() + " (" + event.get_event_type() + "): " + event.get_event_contents())

        return '\n'.join(sb)






