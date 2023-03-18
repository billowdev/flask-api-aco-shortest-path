import axios from "axios";
import httpClient from "../utils/httpClient.util";
import { NodeResponse } from '../models/navigation.model';
import { BuildingResponse } from "@/models/buildings.model";
import {  ENDPOINT} from '@/utils/constant';

export const getNavigation = async (data: any): Promise<any> => {
	const start_state = data.start
	const goal_state = data.goal

	const body = {
		payload: {
			start_state, goal_state
		}
	}

	const response = await axios.post(`${ENDPOINT}/buildings/navigate/geo`, body, {
		headers: {
			'Content-Type': 'application/json',
		},
		method: 'POST'
	})

	return response.data;

};

export const getBuildings = async (): Promise<BuildingResponse> => {
	// const response = await axios.get(
	// 	'http://localhost:5000/api/v1/buildings/get'
	//   );
	const { data: response } = await httpClient.get(`/buildings/get/all/node`, {
		baseURL: process.env.NEXT_PUBLIC_BASE_URL_API,
	});

	return response;
}

export const getNode = async (): Promise<NodeResponse> => {
	const { data: response } = await httpClient.get(`/buildings/node`, {
		baseURL: process.env.NEXT_PUBLIC_BASE_URL_API,
	});
	// const response = await axios.get(
	// 	'http://localhost:3000/api/navigation'
	// );
	return response;
};