import pytest
import string
import src.ceaser_cipher as ceaser_cipher

@pytest.fixture
def uppercase():
    return string.ascii_uppercase


@pytest.fixture
def lowercase():
    return string.ascii_lowercase


@pytest.fixture
def bothcase():
    return string.ascii_letters


def test_uppercase_encryption(uppercase):
    """will test the uppercase encryption function without given the key"""
    assert ceaser_cipher.encrypt(uppercase) == uppercase[3:]+uppercase[:3]


def test_lowercase_encryption(lowercase):
    """will test the lowercase encryption function without given the key"""
    assert ceaser_cipher.encrypt(lowercase) == lowercase[3:]+lowercase[:3]


def test_uppercase_decryption(uppercase):
    """will test the uppercase decryption function without given the key"""
    assert ceaser_cipher.decrypt(uppercase[3:]+uppercase[:3]) == uppercase


def test_lowercase_decryption(lowercase):
    """will test the lowercase encryption function without given the key"""
    assert ceaser_cipher.decrypt(lowercase[3:]+lowercase[:3]) == lowercase

