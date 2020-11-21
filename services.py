import base64


def encode(string_to_encode):
    '''
    encode method can be used to encode any string.
    :param string_to_encode:
    :return:
    '''
    return base64.urlsafe_b64encode("".join(string_to_encode).encode(encoding="utf-8"))


def decode(string_to_decode):
    """
    decode method can be used to decode encoded string.
    :param string_to_decode:
    :return:
    """
    cipher = base64.urlsafe_b64decode(string_to_decode)
    cipher = str(cipher, 'utf-8')
    return "".join(cipher)
