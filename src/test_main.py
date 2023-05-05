from main import *
import pytest
import io

@pytest.mark.parametrize(('fileNo'), [1, 2, 3])
def test_case(capsys, monkeypatch, fileNo):
    inputs, outputs = loadData(fileNo)
    monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
    main()
    results, _ = capsys.readouterr()
    assert results == outputs + "\n"

def loadData(fileNo):
    inputFile = F"src/input/input{fileNo}.txt"
    outputFile = F"src/output/output{fileNo}.txt"
    with open(inputFile, "r") as f:
        inputs = f.read()
    with open(outputFile, "r") as f:
        outputs = f.read()
    return inputs, outputs