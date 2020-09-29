from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 
from typing import NamedTuple

class ProjectSpecifications(NamedTuple):
    """Specifies the details of a new project
    
    site_name: the name of the site where cranes were inspected
    section_name: the section of the site where cranes were inspected
    """
    site_name: str 
    section_name: str
    
class ClientSpecifications(NamedTuple):
    """Specifies the detals of the clinet for the project
    
    client: the name of the client for who's site and section cranes are inspected
    client_rep: the name of the clients representative for the project
    rep_pos: the position of the clinet representative
    """
    client: str
    client_rep: str
    rep_pos: str
    
class MiscellaneousDetails(NamedTuple):
    """Specifies some miscellaneous details regarding the cranes operating conditions
    
    external_env: is the crane situated in doors or outdoors
    corrosive_env: is the crane exposed to a corrosive environment
    heat_env: is the crane exposed to elevated temperatures
    major_rep: history of major repairs
    common_occ: are there common occurances of failures and/or repairs
    """
    external_env: str
    corrosive_env: str
    heat_env: str
    major_rep: str
    common_occ: str

class ProjectAdministration(models.Model):
    """This class defines the project by design.
    """
    def __init__(
            self,
            project_specifications: ProjectSpecifications,
            client_specifications: ClientSpecifications,
            miscellaneous_details: MiscellaneousDetails
    ):
        """
        :param cranes_specifications: Specifications of the crane.
        :param hoists_specifications: A list of the hoists present on the crane.
        :param platform_heights: The different platform heights.
        """
        self.project_specifications = project_specifications
        self.client_specifications = client_specifications
        self.miscellaneous_details = miscellaneous_details
