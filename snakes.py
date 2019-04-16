class Snake:
    """A dangerous and/or harmless serpent."""
    pass


class Cobra(Snake):
    """Definitely dangerous, yup. More dangerous than telling your mother you're not coming home for christmas"""
    
    def bite(self, other):
        """Deliver a dose of venom."""
        return "Help. Oh no. I'm dying. Tell my mother, I should have come homefor christmas"

    
class BoaConstrictor(Snake):
    """This one gives really good hugs."""
    
    def squeeze(self, other):
        """Give a hug."""
        pass

    
class BoatConstrictor(BoaConstrictor):
    """Loose snakes sink ships?"""
    pass
