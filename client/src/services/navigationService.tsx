import axios from "axios";
import httpClient from "../utils/httpClient.util";
import { NavigationModel } from './../models/navigation.model';

export const getNavigation = async (data: any): Promise<any> => {
	const bid_start = data.start
	const bid_goal = data.goal
	const 	body =  {
		payload: {
			bid_start, bid_goal
		}
	}
	const response = await axios.post('http://localhost:5000/api/v1/buildings/navigate', body)
  .then(response => {
    return response
  })
  .catch(error => {
    console.error(error);
  });

	// const response = await httpClient.post(`/buildings/navigate`, {
	// 	payload: {
	// 	  bid_start,
	// 	  bid_goal,
	// 	},
	//   });
	  console.log('====================================');
	  console.log(response);
	  console.log('====================================');
	// const response = await httpClient.post(`/buildings/navigate`, {
	// 	payload: {
	// 		bid_start, bid_goal
	// 	}
	// })

	// baseURL: process.env.REACT_APP_BASE_URL_API
	return response;
	
};