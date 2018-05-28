### Minimalist Event Framework
This is a very simple and minimalist event mixin.  Mix it into your class, and a client object can call...

```python
your_object.when_event_do("someEventName", self.my_event_handling_method)
```

...to register for notification when your object triggers the event named "someEventName".  To trigger "someEventName", just do this:

```python
self.trigger_event("someEventName")
```

When the client object no longer wishes to be notified of your event, it can unregister by calling...

```python
your_object.when_event_do_not("someEventName", self.my_event_handling_method)
```

Easy peasy!