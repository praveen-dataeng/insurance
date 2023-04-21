import presparser.util as util
from presparser.main_parser import MedicalDocParser

class PatientDetailsParser(MedicalDocParser):
    """
    This class will be usedd to extract the information about the patient details
    """
    def __init__(self, text):
        super().__init__(text)

    def parse(self):
        return {
            'Patient_name': self.get_patient_name(),
            'Patient_Phone_number':self.get_patient_contact(),
            'Patient_Mediacal_issues': self.get_patient_medicalissues(),
            'Pateint_Vaccination_status': self.get_patient_vaccination()
        }
    
    def get_patient_name(self):           
        pattern = "Birth Date(.*\n*)(.*)"
        matches = util.re.findall(pattern, self.text)
        matches = matches[0][1]
        pattern = '(.*)((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[^\d])'
        date_match = util.re.findall(pattern, matches)

        if date_match:
            date = date_match[0][0].strip()
            name = date      
        return name
    
    def get_patient_contact(self):
        pattern = "(\(\d{3}\) \d{3}-\d{4}) Weight"
        phone_number = util.re.findall(pattern, self.text)
        return phone_number[0].strip()

    def get_patient_vaccination(self):
        pattern = "vaccination\?.*(yes|No|Yes|no)"
        vaccination_status = util.re.findall(pattern, self.text, util.re.DOTALL)
        return vaccination_status[0]

    def get_patient_medicalissues(self):
        pattern = "Medical Problems .*:(\n|.*?)\n(.*?\n)"
        medical_problems = util.re.findall(pattern, self.text, util.re.DOTALL)
        return medical_problems[0][1].strip()

