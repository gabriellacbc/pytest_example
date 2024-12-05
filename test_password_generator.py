import pytest
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from password_generator import generate_password  # Substitua "password_generator" pelo nome do arquivo onde está sua função a ser testada.

def test_generate_password_length():
    # Testa se a senha gerada tem o comprimento correto
    length = 16
    password = generate_password(length)
    assert len(password) == length, f"A senha deve ter {length} caracteres."

def test_generate_password_default_length():
    # Testa se a senha padrão tem 12 caracteres
    password = generate_password()
    assert len(password) == 12, "A senha padrão deve ter 12 caracteres."

def test_generate_password_character_types():
    # Testa se a senha contém pelo menos um caractere de cada tipo
    password = generate_password(20)
    assert any(char in ascii_lowercase for char in password), "A senha deve conter pelo menos uma letra minúscula."
    assert any(char in ascii_uppercase for char in password), "A senha deve conter pelo menos uma letra maiúscula."
    assert any(char in digits for char in password), "A senha deve conter pelo menos um dígito."
    assert any(char in punctuation for char in password), "A senha deve conter pelo menos um caractere especial."

def test_generate_password_minimum_length():
    # Testa se uma exceção é levantada para senhas menores que 6 caracteres
    with pytest.raises(ValueError, match="Password length should be at least 6 characters."):
        generate_password(5)

