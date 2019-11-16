from exex_cli.application import application
from exex_cli.commands import ExtractCommand

if __name__ == "__main__":
    application.add(ExtractCommand())
    application.set_default_command("extract", is_single_command=True)
    application.run()
