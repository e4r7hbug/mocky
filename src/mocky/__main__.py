"""Mocked POSIX commands."""
import pathlib
import sys
import functools

import coloredlogs

coloredlogs.install(level='DEBUG')
LOG = coloredlogs.logging.getLogger(__package__)


def command_squash():
    """Squash command and arguments together."""
    command, *args = sys.argv
    command_name = pathlib.Path(command).name
    return ' '.join([command_name] + args)


debug = functools.partial(LOG.debug, '%s', command_squash())
info = functools.partial(LOG.info, '%s', command_squash())
warning = functools.partial(LOG.warning, '%s', command_squash())
error = functools.partial(LOG.error, '%s', command_squash())
critical = functools.partial(LOG.critical, '%s', command_squash())
fatal = functools.partial(LOG.fatal, '%s', command_squash())


def main():
    """Main entry point."""
    LOG.info('Not meant for direct consumption.')


if __name__ == '__main__':
    main()
