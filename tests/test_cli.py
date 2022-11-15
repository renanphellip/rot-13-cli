import sys
from io import StringIO

from rot_cli.cli import decrypt_input, encrypt_input


def test_encrypt_input_return_printed_cipher():
    # Arrange
    captured_output = StringIO()
    sys.stdout = captured_output
    text = 'eduardo'
    rot = 13
    expected_cipher = 'rqhneqb'

    # Act
    cipher = encrypt_input(text, rot)
    print(cipher)

    sys.stdout = sys.__stdout__

    # Assert
    assert expected_cipher in captured_output.getvalue()


def test_decrypt_input_return_printed_text():
    # Arrange
    captured_output = StringIO()
    sys.stdout = captured_output
    cipher = 'rqhneqb'
    rot = 13
    expected_text = 'eduardo'

    # Act
    text = decrypt_input(cipher, rot)
    print(text)

    sys.stdout = sys.__stdout__

    # Assert
    assert expected_text in captured_output.getvalue()
