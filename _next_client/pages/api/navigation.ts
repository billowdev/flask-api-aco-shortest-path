import { NextApiRequest, NextApiResponse } from 'next';
import httpClient from "@/utils/httpClient.util";
type ApiResponse = {
	message: string;
	payload: string[][];
};

export default async function handler(
	req: NextApiRequest,
	res: NextApiResponse<ApiResponse>
) {
	try {
		const { data: response } = await httpClient.get(`/buildings/node`, {
			baseURL: process.env.NEXT_PUBLIC_BASE_URL_API,
		});

		res.status(200).json(response);
	} catch (error) {
		res.status(400).json({ message: 'Error retrieving buildings', payload: [] });
	}
}
