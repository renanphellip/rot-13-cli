from rot_cli.core import decrypt


def test_decrypt_rqhneqb_return_eduardo():
    # Arrange
    cipher = 'rqhneqb'
    rot = 13
    expected_text = 'eduardo'
    # Act
    result = decrypt(cipher, rot)
    # Assert
    assert result == expected_text


def test_decrypt_eduardo_return_rqhneqb():
    # Arrange
    cipher = 'Eduardo'
    rot = 13
    expected_text = 'rqhneqb'
    # Act
    result = decrypt(cipher, rot)
    # Assert
    assert result == expected_text


def test_decrypt_return_lowercase():
    # Arrange
    cipher = 'A'
    rot = 13
    # Act
    result = decrypt(cipher, rot)
    # Assert
    assert result.islower()


def test_decrypt_preserve_spaces():
    # Arrange
    cipher = 'r e'
    rot = 13
    expected_result = ' '
    # Act
    result = decrypt(cipher, rot)
    # Assert
    assert result[1] == expected_result


def test_decrypt_non_ascii_char_return_blank():
    # Arrange
    cipher = 'קום'
    rot = 13
    expected_result = ''
    # Act
    result = decrypt(cipher, rot)
    # Assert
    assert result == expected_result
