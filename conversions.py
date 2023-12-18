

def convert_wei_to_lrc(wei_amount: int):
    """
    Convert LRC amount from wei to LRC.
    1 LRC = 10^18 wei

    :param wei_amount: The amount in wei.

    :return float: The amount in LRC.
    """
    return wei_amount / 10**18
