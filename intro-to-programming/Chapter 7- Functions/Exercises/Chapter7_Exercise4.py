def make_shirt(size='large', message='I love Python!'):
    """Summarization of the t-shirt being made:"""
    print("\nI'm going to make a " + size + " t-shirt.")
    print ('It will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')