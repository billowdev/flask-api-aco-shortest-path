import { BuildingPayload } from "@/models/building.model";
import httpClient from "@/utils/httpClient.util";
import { ForkedTask } from "@reduxjs/toolkit";

export const getBuildings = async (): Promise<BuildingPayload[]> => {
	const response = await httpClient.get(`/buildings/get/all`)
	return response.data;
};

export const getBuilding = async (id: string) => {
	const response = await httpClient.get(`/buildings/${id}`);
	return response.data;
};

export const createBuilding = async (data: BuildingPayload): Promise<any> => {
	await httpClient.post(`/buildings`, data);
};

export const updateBuilding = async (data: any): Promise<void> => {
	await httpClient.put(`/buildings/${data.id}`, data);
};


export const deleteBuilding = async (id?: string): Promise<void> => {
	await httpClient.delete(`/buildings/${id}`);
};
