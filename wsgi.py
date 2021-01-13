"""First Entry For The WSGI Server."""

from src.masonite.app import App

from src.masonite.wsgi import package_response_handler
from src.masonite.helpers import config
from src.masonite.environment import LoadEnvironment

"""Instantiate Container And Perform Important Bindings
Some Service providers need important bindings like the WSGI application
and the application configuration file before they boot.
"""

LoadEnvironment()

container = App()

container.bind('WSGI', package_response_handler)
container.bind('Container', container)

container.bind('Providers', [])
container.bind('WSGIProviders', [])

"""Bind all service providers
Let's register everything into the Service Container. Once everything is
in the container we can run through all the boot methods. For reasons
some providers don't need to execute with every request and should
only run once when the server is started. Providers will be ran
once if the wsgi attribute on a provider is False.
"""

for provider in config('providers.providers'):
    located_provider = provider()
    located_provider.load_app(container).register()
    if located_provider.wsgi:
        container.make('WSGIProviders').append(located_provider)
    else:
        container.make('Providers').append(located_provider)

for provider in container.make('Providers'):
    container.resolve(provider.boot)

"""Get the application from the container
Some providers may change the WSGI Server like wrapping the WSGI server
in a Whitenoise container for an example. Let's get a WSGI instance
from the container and pass it to the application variable. This
will allow WSGI servers to pick it up from the command line
"""

application = container.make('WSGI')
