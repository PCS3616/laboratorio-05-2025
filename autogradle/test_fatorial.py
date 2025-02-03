from pathlib import Path
from tempfile import NamedTemporaryFile

from utils import executable, run_mvn, SUBMISSION_PATH, assert_file_exists

def limpa(string):
    res=string.split(" ")
    res=list(filter(None, res))
    return int(res[1]+res[2],16)

def fatorial(n: int):
  if n <= 1:
    return 1
  return n*fatorial(n-1)

def test_fat(n: int = 0):
    assert_file_exists(SUBMISSION_PATH / "fatorial.asm")
    filecode = executable(SUBMISSION_PATH / "fatorial")

    n_str = "{:04X}".format(n)
    input_file = NamedTemporaryFile(mode='w')
    input_file.writelines([
        f"0100	{n_str}\n"
    ])
    input_file.flush()

    output_file = NamedTemporaryFile(mode='r')

    inputs = [
        f"p {filecode.as_posix()}",
        "",
        f"p {input_file.name}",
        "",
        "r",
        "0",
        "n",
        "",
        f"m 0102 0103 {output_file.name}",
        "",
        "x",
        "",
    ]

    run_mvn('\n'.join(inputs))

    fat = limpa(output_file.read())

    assert fat == fatorial(n), \
      f"Seu código não está correto\nConfira seu envio."

def test_fat_1():
  test_fat(1)

def test_fat_4():
  test_fat(4)

def test_fat_5():
  test_fat(5)
