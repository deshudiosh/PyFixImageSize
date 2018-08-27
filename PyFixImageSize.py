import sys

import click


@click.command()
@click.argument("args", nargs=-1)
def cli(args):
    # with open("./test.txt", "w") as f:
    #     f.write(str(args))
    for arg in args:
        print(arg)



if getattr(sys, "frozen", False):
    cli()
else:
    cli(['C:\\Users\\pawelgrze\\Desktop\\tQ0WAjJ.jpg', 'C:\\Users\\pawelgrze\\Desktop\\VrayZdepthCalculator.exr'])
