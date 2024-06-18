from events import EventBroadcaster, EventListener, Event


class BaseEquip(EventListener, EventBroadcaster):
    listening_to = []

    def __init__(self, event_handler):
        EventListener.__init__(self, event_handler)
        EventBroadcaster.__init__(self, event_handler)

    def parse_event(self, event):
        pass
