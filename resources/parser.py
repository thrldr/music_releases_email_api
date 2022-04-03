from flask_restful import reqparse


def make_parser(arguments: list) -> reqparse.RequestParser:
    parser = reqparse.RequestParser()
    for argument in arguments:
        parser.add_argument(argument,
                type=str,
                required=True,
                help=f"Field '{argument}' cannot be omitted."
            )
    return parser
