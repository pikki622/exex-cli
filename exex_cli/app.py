from cleo import Application

from .commands import ExtractCommand

application = Application(name="exex-cli", version="0.1.0")
application.add(ExtractCommand())
