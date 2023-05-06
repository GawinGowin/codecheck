from main import *
import pytest
import io

@pytest.mark.parametrize(('fileNo'), [1, 2,])
def test_case(capsys, monkeypatch, fileNo):
    inputs, outputs = load_data(fileNo)
    monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
    main()
    results, _ = capsys.readouterr()
    assert results == outputs + "\n"

def load_data(fileNo):
    inputFile = F"src/input/input{fileNo}.txt"
    outputFile = F"src/output/output{fileNo}.txt"
    with open(inputFile, "r") as f:
        inputs = f.read()
    with open(outputFile, "r") as f:
        outputs = f.read()
    return inputs, outputs