def processit(search_term):

    '''
    Cleanup search terms entered by user, and strip away unnecessary url parts to get the domain name.
    '''

    # Initialize the variables so that we don't get an exception if the search_term is not a domain name - i.e. an actual word.
    ext_marker = ""
    before_ext = ""

    # Code to handle substring after the domain name.
    # Clear out the domain extension and characters after it.
    if search_term.find(".com") > -1:
        ext_marker = search_term.find(".com")
        before_ext = search_term[:ext_marker]
    elif search_term.find(".co") > -1:
        ext_marker = search_term.find(".co")
        before_ext = search_term[:ext_marker]
    elif search_term.find(".net") > -1:
        ext_marker = search_term.find(".net")
        before_ext = search_term[:ext_marker]
    elif search_term.find(".org") > -1:
        ext_marker = search_term.find(".org")
        before_ext = search_term[:ext_marker]
    elif search_term.find(".us") > -1:
        ext_marker = search_term.find(".us")
        before_ext = search_term[:ext_marker]
    elif search_term.find(".io") > -1:
        ext_marker = search_term.find(".io")
        before_ext = search_term[:ext_marker]
    else:
        before_ext = search_term

    # Code to handle substring before the domain name. NOTE: Possibilities left to appear before our domain name are "/", ".", or None.
    if before_ext.find(".") > -1 or before_ext.find("/") > -1:

        try:
            # If we find a period, it is the next marker
            # Get the last period
            last_marker = before_ext.rindex(".")

            # Delete the period and everyting before it
            strip_search = before_ext[last_marker + 1 :]

        except:
            # Since there is no period, the only possibilities left are a "/" or None
            # If we find a slash, it is the new marker
            # Get the last slash
            last_marker = before_ext.rindex("/")

            # Delete the slash and everyting before it
            strip_search = before_ext[last_marker + 1 :]

    else:
        # Take the search_term as is
        strip_search = before_ext

    return strip_search