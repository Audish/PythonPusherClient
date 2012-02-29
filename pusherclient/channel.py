from collections import defaultdict

class Channel():
    def __init__(self, channelName):
        self.name = channelName
        self.event_callbacks = defaultdict(list)
    def bind(self, eventName, callback):
        self.event_callbacks[eventName].append(callback)
    def trigger(self, eventName, data):
        raise NotImplementedError()
    def _handle_event(self, eventName, data):
        for callback in self.event_callbacks[eventName]:
            callback(eventName, data)
        for callback in self.event_callbacks[None]:
            callback(eventName, data)
