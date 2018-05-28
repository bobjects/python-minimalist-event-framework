from eventSourceMixin import EventSourceMixin


class ObservedObject(EventSourceMixin):
    def trigger_them(self):
        print "About to trigger the mainEvent..."
        self.trigger_event("mainEvent")


class ObservingObject(object):
    def __init__(self, name_string):
        self.name = name_string

    def print_that_event_was_triggered(self):
        print self.name + " was notified that event was triggered"

    def start_observing(self, an_observed_object):
        an_observed_object.when_event_do("mainEvent", self.print_that_event_was_triggered)

    def stop_observing(self, an_observed_object):
        an_observed_object.when_event_do_not("mainEvent", self.print_that_event_was_triggered)


observed = ObservedObject()
observed.trigger_them()
observer1 = ObservingObject("observer1")
observer2 = ObservingObject("observer2")
observer3 = ObservingObject("observer3")
observer4 = ObservingObject("observer4")
observer5 = ObservingObject("observer5")
observer1.start_observing(observed)
observer2.start_observing(observed)
observer3.start_observing(observed)
observer4.start_observing(observed)
observer5.start_observing(observed)
observed.trigger_them()
observer1.stop_observing(observed)
observer2.stop_observing(observed)
observer3.stop_observing(observed)
observer4.stop_observing(observed)
observer5.stop_observing(observed)
observed.trigger_them()
