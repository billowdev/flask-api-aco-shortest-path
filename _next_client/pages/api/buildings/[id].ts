import { NextApiRequest, NextApiResponse } from 'next';
import { setCookie } from '@/utils/cookies.util';
import httpClient from '@/utils/httpClient.util';
import {
  HTTP_METHOD_POST,
  HTTP_METHOD_DELETE,
  HTTP_METHOD_PATCH,
  HTTP_METHOD_GET,
  ACCESS_TOKEN_KEY,
} from "@/utils/constant.util";

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === HTTP_METHOD_DELETE) {
    return deleteBuilding(req, res);
  } else  if (req.method === HTTP_METHOD_PATCH) {
    return updateBuilding(req, res);
  }else {
    return res
      .status(405)
      .end(`Error: HTTP ${req.method} is not supported for ${req.url}`);
  }
}



async function deleteBuilding(req: NextApiRequest, res: NextApiResponse<any>) {
  try {

    const accessToken = req.cookies[ACCESS_TOKEN_KEY];
    if (!accessToken) {
      return res.status(401).json({ message: 'Unauthorized' });
    }
    if (req.query) {
      const { data } = await httpClient.delete(`/buildings/delete/${req.query['id']}`, {
        headers: {
          'Authorization': `Bearer ${accessToken}`,
        },
      });
      if(data){
        return res.status(200).json(data);
      }else{
        return res.status(400).json(data);
      }
    } else {
      return res.status(400).json({ message: 'id required' });
    }

  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: 'Internal Server Error' });
  }
}


async function updateBuilding(req: NextApiRequest, res: NextApiResponse<any>) {
  try {
    const accessToken = req.cookies[ACCESS_TOKEN_KEY];
    if (!accessToken) {
      return res.status(401).json({ message: 'Unauthorized' });
    }

    const updateBody = req.body;
    if (req.query) {
      const { data } = await httpClient.patch(`/buildings/update/${req.query['id']}`, updateBody, {
        headers: {
          'Authorization': `Bearer ${accessToken}`,
        },
      });

      if(data){
        return res.status(200).json(data);
      }else{
        return res.status(400).json(data);
      }
    } else {
      return res.status(400).json({ message: 'id required' });
    }

  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: 'Internal Server Error' });
  }
}