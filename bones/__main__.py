"""bones.__main__: utility script for dice analysis.

usage: bones [args...]
       python -m bones [args...]

TODO: options, arguments, and usage notes
"""

__author__ = "Bradd Szonye <bszonye@gmail.com>"

__all__ = ["main"]

import sys
from importlib import import_module

from .pmf import PMF


def eval_demo(*expressions: str) -> None:
    """Evaluate expressions from the command line."""
    from . import __all__ as exports, __name__ as package_name

    package = import_module(package_name)
    module_names = ["color", "pmf", "roll", "warhammer"]

    g = {package_name: package}
    g |= {name: import_module(f".{name}", package_name) for name in module_names}
    g |= {name: getattr(package, name) for name in exports}

    for expression in expressions:
        v = eval(expression, g)
        if isinstance(v, PMF):
            if sys.__stdout__.isatty():  # pragma: no cover
                v.plot()
            else:
                print("\n".join(v.tabulate(":.2%")))
        elif v is not None:
            print(v)


def main() -> None:
    """Script entry point. Command-line interface TBD."""
    eval_demo(*sys.argv[1:])


if __name__ == "__main__":
    main()
    sys.exit(0)
