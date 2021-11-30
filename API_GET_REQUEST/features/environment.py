def before_tag(context, tag):
    if 'tag1' in str(tag):
        print ('=Before Tag=' + str(tag))


def after_tag(context, tag):
    if 'tag1' in str(tag):
        print ('=After Tag=' + str(tag))

