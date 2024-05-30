class Event:
    type = ''
    content = object
    message = ''

    def __init__(self, etype, content=None, message=''):
        self.type = etype
        self.content = content
        self.message = message


class EventListener:
    listening_to = []

    def __init__(self, event_handler, listening_to):
        self.event_handler = event_handler
        self.listening_to = listening_to
        for event in self.listening_to:
            if event not in self.event_handler.listeners.keys():
                self.event_handler.listeners[event] = []
            self.event_handler.listeners[event].append(self)

    def parse_event(self, event):
        pass


class EventBroadcaster:
    def __init__(self, event_handler):
        self.event_handler = event_handler

    def broadcast(self, event):
        self.event_handler.resolve(event)


class EventHandler:
    listeners = {}

    def resolve(self, event):
        # print(self.listeners)
        # print(event.type, event.content)
        if not (event.type in self.listeners.keys()):
            return
        for listener in self.listeners[event.type]:
            listener.parse_event(event)

