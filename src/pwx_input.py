### Created by Emanuele Oggiano
### Last Update by Emanuele Oggiano

### Modules
import os
from datetime import date

###--------------------------------------------------------------------------------###
### A pw.x input file can be divided in sections. Some sections are more
### important than others.
### The four main sections are: 1) CONTROL 2) SYSTEM 3) ELECTRONS 4) IONS
### Other sections can be added, yet this four must be included in every .in file
### TO BE COMPLETED...
###--------------------------------------------------------------------------------###
class ipwx:
    
    ##########
    ### Init constructor
    def __init__(self, filename, filedir):

        ### Check if the file extension is correct
        if not filename.endswith('.in'):
            raise ValueError('The file {} must have the .in extension!'.format(filename))
             
        ### Create the folder if it is not present
        if not os.path.exists(filedir):
            os.makedirs(filedir)

        self.filename = filename
        self.filedir = filedir

        ### Full path
        filepath = os.path.join(self.filedir, self.filename)

        ### Check if the file already exists. Raise an error in that case
        if os.path.exists(filepath):
            raise FileExistsError('The file {} already exists in this folder. Create a new one!'.format(self.filename))
        
        ### Write the date in which the file has been created
        with open(filepath, 'w') as file:
            file.write('! - {}'.format( date.today().strftime('%a %d %b %y') ))

        ### Dictionaries for the four main sections
        self.control_dict = { 'restart_mode': 'from_scratch' }
        self.system_dict = {}
        self.electrons_dict = {}
        self.ions_dict = {}
    ##########


    ##########
    ### &CONTROL section
    def set_control_param(self, parameters):

        ### Check if parameters is a dictionary
        if not isinstance(parameters, dict):
            raise TypeError("You must pass a dictionary")

        self.control_dict.update(parameters)

        __calculation = self.control_dict.get("calculation", "")

        if not __calculation:
            raise ValueError("Missing calculation parameter")

        if __calculation not in ["scf", "nscf", "bands" , "relax", "md", "vc-relax", "vc-md"]:
            raise ValueError("The {} calculation is not supported".format(__calculation))

        for key in ["prefix", "outdir", "pseudo_dir"]:
            if key not in self.control_dict:
                raise ValueError("Missing '{}' parameter".format(key))
        
        ### A dictionary is created in order to check if the convergence threshold is in the correct format
        conv_dict = {
                "etot_conv_thr": None,
                "forc_conv_thr": None
        }

        ### The loop is used to check if the format is correct
        for key in conv_dict:

            value = self.control_dict.get(key, None)
            
            if value is not None and not isinstance(value, float):
                raise ValueError("The value for the {} parameter must be in the format: 1e-n".format(key))
    ##########


    ##########
    ### &SYSTEM section
    def set_system_param(self, parameters):
        
        ### Check if parameters is a dictionary
        if not isinstance(parameters, dict):
            raise TypeError("You must pass a dictionary")

        self.system_dict.update(parameters)
        
        ### Setting up a dictionary to check if these values are integers
        keys_dict = {
                "ibrav": None,
                "nat": None,
                "ntyp": None,
                "ecutwfc": None,
                "ecutrho": None
        }
        
        ### Check if the values are integers or not
        for key in keys_dict:

            value = self.system_dict.get(key, None)
            
            if value is not None and not isinstance(value, int):
                raise ValueError("The {} parameter must be an integer".format(key))
    ##########


    ##########
    ### &ELECTRONS section
    def set_electrons_param(self):
        pass
    ##########


    ##########
    ### &IONS section
    def set_ions_param(self):
        pass
    ##########
