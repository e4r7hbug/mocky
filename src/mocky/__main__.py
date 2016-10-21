"""Mocked POSIX commands."""
import coloredlogs

coloredlogs.install(level='DEBUG')
LOG = coloredlogs.logging.getLogger(__package__)


def main():
    """Main entry point."""
    LOG.info('Not meant for direct consumption.')


if __name__ == '__main__':
    main()
