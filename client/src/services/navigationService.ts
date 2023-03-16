import axios from "axios";
import httpClient from "../utils/httpClient.util";
import { NavigationModel } from '../models/navigation.model';
import { AxisosHeader } from '../utils/httpClient.util';

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
		.then(response => {
			return response.data
		})
		.catch(error => {
			console.error(error);
		});

	
	return response;

};