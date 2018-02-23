class Planet:

    def __init__(self,name,radius,gravity,system): 
    # called when new instance is created
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    # instance method
    def orbit(self):
        return f'{self.name} is orbiting in {self.system}'

    shape = 'round' # Class level attribute

    # class methods
    @classmethod
    def commons(cls):
        return(f'All planets are {cls.shape} because of gravity')


    # static method doesnot have access to class or self/self attributes
    # only to parameters passed
    # @ starting names are called decorator
    @staticmethod 
    def spin(speed = '2000 miles per hour'):
        return(f'The planet spins and spins at {speed}')

#hoth = Planet('Hoth',200000,5.5,'Hoth System')
#print(f'Name is: {hoth.name}')
#print(f'Radius is: {hoth.radius}')
#print(f'Gravity is: {hoth.gravity}')
#print(hoth.orbit())

#naboo = Planet('Naboo',300000,8,'Naboo System')
#print(f'Name is: {naboo.name}')
#print(f'Radius is: {naboo.radius}')
#print(f'Gravity is: {naboo.gravity}')

#print(Planet.shape)
#print(naboo.shape)
#print(Planet.commons())
#print(naboo.commons())

#print(Planet.spin('at a very high speed.'))
#print(naboo.spin('at a very high speed.'))
