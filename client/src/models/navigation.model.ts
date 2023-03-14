import { BestPathArrayType, CoordinatesType, NavigationArrayType } from "../types/navigation.types"

export interface NavigationModel {
	best_path: BestPathArrayType
	coordinates: CoordinatesType
	distance: number
	from_start: string
	navigation: NavigationArrayType
	to_goal: string
}

