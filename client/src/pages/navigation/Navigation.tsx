import { LatLng, LatLngExpression } from 'leaflet';
import { useEffect, useState } from 'react';

import { MapContainer, TileLayer, Marker, Polyline, Popup, } from 'react-leaflet';

type NavigationArrayType = {
	bid: string;
	lat: string;
	lng: string;
}[];
// const NavigationMap = ({ currentPosition }: { currentPosition: number[] }) => {
const NavigationMap = () => {
	const [currentPosition, setCurrentPosition] = useState<[number, number]>([17.189578289590823, 104.090411954494540]); // initialize with dummy values
	// This function is called when the component mounts, and it gets the current location from the browser
	// useEffect(() => {
	// 	navigator.geolocation.getCurrentPosition(
	// 		position => setCurrentPosition([position.coords.latitude, position.coords.longitude]),
	// 		error => console.log(error)
	// 	);
	// }, []);

	useEffect(() => {
		const positions = [
			[17.189578289590823, 104.090411954494540],
			[17.189400286942945, 104.091741718379720],
			[17.190634027635916, 104.090406832360340],
			[17.191058760990806, 104.089470842039700],
		];
		let counter = 0;
		const intervalId = setInterval(() => {
			setCurrentPosition([positions[counter][0], positions[counter][1]]);
			counter = (counter + 1) % positions.length;
		}, 2000);

		return () => clearInterval(intervalId);
	}, []);


	// useEffect(() => {
	// 	setInterval(() => {
	// 		setCurrentPosition([17.189578289590823, 104.090411954494540])

	// 		setCurrentPosition([17.188738469975437, 104.091374063713420])

	// 		setCurrentPosition([17.189400286942945, 104.091741718379720])

	// 		setCurrentPosition([17.190634027635916, 104.090406832360340])
	// 	}, 1000)

	// }, [])



	const navigation: NavigationArrayType = [
		{
			"bid": "C1",
			"lat": "17.189578289590823",
			"lng": "104.090411954494540"
		},

		{
			"bid": "C5",
			"lat": "17.188738469975437",
			"lng": "104.091374063713420"
		},
		{
			"bid": "C4",
			"lat": "17.189400286942945",
			"lng": "104.091741718379720"
		},
		{
			"bid": "A9",
			"lat": "17.190634027635916",
			"lng": "104.090406832360340"
		},
		{
			"bid": "A7",
			"lat": "17.191058760990806",
			"lng": "104.089470842039700"
		},

	]
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
	const goal = [navigation[navigation.length - 1].lat, navigation[navigation.length - 1].lng];

	// This is the closest point in the navigation array to the starting point
	const closestPoint = findClosestPoint(from_start[0], from_start[1]);

	// This is the path from the starting point to the goal
	const path: LatLngExpression[] = [
		new LatLng(from_start[0], from_start[1]),
		new LatLng(parseFloat(closestPoint.lat), parseFloat(closestPoint.lng)),
		new LatLng(parseFloat(goal[0]), parseFloat(goal[1]))
	];

	const _path: LatLngExpression[] = [
		[17.189578289590823, 104.090411954494540],
		[17.189400286942945, 104.091741718379720],
		[17.190634027635916, 104.090406832360340],
		[17.191058760990806, 104.089470842039700],
	];

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
				<Marker position={new LatLng(parseFloat(goal[0]), parseFloat(goal[1]))}>
					<Popup>
						Your goal location.
					</Popup>
				</Marker>
				<Polyline pathOptions={{ color: 'blue' }} positions={path} />
				<Polyline pathOptions={{ color: 'red' }} positions={_path} />
			</div>
		</MapContainer>
	);
}

export default NavigationMap;
