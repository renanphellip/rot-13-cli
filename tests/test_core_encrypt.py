from rot_cli.core import encrypt


def test_encrypt_eduardo_return_rqhneqb():
    # Arrange
    text = 'Eduardo'
    rot = 13
    expected_cipher = 'rqhneqb'
    # Act
    result = encrypt(text, rot)
    # Assert
    assert result == expected_cipher


def test_encrypt_rqhneqb_return_eduardo():
    # Arrange
    text = 'rqhneqb'
    rot = 13
    expected_cipher = 'eduardo'
    # Act
    result = encrypt(text, rot)
    # Assert
    assert result == expected_cipher


def test_encrypt_return_lowercase():
    # Arrange
    text = 'A'
    rot = 13
    # Act
    result = encrypt(text, rot)
    # Assert
    assert result.islower()


def test_encrypt_preserve_spaces():
    # Arrange
    text = 'r e'
    rot = 13
    expected_result = ' '
    # Act
    result = encrypt(text, rot)
    # Assert
    assert result[1] == expected_result


def test_encrypt_non_ascii_char_return_blank():
    # Arrange
    text = 'קום'
    rot = 13
    expected_result = ''
    # Act
    result = encrypt(text, rot)
    # Assert
    assert result == expected_result
