import abc

class MedicalDocParser(metaclass=abc.ABCMeta):
    """
    This is parent class for Prscription & Patient detail Parser
    """
    def __init__(self,extractedinformation):
        self.text = extractedinformation
    
    # we have used Abstract method to mondate this parse method in child classes
    @abc.abstractmethod
    def parse(self):
        pass