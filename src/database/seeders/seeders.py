from . import user_seeder
from . import building_seeder
from . import link_node_G1_E1
from . import link_node_G1_A18

def run_seed():
	building_seeder.seed()
	user_seeder.seed()
	# link_node_G1_E1.seed()
	link_node_G1_A18.seed()
 