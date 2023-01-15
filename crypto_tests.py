from crypto_functions import *

assert encrypt_transposition("CSW EIGHT IS AMAZING!", 4) == "CET Z!SI AI WGIMN  HSAG "
assert encrypt_transposition("I WILL ACE THE FINAL PROJECT!", 8) == "ICIJ ENEW ACITLTLH !LEP   R AFO "
assert encrypt_transposition("YOU GOT THIS! YOU CAN DO IT!", 5) == "YOIONIOTSU TU ! D! T CO GHYA  "

assert decrypt_transposition("CET Z!SI AI WGIMN  HSAG ", 4) == "CSW EIGHT IS AMAZING!"
assert decrypt_transposition("ICIJ ENEW ACITLTLH !LEP   R AFO ", 8) == "I WILL ACE THE FINAL PROJECT!"
assert decrypt_transposition("YOIONIOTSU TU ! D! T CO GHYA  ", 5) == "YOU GOT THIS! YOU CAN DO IT!"
assert decrypt_transposition("EEEXLNCLT", 3) == "EXCELLENT"

assert extend_string("CS8", 10) == "CS8CS8CS8C"
assert extend_string("CMPSC8", 18) == "CMPSC8CMPSC8CMPSC8"
assert extend_string("A very long sentence", 0) == ""
assert extend_string("Hello World!", 7) == "Hello W"

assert encrypt_vigenere("", "NOWORDS") == ""
assert encrypt_vigenere("CallMeIshmaelThe3rd", "MOBYDICK") == "OomJPmKCtAbCo1jofFe"
assert encrypt_vigenere("CryptographyIsSoCool", "Bitcoin") == "D9r1h63sSiTmqfT6v0c3"
assert encrypt_vigenere("WE HOPE YOU LIKE THE PROJECT", "CSW8") == -1

assert decrypt_vigenere("", "NOWORDS") == ""
assert decrypt_vigenere("OomJPmKCtAbCo1jofFe", "MOBYDICK") == "CallMeIshmaelThe3rd"
assert decrypt_vigenere("D9r1h63sSiTmqfT6v0c3", "Bitcoin") == "CryptographyIsSoCool"
assert decrypt_vigenere("K3mXWaUeG", "CS8") == "ILOVECSW8"
