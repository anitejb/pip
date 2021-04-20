import os

from src.anitejb import safeopen

def test_safeopen(tmpdir):
    testfile = str(tmpdir.join("testfile.txt"))
    testfile_body = "testfile"
    newfile = str(tmpdir.join("testfile_(1).txt"))
    newfile_body = "newfile"

    with open(testfile, "w") as f:
        f.write(testfile_body)

    with safeopen(testfile, "w") as f:
        f.write(newfile_body)

    assert os.path.exists(testfile)
    with open(testfile) as f:
        assert f.read() == testfile_body
    assert os.path.exists(newfile)
    with open(newfile) as f:
        assert f.read() == newfile_body
