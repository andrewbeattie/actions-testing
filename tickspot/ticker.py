from pprint import PrettyPrinter
from argparse import ArgumentParser
from tickspot.net.tickspot import fetch, create


def main():
    parser = ArgumentParser(prog="TickSpot")
    subparsers = parser.add_subparsers(help="help for subcommands")
    parser_list = subparsers.add_parser("list")
    parser_list.set_defaults(func=fetch)
    parser_list.add_argument(
        "category",
        choices=["project", "task"],
        type=str,
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
        "-ho", "--hours", type=float, help="How many hours to use when creating an entry."
    )
    parser_create.add_argument(
        "-p", "--project", type=int, help="Project id as int to use when creating an entry."
    )
    parser_create.add_argument(
        "-t", "--task", type=int, help="Task id to use as int when creating an entry."
    )
    parser_create.add_argument(
        "-d", "--date", help="Date to use when creating an entry in the format %Y-%m-%d."
    )
    parser_create.add_argument(
        "-v",
        "--vacation",
        choices=[True, False],
        type=bool,
        help="If we should try to pull holiday information that information must be filled out in the config.yaml file",
    )
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    """Examples of How To Use
    tickspot list project
    tickspot list task 11934
    tickspot create -p 11934 -t 12319 -ho 8 -d 2021-07-16
    """
    main()
