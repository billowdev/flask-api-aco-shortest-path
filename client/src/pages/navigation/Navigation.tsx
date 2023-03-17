import { LatLng, LatLngExpression } from 'leaflet';
import { useEffect, useState } from 'react';
import { getNavigation, navigationLoadingSelector, navigationSelector } from "../../store/slices/navigationSlice";
import { useSelector } from "react-redux";
import { MapContainer, TileLayer, Marker, Polyline, Popup, } from 'react-leaflet';
import { useAppDispatch } from '../../store/store';


// This function calculates the distance between two points using the Haversine formula
const calculateDistance = (lat1: number, lon1: number, lat2: number, lon2: number) => {
	const R = 6371; // Radius of the earth in km
	const dLat = (lat2 - lat1) * Math.PI / 180; // deg2rad below
	const dLon = (lon2 - lon1) * Math.PI / 180;
	const a =
		Math.sin(dLat / 2) * Math.sin(dLat / 2) +
		Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
		Math.sin(dLon / 2) * Math.sin(dLon / 2);
	const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
	const d = R * c; // Distance in km
	return d;
}



type NavigationArrayType = {
	bid: string;
	lat: string;
	lng: string;
	is_node: boolean,
}[];
// const CustomNavigationMap = ({ currentPosition }: { currentPosition: number[] }) => {
const NavigationMap = () => {
	const dispatch: any = useAppDispatch();

	const [isLoading, setIsLoading] = useState<boolean>(false);
	const navigationLoading = useSelector(navigationLoadingSelector);
	const navigationList = useSelector(navigationSelector);
	const [coordinates, setCoordinates] = useState([
		[
			17.19256404202556,
			104.09360793646384
		],
		[
			17.192329942043273,
			104.09348628794305
		],

	])

	const [navigation, setNavigation] = useState<NavigationArrayType>([

		{
			"bid": "G1",
			"is_node": true,
			"lat": "17.192564042025560",
			"lng": "104.093607936463840"
		},
		{
			"bid": "G1L01",
			"is_node": false,
			"lat": "17.192329942043273",
			"lng": "104.093486287943050"
		},
	])


	useEffect(() => {
		const fetchNavigation = async () => {
			setIsLoading(true)
			await dispatch(getNavigation({ start: "G1", goal: "C1" }))
		}

		fetchNavigation()
	}, [])

	useEffect(() => {
		setCoordinates(navigationList.coordinates)
		setNavigation(navigationList.navigation)
	}, [navigationList.coordinates, navigationList.navigation])
	const [currentPosition, setCurrentPosition] = useState<[number, number]>([17.189578289590823, 104.090411954494540]); // initialize with dummy values

	useEffect(() => {

		let counter = 0;
		const intervalId = setInterval(() => {
			setCurrentPosition([coordinates[counter][0], coordinates[counter][1]]);
			counter = (counter + 1) % coordinates.length;
		}, 1000);

		return () => clearInterval(intervalId);
	}, [coordinates]);



	// This function finds the closest point in the navigation array to the current position
	const findClosestPoint = (lat: number, lng: number) => {
		let closestPoint = navigation[0];

		let closestDistance = calculateDistance(lat, lng, parseFloat(closestPoint.lat), parseFloat(closestPoint.lng));
		for (let i = 1; i < navigation.length; i++) {
			const distance = calculateDistance(lat, lng, parseFloat(navigation[i].lat), parseFloat(navigation[i].lng));
			if (distance < closestDistance) {
				closestPoint = navigation[i];
				closestDistance = distance;
			}
		}
		return closestPoint;
	}


	// This is the starting point (it can be replaced with the current position from GPS)
	const from_start = currentPosition.length ? [currentPosition[0], currentPosition[1]] : [0, 0];

	// This is the goal (it can be any point in the navigation array)
	// const goal = [navigation[navigation.length - 1].lat, navigation[navigation.length - 1].lng];
	// const goal = [navigation[navigation.length - 1].lat, navigation[navigation.length - 1].lng];
	let goal;
	if (navigation.length) {
		goal = [parseFloat(navigation[navigation.length - 1]['lat']), parseFloat(navigation[navigation.length - 1]['lng'])];
	} else {
		goal = [17.189578289590823, 104.090411954494540];


	}


	// This is the closest point in the navigation array to the starting point
	const closestPoint = findClosestPoint(from_start[0], from_start[1]);

	// This is the path from the starting point to the goal
	const path: LatLngExpression[] = [
		new LatLng(from_start[0], from_start[1]),
		new LatLng(parseFloat(closestPoint.lat), parseFloat(closestPoint.lng)),
		new LatLng(goal[0], goal[1])
	];


	const _path: LatLngExpression[] = coordinates as LatLngExpression[]

	return (
		<MapContainer center={new LatLng(from_start[0], from_start[1])} zoom={20}
			style={{ height: '100vh' }}
		>
			<TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
			<h1>{from_start[0]}</h1>
			<div>
				<Marker position={new LatLng(from_start[0], from_start[1])}>
					<Popup>
						Your current location.
					</Popup>
				</Marker>
				<Marker position={new LatLng(goal[0], goal[1])}>
					<Popup>
						Your goal location.
					</Popup>
				</Marker>
				<Polyline
					pathOptions={{ color: 'blue' }}
					positions={path}
					dashArray='10, 10'

				/>
				<Polyline pathOptions={{ color: 'red' }} positions={_path} />
			</div>
		</MapContainer>

	);
}

export default NavigationMap;