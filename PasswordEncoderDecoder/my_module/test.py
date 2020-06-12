import pytest
import guidelines
import password
import encode
import decode

def test_checks_input():
    bad_input = "no"
    good_input = "encode"
    assert (False, False, False) == guidelines.checks_input(bad_input)
    assert (True, True, False) == guidelines.checks_input(good_input)

def test_password_check():
    bad_password = "heeelloop"
    spaces_password = "honp i noe"
    short_password = "hello"
    good_password = "12tholp31"
    
    assert False == password.password_check(bad_password)
    assert False == password.password_check(spaces_password)
    assert False == password.password_check(short_password)
    assert True == password.password_check(good_password)

def test_password_strength():
    weak_password = "Nretdasjt"
    medium_password = "123Dnat5de"
    strong_password = "34dasTe1!def"
    
    assert "Weak" == password.password_strength(weak_password)
    assert "Medium" == password.password_strength(medium_password)
    assert "Strong" == password.password_strength(strong_password)

def test_encode_decode():
    test_string = "encode"
    encoded_string = encode.single_encode(test_string)
    
    assert test_string == decode.single_decode(encoded_string)
    
def test_variable_encode_decode():
    test_string = "!encodeThis1234"
    encoded_string = encode.variable_encode(test_string)
    
    assert test_string == decode.variable_decode(encoded_string)
    
def test_custom_variable_encode_decode():
    test_string = "!jdanEncode?3"
    encoded_string = encode.custom_encode(test_string, 50, 3, 2)
    
    assert test_string == decode.custom_decode(encoded_string, 50, 3, 2)
    
def test_random_encode():
    test_string = "123%adkmDe"
    encoded_string = encode.random_encode(test_string)
    
    assert test_string != encoded_string