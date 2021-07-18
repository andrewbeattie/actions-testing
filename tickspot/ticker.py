from pprint import PrettyPrinter
from argparse import ArgumentParser
from tickspot.net.tickspot import fetch, create

if __name__ == "__main__":
    """Examples of How To Use
    tickspot list project
    tickspot list task 11934
    tickspot create -p 11934 -t 12319 -ho 8 -d 2021-07-16
    """

    parser = ArgumentParser(prog="TickSpot")
    subparsers = parser.add_subparsers(help="help for subcommands")
    parser_list = subparsers.add_parser("list")
    parser_list.set_defaults(func=fetch)
    parser_list.add_argument(
        "category",
        choices=["project", "task"],
        help="Defines the action to take, can be either task, project or entry",
    )
    parser_list.add_argument(
        "-p",
        "--project",
        type=int,
        help="To return tasks we require that a project id is provided.",
    )
    parser_create = subparsers.add_parser("create")
    parser_create.set_defaults(func=create)

    parser_create.add_argument(
        "-ho", "--hours", help="How many hours to use when creating an entry."
    )
    parser_create.add_argument("-p", "--project", help="Project id to use when creating an entry.")
    parser_create.add_argument("-t", "--task", help="Task id to use when creating an entry.")
    parser_create.add_argument(
        "-d", "--date", help="Date to use when creating an entry in the format %Y-%m-%d."
    )
    parser_create.add_argument(
        "-v", "--vacation", help="Country, state or province to check if there is a holiday."
    )
    args = parser.parse_args()
    args.func(args)
