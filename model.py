class Model():
    # https://en.wikipedia.org/wiki/Observer_pattern
    def __init__(self):
        self.__observers = []
        self.stimuli = []
        self.responses = []
        self.state = None  # "response", "stimuli"

    def register_observer(self, observer):
        self.__observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)

    def add_response(self, response):
        self.responses.append(response)
        self.notify_observers()

    def add_stimuli(self, stimuli):
        self.stimuli.append(stimuli)
        self.notify_observers()

    def set_state(self, state):
        self.state = state
        self.notify_observers(state=self.state)
