import axios from "axios";
import httpClient from "../utils/httpClient.util";
import { BuildingsResponse, NavigationModel } from '../models/navigation.model';

export const getNavigation = async (data: any): Promise<any> => {
	const bid_start = data.start
	const bid_goal = data.goal
	
	const body = {
		payload: {
			bid_start, bid_goal
		}
	}

	const response = await axios.post('http://localhost:5000/api/v1/buildings/navigate', body, {
		headers: {
			'Content-Type': 'application/json',
		},
		method: 'POST'
	})

	return response.data;

};

export const getNode = async (): Promise<BuildingsResponse> => {
	const response = await axios.get(
	  'http://localhost:3000/api/navigation'
	);
	return response.data;
  };