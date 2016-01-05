from eventSourceMixin import EventSourceMixin

class ObservedObject(EventSourceMixin):
    def triggerThem(self):
        print "About to trigger the mainEvent..."
        self.triggerEvent("mainEvent")

class ObservingObject(object):
    def __init__(self, nameString):
        self.name = nameString

    def printThatEventWasTriggered(self):
        print self.name + " was notified that event was triggered"

    def startObserving(self, anObservedObject):
        anObservedObject.whenEventDo("mainEvent", self.printThatEventWasTriggered)

    def stopObserving(self, anObservedObject):
        anObservedObject.whenEventDoNot("mainEvent", self.printThatEventWasTriggered)

observed = ObservedObject()
observed.triggerThem()
observer1 = ObservingObject("observer1")
observer2 = ObservingObject("observer2")
observer3 = ObservingObject("observer3")
observer4 = ObservingObject("observer4")
observer5 = ObservingObject("observer5")
observer1.startObserving(observed)
observer2.startObserving(observed)
observer3.startObserving(observed)
observer4.startObserving(observed)
observer5.startObserving(observed)
observed.triggerThem()
observer1.stopObserving(observed)
observer2.stopObserving(observed)
observer3.stopObserving(observed)
observer4.stopObserving(observed)
observer5.stopObserving(observed)
observed.triggerThem()
