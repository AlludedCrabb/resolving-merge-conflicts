class Snake:
    """A dangerous and/or harmless serpent."""
    pass


class Cobra(Snake):
<<<<<<< HEAD
    """Definitely dangerous, yup. More dangerous than telling your mother you're not coming home for christmas"""
    
=======
    """Definitely dangerous, yup."""


    def bite(self, other):
        """Deliver a dose of venom."""
        return "Help. Oh no. I'm dying. Tell my mother, I should have come homefor christmas"

    
class BoaConstrictor(Snake):
    """This one gives really good hugs."""
    
    def squeeze(self, other):
 
<<<<<<< HEAD
       return 'before you die, that crick in your back finally pops' 
=======
        from bear import hug
        hug(self, other, kill=True)
>>>>>>> smiles/master

    
class BoatConstrictor(BoaConstrictor):
    """Loose snakes sink ships?"""

    def __init__(self):
        """Create a new BoatConstrictor"""
        super().__init__()
        self.size = "enormous"
