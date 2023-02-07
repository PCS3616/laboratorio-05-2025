from pathlib import Path
import subprocess
import re
import tempfile

submission_path = Path("./submission")

def limpa(string):
    res=string.split(" ")
    res=list(filter(None, res))
    return int(res[1]+res[2],16)

def run_mvn(input_text):
    # I hate the current MVN
    # A good class solve this, but now are a really mess code

    p = subprocess.run(
        [
            "python", 
            "-m", 
            "MVN.mvnMonitor"
        ],
        input=input_text,
        capture_output=True, 
        text=True,
    )
    return p.stdout

def test_1_1():
    filecode = submission_path / "triangulos.mvn"
    assert filecode.exists(), f"A submissão não contém o arquivo '{filecode.name}'"

    input_file = tempfile.NamedTemporaryFile(mode='w')
    input_file.writelines([
        "0010	0001\n",
        "0012	0002\n",
        "0014	0003\n",
        ";0016	0000\n",
    ])
    input_file.flush()

    output_file = tempfile.NamedTemporaryFile(mode='r')

    inputs = [
        f"p {filecode.as_posix()}",
        "",
        f"p {input_file.name}",
        "",
        "r",
        "0",
        "n",
        "",
        f"m 0016 0017 {output_file.name}",
        "",
        "x",
        "",
    ]

    out = run_mvn('\n'.join(inputs))

    mvn_output = limpa(output_file.read())

    assert mvn_output == 0, \
            f"Seu código não está correto"

def test_1_2():
    filecode = submission_path / "triangulos.mvn"
    assert filecode.exists(), f"A submissão não contém o arquivo '{filecode.name}'"

    input_file = tempfile.NamedTemporaryFile(mode='w')
    input_file.writelines([
        "0010	0003\n",
        "0012	0004\n",
        "0014	0005\n",
        ";0016	0001\n",
    ])
    input_file.flush()

    output_file = tempfile.NamedTemporaryFile(mode='r')

    inputs = [
        f"p {filecode.as_posix()}",
        "",
        f"p {input_file.name}",
        "",
        "r",
        "0",
        "n",
        "",
        f"m 0016 0017 {output_file.name}",
        "",
        "x",
        "",
    ]

    out = run_mvn('\n'.join(inputs))

    mvn_output = limpa(output_file.read())

    assert mvn_output == 1, \
            f"Seu código não está correto"

def test_1_3():
    filecode = submission_path / "triangulos.mvn"
    assert filecode.exists(), f"A submissão não contém o arquivo '{filecode.name}'"

    input_file = tempfile.NamedTemporaryFile(mode='w')
    input_file.writelines([
        "0010	0003\n",
        "0012	0004\n",
        "0014	0004\n",
        ";0016	0002\n",
    ])
    input_file.flush()

    output_file = tempfile.NamedTemporaryFile(mode='r')

    inputs = [
        f"p {filecode.as_posix()}",
        "",
        f"p {input_file.name}",
        "",
        "r",
        "0",
        "n",
        "",
        f"m 0016 0017 {output_file.name}",
        "",
        "x",
        "",
    ]

    out = run_mvn('\n'.join(inputs))

    mvn_output = limpa(output_file.read())

    assert mvn_output == 2, \
            f"Seu código não está correto"

def test_1_4():
    filecode = submission_path / "triangulos.mvn"
    assert filecode.exists(), f"A submissão não contém o arquivo '{filecode.name}'"

    input_file = tempfile.NamedTemporaryFile(mode='w')
    input_file.writelines([
        "0010	0003\n",
        "0012	0004\n",
        "0014	0006\n",
        ";0016	0003\n",
    ])
    input_file.flush()

    output_file = tempfile.NamedTemporaryFile(mode='r')

    inputs = [
        f"p {filecode.as_posix()}",
        "",
        f"p {input_file.name}",
        "",
        "r",
        "0",
        "n",
        "",
        f"m 0016 0017 {output_file.name}",
        "",
        "x",
        "",
    ]

    out = run_mvn('\n'.join(inputs))

    mvn_output = limpa(output_file.read())

    assert mvn_output == 3, \
            f"Seu código não está correto"
