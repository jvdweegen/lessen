"""
convert.py
Convert data from one CSV format to another CSV format or JSON.
FIXME
"""


from argparse import ArgumentParser


def read_csv(path):
    """
    Read CSV formatted data from `path` and return a list of lines
    FIXME
    """
    return [
        "Sheldon;22;Utrecht",
        "Shelly;42;Amersfoort"
    ]


def write_out(path, data, formatting="csv"):
    """
    Write every line in `data` to `path`.`formatting`
    FIXME
    """
    print(f"output.{formatting}")
    for line in data:
        print(line)


def convert():
    """
    Convert data from one CSV format to another CSV format or JSON.
    FIXME
    """
    parser = ArgumentParser()
    args = parser.parse_args()

    old_delim = parser.add_argument('-cf', 
                                    '--currentformat', 
                                    help='Current format to convert', 
                                    type=lambda lineobtain:(";", ",", "|", ":", lineobtain),
                                    )
    new_delim = parser.add_argument("-nf", 
                                    "--newformat",
                                    help="Change old format to new format",
                                    type=lambda linechange:(";", ",", "|", ":", linechange),
                                    )

    old = read_csv("")

    new = []

    for line in old:
        parts = line.split(old_delim)
        new.append(new_delim.join(parts))

    write_out("", new)


if __name__ == "__main__":
    convert()
