import presparser.util as util
from presparser.main_parser import MedicalDocParser

class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        super().__init__(text)

    def parse(self):
        return {
            'pateint_name': self.get_field('pateint_name'),
            'patient_address': self.get_field('patient_address'),
            'medicines': self.get_field('medicines'),
            'instructions': self.get_field('instructions'),
            'refill_instruction': self.get_field('refill_instruction')
        }
    
    def get_field(self, field_name):
        # pattern = ''
        # flag = None

        pattern_dict = {
            'pateint_name' : {'pattern': 'Name:(.*)Date:', 'flag': 0},
            'patient_address' : {'pattern': 'Address:(.*)\n', 'flag': 0},
            'medicines' : {'pattern': 'Address:[^\n]*(.*)Directions', 'flag': util.re.DOTALL},
            'instructions' : {'pattern': 'Directions:(.*)\nRefill', 'flag': util.re.DOTALL},
            'refill_instruction' : {'pattern': 'Refill:(.*)times', 'flag': 0},
        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = util.re.findall(pattern_object['pattern'], self.text, flags=pattern_object['flag'])
            if len(matches) > 0:
                return matches[0].strip()  

