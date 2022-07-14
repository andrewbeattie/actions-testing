from argparse import ArgumentParser
from tickspot.net.tickspot import fetch, create, start


def main():
    parser = ArgumentParser(prog="TickSpot")
    subparsers = parser.add_subparsers(help="help for subcommands")
    parser_list = subparsers.add_parser("list")
    parser_list.set_defaults(func=fetch)
    parser_list.add_argument(
        "category",
        choices=["project", "task", "today"],
        type=str,
        help="Defines the action to take, can be either task, project or entry",
    )
    parser_list.add_argument(
        "-p",
        "--project",
        type=int,
        help="To return tasks we require that a project id is provided.",
    )
    parser_start = subparsers.add_parser("start")
    parser_start.set_defaults(func=start)
    parser_start.add_argument(
        "-p", "--project", type=int, help="Project id as int to use when creating an entry."
    )
    parser_start.add_argument(
        "-t", "--task", type=int, help="Task id to use as int when creating an entry."
    )
    parser_start.add_argument(
        "-m", "--message", type=str, help="Task id to use as int when creating an entry."

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
    ticker list project
    ticker list task 11934
    ticker create -p 1955215 -t 14519343 -ho 8 -d 2021-10-11
    ticker start -p <project> -t <task> -m <summary>
    """
    main()
