import { LatLng, LatLngExpression } from 'leaflet';
import { useEffect, useState } from 'react';
import { MapContainer, TileLayer, Marker, Polyline } from 'react-leaflet';
type NavigationArrayType = {
	bid: string;
	lat: string;
	lng: string;
}[];

interface MapProps {
	navigation: NavigationArrayType;
}

const MapComponent: React.FC<MapProps> = ({ navigation }) => {
	const [currentPosition, setCurrentPosition] = useState<[number, number]>([0, 0]); // initialize with dummy values

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

	// This function is called when the component mounts, and it gets the current location from the browser
	useEffect(() => {
		navigator.geolocation.getCurrentPosition(
			position => setCurrentPosition([position.coords.latitude, position.coords.longitude]),
			error => console.log(error)
		);
	}, []);

	// This is the starting point (it can be replaced with the current position from GPS)
	const from_start: LatLngExpression = currentPosition.length ? [currentPosition[0], currentPosition[1]] : [0, 0];

	// This is the goal (it can be any point in the navigation array)
	const goal: LatLngExpression = [parseFloat(navigation[navigation.length - 1].lat), parseFloat(navigation[navigation.length - 1].lng)];

	// This is the closest point in the navigation array to the starting point
	const closestPoint = findClosestPoint(from_start[0], from_start[1]);

	// This is the path from the starting point to the goal
	const path: LatLngExpression[] = [
		new LatLng(from_start[0], from_start[1]),
		new LatLng(parseFloat(closestPoint.lat), parseFloat(closestPoint.lng)),
		new LatLng(goal[0], goal[1])
	];
	return (
		<MapContainer center={from_start} zoom={15}>
			<TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
			<Marker position={from_start} />
			<Marker position={goal} />
			<Polyline pathOptions={{ color: 'blue' }} positions={path} />
		</MapContainer>
	);
}

export default MapComponent
