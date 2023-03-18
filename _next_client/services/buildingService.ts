import { BuildingPayload } from "@/models/building.model";
import httpClient from "@/utils/httpClient.util";
import { ForkedTask } from "@reduxjs/toolkit";
import { parseCookies } from 'nookies';
import {
	ACCESS_TOKEN_KEY,
} from "@/utils/constant";
const cookies = parseCookies();
const token = cookies[ACCESS_TOKEN_KEY];

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


export const deleteBuilding = async (id?: string): Promise<void> => {
	
	console.log(token)
	await httpClient.delete(`/buildings/delete/${id}`,{
		headers: {
			'Authorization': 'Bearer ${token}'
		}
	});
};
