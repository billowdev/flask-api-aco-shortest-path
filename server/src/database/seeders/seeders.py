from . import user_seeder
from . import building_seeder
from . import node_seeder_1
from . import node_G1_E1
from . import node_G1_A18
from . import old_bs

def run_seed():
	building_seeder.seed()
	user_seeder.seed()
	# old_bs.seed()
	# node_seeder_1.seed()
	# node_G1_E1.seed()
	# node_G1_A18.seed()
 