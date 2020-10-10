from typing import Dict, List

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

class EventLog:

    def __init__(self) -> None:
        # maintains eventid -> event for quick lookup by exact id
        self._events : Dict[str, Event] = {}

        # maintains eventids in order of addition
        self._eventids_ordered : List[str] = []

        # maintains dict of event_types to list of event_ids for quick lookup by type
        self._events_by_type : Dict[str, List[str]] = {}

    def log(self, event: Event) -> None:
        self._events[event.get_event_id()] = event
        self._eventids_ordered.append(event.get_event_id())

        if event.get_event_type() not in self._events_by_type:
            self._events_by_type[event.get_event_type()] = []
        self._events_by_type[event.get_event_type()].append(event.get_event_id())

    def get(self, event_id: str) -> Event:
        return self._events[event_id]

    def get_last(self) -> Event:
        return self._events[self._eventids_ordered[-1]]

    def get_last_of_type(self, event_type) -> Event:
        return self._events[self._events_by_type[event_type][-1]]

    def __str__(self) -> str:
        sb = []
        for event_id in self._eventids_ordered:
            event = self._events[event_id]
            sb.append(event.get_event_id() + " (" + event.get_event_type() + "): " + event.get_event_contents())

        return '\n'.join(sb)