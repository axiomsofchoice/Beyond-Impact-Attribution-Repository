This is a script to run our demo in fluid.

{{ d['populating-fluid.py|idio|pycon|pyg']['imports'] }}

We log in with a username/password from the env:

{{ d['populating-fluid.py|idio|pycon|pyg']['fluid-login'] }}


Now we will consider how to create bibliographic entries.

In Fluid, you can create objects via a unique name, or you can create an unnamed objects. In either case, Fluid will return the identifier for the item. If you create an object by name and this name already exists, the existing identifier is returned.

Here is a named object:
{{ d['populating-fluid.py|idio|pycon|pyg']['create-named-object'] }}

Here is an anonymous object:
{{ d['populating-fluid.py|idio|pycon|pyg']['create-anonymous-object'] }}


