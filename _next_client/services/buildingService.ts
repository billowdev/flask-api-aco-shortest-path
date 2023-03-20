import { BuildingPayload } from "@/models/building.model";
import httpClient from "@/utils/httpClient.util";


export const getBuildings = async (): Promise<BuildingPayload[]> => {
	const response = await httpClient.get(`/buildings/get/all`)
	return response.data.payload;
};

export const getBuilding = async (id: string) => {
	const {data: response} = await httpClient.get(`/buildings/get/${id}`);
	return response.payload;
};

export const createBuilding = async (data: BuildingPayload): Promise<any> => {
	await httpClient.post(`/buildings`, data);
};

export const updateBuilding = async (data: any): Promise<void> => {
	await httpClient.patch(`/buildings/${data.id}`, data, {
		baseURL: process.env.NEXT_PUBLIC_BASE_URL_LOCAL_API,
	});
};


export const deleteBuilding = async (id: string): Promise<void> => {
	const response = await httpClient.delete(`/buildings/${id}`,{
		headers: {
			'Authorization': 'Bearer ${accessToken}',
		},
		baseURL: process.env.NEXT_PUBLIC_BASE_URL_LOCAL_API,
	});
	// console.log("==============")
	// console.log(response)
	// console.log("==============")
};
