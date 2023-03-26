from . import user_seeder
from . import building_seeder
from . import dev_seed


def run_seed():
	dev_seed.seed()
	user_seeder.seed()
	# link_node_G1_E1.seed()
	# link_node_G1_A18.seed()
 