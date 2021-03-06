import sys
from pathlib import Path

import click
from PIL import Image


def find_size_in_name(name: Path):
    """" search for WWWxHHH in filename and return as tuple"""
    try:
        n = name.stem
        extracted = [c if c in "1234567890x" else " " for c in n]
        extracted = "".join(extracted).split()
        extracted = [x for x in extracted if "x" in x]
        extracted = extracted[0]

        size = extracted.split("x")
        size = tuple(map(int, size))
        assert len(size) == 2
    except:
        size = None

    return size


def crop_if_needed(arg: Path):
    """ Apply crop to image based on filename template: "filename_WWWxHHH.ext" """
    expected_size = find_size_in_name(arg)
    img = Image.open(arg) # type: Image.Image

    # if image size doesn't match it's name
    if expected_size != img.size and expected_size is not None:
        img.crop((0, 0, *expected_size)).save(fp=arg, subsampling=0, quality=100)
        click.echo(arg)
        return img
    else:
        return None


def validate_image(arg) -> Path:
    """ Return if arg is existing file and is jpg or png"""
    p = Path(arg)
    return p if p.is_file() and p.suffix in ['.jpg', '.png'] else None


@click.command()
@click.argument("args", nargs=-1)
def cli(args):
    click.echo("List of cropped images:")

    images = [validate_image(arg) for arg in args if validate_image(arg) is not None]
    [crop_if_needed(img) for img in images]

    click.confirm('Cropping done ♥ Happy?')


def test():
    for n in [Path('C:\\Users\\pawelgrze\\Desktop\\do testu\\test_970x600 copy 4.jpg'),
              Path('test_970x600 (copy 4).jpg'),
              Path('test 076x334 (1)'),
              Path('test2_076x334 (1)')]:
        print(find_size_in_name(n))


    # cli([,
    #      'C:\\Users\\pawelgrze\\Desktop\\do testu\\dobre_400x400.jpg',
    #      'C:\\Users\\pawelgrze\\Desktop\\do testu\\nazwa1.jpg',
    #      'C:\\Users\\pawelgrze\\Desktop\\do testu\\nazwa2_100_499.jpg',
    #      'C:\\Users\\pawelgrze\\Desktop\\5490155_555x555.jpg',
    #      'dupa.jpg'])


if getattr(sys, "frozen", False):
    cli()
else:
    # tests are run only if app is not frozen
    test()
    pass
