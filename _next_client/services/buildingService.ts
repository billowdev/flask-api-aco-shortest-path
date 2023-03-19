import { BuildingPayload } from "@/models/building.model";
import httpClient from "@/utils/httpClient.util";
import { ForkedTask } from "@reduxjs/toolkit";

import {
	ACCESS_TOKEN_KEY,
} from "@/utils/constant.util";



export const getBuildings = async (): Promise<BuildingPayload[]> => {
	const response = await httpClient.get(`/buildings/get/all`)
	return response.data.payload;
};

export const getBuilding = async (id: string) => {
	const response = await httpClient.get(`/buildings/${id}`);
	return response.data;
};

export const createBuilding = async (data: BuildingPayload): Promise<any> => {
	await httpClient.post(`/buildings`, data);
};

export const updateBuilding = async (data: any): Promise<void> => {
	await httpClient.put(`/buildings/update/${data.id}`, data);
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
