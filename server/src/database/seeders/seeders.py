from . import user_seeder
from . import building_seeder

def run_seed():
	user_seeder.seed()
	building_seeder.seed()