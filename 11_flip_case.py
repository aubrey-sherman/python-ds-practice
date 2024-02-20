def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    phrase = list(phrase)
    for i, char in enumerate(phrase):
        if char == to_swap.lower():
            phrase[i] = to_swap.upper()
        elif char == to_swap.upper():
            phrase[i] = to_swap.lower()

    return ''.join(phrase)
