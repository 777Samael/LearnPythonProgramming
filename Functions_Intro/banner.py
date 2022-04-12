def banner_text(text=" ", screen_width: int = 80) -> None:
    """ Print a string centred, with ** either side.

    :param text: The string to print.
        An asterisk (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border at
        the left and right edges.
    :param screen_width: The overall width to print within
        (including the 4 spaces for the ** either side).
    :raises ValueError: if the supplied string is too long to fit.
    """
    # screen_width = 50
    if len(text) > screen_width - 4:
        # print("EEK!!")
        # print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")
        raise ValueError("String \"{0}\" is larger then specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


s_width = 66
banner_text("*", s_width)
banner_text("Always look on the bright side of life...", s_width)
banner_text("If life seems jolly rotten,", s_width)
banner_text("There's something you've forgotten!", s_width)
banner_text("And that's to laugh and smile and dance and sing,", 66)
banner_text(screen_width=66)
banner_text("When you're feeling in the dumps,", s_width)
banner_text("Don't be silly chumps,", s_width)
banner_text("Just purse your lips and whistle - that's the thing!", s_width)
banner_text("And... always look on the bright side of life...", s_width)
banner_text("*", s_width)
