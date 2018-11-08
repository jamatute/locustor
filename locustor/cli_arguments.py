# import os
# import sys
# import yaml
import logging
import argparse
import argcomplete


def load_parser():
    ''' Configure environment '''

    # Argparse
    parent_parser = argparse.ArgumentParser(add_help=False,
        description="Tool to execute locust and produce reports")
    group = parent_parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")

    parent_parser.add_argument("-u", "--user_cases", type=list,
                               default=['10', '100', '1000'],
                               help=' '.join(
                                   ['List of cases to test, where each item',
                                    'is an int with the number of users']))

    parent_parser.add_argument("url", type=str, help='Url to test')

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='subcommand', help='subcommands')
    subparser.add_parser('run', parents=[parent_parser])
    # compare_parser = subparser.add_parser('compare', parents=[parent_parser])

    argcomplete.autocomplete(parser)
    return parser


def load_logger(args):
    logging.addLevelName(logging.INFO, "[\033[36m+\033[0m]")
    logging.addLevelName(logging.ERROR, "[\033[31m+\033[0m]")
    logging.addLevelName(logging.DEBUG, "[\033[32m+\033[0m]")
    logging.addLevelName(logging.WARNING, "[\033[33m+\033[0m]")
    if args.verbose is 1:
        logging.basicConfig(level=logging.INFO,
                            format="  %(levelname)s %(message)s")
    elif args.verbose is 2:
        logging.basicConfig(level=logging.DEBUG,
                            format="  %(levelname)s %(message)s")
    elif args.quiet:
        logging.basicConfig(level=logging.ERROR,
                            format="  %(levelname)s %(message)s")
    else:
        logging.basicConfig(level=logging.WARNING,
                            format="  %(levelname)s %(message)s")
    return logging.getLogger('Main')
