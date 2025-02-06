from pathlib import Path
import re
import tempfile

from utils import executable, run_mvn, SUBMISSION_PATH, assert_file_exists


def test_1():
    assert_file_exists(SUBMISSION_PATH / "quadrados-perfeitos.asm")
    filecode = executable(SUBMISSION_PATH / "quadrados-perfeitos")

    output_file = tempfile.NamedTemporaryFile(mode='r')

    inputs = [
        f"p {filecode.as_posix()}",
        "",
        "r",
        "0",
        "n",
        "",
        f"m 0100 017f {output_file.name}",
        "",
        "x",
    ]

    out = run_mvn('\n'.join(inputs))

    mvn_output = output_file.read()
    expected_output = """
0100:  00  00  00  01  00  04  00  09  00  10  00  19  00  24  00  31
0110:  00  40  00  51  00  64  00  79  00  90  00  a9  00  c4  00  e1
0120:  01  00  01  21  01  44  01  69  01  90  01  b9  01  e4  02  11
0130:  02  40  02  71  02  a4  02  d9  03  10  03  49  03  84  03  c1
0140:  04  00  04  41  04  84  04  c9  05  10  05  59  05  a4  05  f1
0150:  06  40  06  91  06  e4  07  39  07  90  07  e9  08  44  08  a1
0160:  09  00  09  61  09  c4  0a  29  0a  90  0a  f9  0b  64  0b  d1
0170:  0c  40  0c  b1  0d  24  0d  99  0e  10  0e  89  0f  04  0f  81
Final do dump.""".strip()

    if mvn_output != expected_output:
        olines = mvn_output.splitlines()
        elines = expected_output.splitlines()
        for oline, eline in zip(olines, elines):
            assert oline.strip() == eline.strip(), \
                f"Seu código não está correto"


def test_2():
    assert_file_exists(SUBMISSION_PATH / "io.asm")
    filecode = executable(SUBMISSION_PATH / "io")

    newcodefile = tempfile.NamedTemporaryFile(mode='w')

    with open(filecode) as f:
        new = re.sub("(e|E)100", "e300", f.read())
        newcodefile.write(new)
        newcodefile.flush()

    outputfile = tempfile.NamedTemporaryFile(mode='r')

    inputs = [
        f"p {newcodefile.name}",
        "s",
        "a",
        "3",
        "00",
        outputfile.name,
        "e",
        "r",
        "",
        "n",
        "07  54",
        "x",
    ]

    run_mvn('\n'.join(inputs))

    mvn_output = outputfile.read().replace('\n', '')
    assert mvn_output == "61", \
        f"Seu código não está correto\nConfira seu envio."
