import axios from 'axios'
export const AxisosHeader = {
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer yourAuthTokenHere'
  }
};
const httpClient = axios.create({
  baseURL: process.env.REACT_APP_BASE_URL_API
})

export default httpClient
