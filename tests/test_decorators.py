from src.decorators import log


def test_log(capsys):
    @log()
    def add_numbers(a, b):
        return a + b
    add_numbers(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "add_numbers ok\n"

    @log()
    def add_numbers(a, b):
        return a + b

    add_numbers(1, "2")
    captured = capsys.readouterr()
    assert captured.out == "add_numbers error: TypeError. Inputs: (1, '2'), {}\n"


def test_log_success(tmp_path):
    log_file = tmp_path / "test_logs1.txt"

    @log(filename=str(log_file))
    def add_numbers(a, b):
        return a + b

    add_numbers(1, 2)
    log_lines = log_file.read_text(encoding="utf-8").splitlines()
    assert log_lines[-1] == "add_numbers ok"


def test_log_error(tmp_path):
    log_file = tmp_path / "test_logs2.txt"

    @log(filename=str(log_file))
    def add_numbers(a, b):
        return a + b

    add_numbers(1, "2")
    log_lines = log_file.read_text(encoding="utf-8").splitlines()
    assert log_lines[-1] == "add_numbers error: TypeError. Inputs: (1, '2'), {}"
