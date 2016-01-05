### Minimalist Event Framework
This is a very simple and minimalist event mixin.  Mix it into your class, and a client object can call...

```python
yourObject.whenEventDo("someEventName", self.myEventHandlingMethod)
```

...to register for notification when your object triggers the event named "someEventName".  To trigger "someEventName", just do this:

```python
self.triggerEvent("someEventName")
```

When the client object no longer wishes to be notified of your event, it can unregister by calling...

```python
yourObject.whenEventDoNot("someEventName", self.myEventHandlingMethod)
```

Easy peasy!
