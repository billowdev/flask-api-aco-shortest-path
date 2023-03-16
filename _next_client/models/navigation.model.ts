
export interface NavigationModel {
	best_path: BestPathArrayType
	coordinates: CoordinatesType
	distance: number
	from_start: string
	navigation: NavigationArrayType
	to_goal: string
}


export interface NavigationType {
	message: string
	payload: NavigationPayload
}
export type CoordinatesType = number[][]
export type BestPathArrayType = string[]

export interface NavigationPayload {
	best_path: BestPathArrayType
	coordinates: CoordinatesType
	distance: number
	from_start: string
	navigation: NavigationArrayType
	to_goal: string
}

export interface NavigationPayloadType {
	bid: string
	is_node: boolean
	lat: string
	lng: string
}

export type NavigationArrayType = NavigationPayloadType[]