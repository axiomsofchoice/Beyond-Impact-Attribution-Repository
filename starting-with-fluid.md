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

However, for the goals of this project, the anonymous object makes more sense. While it is tempting to use DOIs as a name, this is problematic as you may not know a DOI when you are creating an object, and some formats of DOI are not suitable as fluidinfo names (even with url escaping). So it is more appropriate to use anonymous objects and set the DOI (if we have one) as a tag.
