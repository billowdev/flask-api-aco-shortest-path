export interface BuildingResponse {
	msg: string
	payload: BuildingPayload[]
  }
  
  export interface BuildingPayload {
	bid: string
	desc: string
	id: number
	is_node: boolean
	lat: string
	lng: string
	name: string
	image: string
  }
  