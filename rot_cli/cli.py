from typing import Optional

import typer
from rot_cli.core import decrypt, encrypt

cli = typer.Typer(help='Rotate by N Places CLI', no_args_is_help=True)


@cli.command('encrypt')
def encrypt_input(
    text: str = typer.Option(
        default=None, help='Text to encrypt using rotation algorithm.'
    ),
    rotation: Optional[int] = typer.Option(
        default=13, help='Number of rotations to encrypt.'
    ),
) -> str:
    """Prints encrypted text."""
    cipher = encrypt(text, rotation)
    print(cipher)


@cli.command('decrypt')
def decrypt_input(
    cipher: str = typer.Option(
        default=None, help='Cipher to decrypt using rotation algorithm.'
    ),
    rotation: Optional[int] = typer.Option(
        default=13, help='Number of rotations to decrypt.'
    ),
) -> str:
    """Prints decrypted cipher."""
    text = decrypt(cipher, rotation)
    print(text)
