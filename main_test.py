import main

def test(capsys):
    main.calculate()
    captured = capsys.readouterr()
   # assert captured.out == "Total: 78.75\n"
    assert captured.out == "Total: 47.25\n"
