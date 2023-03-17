import { LatLng, LatLngBoundsExpression, LatLngExpression } from 'leaflet';
import { useEffect, useState } from 'react';
import { getNavigation, navigationSelector, coordinatesSelector } from "../../store/slices/navigationSlice";
import { useSelector } from "react-redux";

import React from 'react';
// import { useAppDispatch, useAppSelector } from '../store';
import { useAppDispatch } from '@/store/store';
import { NavigationModel } from './../../models/navigation.model';
import { CoordinatesType } from '@/models/navigation.model';
import { store } from "@/store/store";
import dynamic from 'next/dynamic';


const MapContainer = dynamic(() => import('react-leaflet').then((mod) => mod.MapContainer), {
	ssr: false, // disable server-side rendering
});

const Polyline = dynamic(() => import('react-leaflet').then((mod) => mod.Polyline), {
	ssr: false, // disable server-side rendering
});
const TileLayer = dynamic(() => import('react-leaflet').then((mod) => mod.TileLayer), {
	ssr: false, // disable server-side rendering
});
const Marker = dynamic(() => import('react-leaflet').then((mod) => mod.Marker), {
	ssr: false, // disable server-side rendering
});
const Popup = dynamic(() => import('react-leaflet').then((mod) => mod.Popup), {
	ssr: false, // disable server-side rendering
});


interface NavigationMapProps {
	bestPath: string[];
	coordinates: [number, number][];
	navigation: {
		bid: string;
		is_node: boolean;
		lat: string;
		lng: string;
	}[];
}

// const CustomNavigationMap = ({ currentPosition }: { currentPosition: number[] }) => {
const CustomNavigationMap = (
	{
		bestPath,
		coordinates,
		navigation,
	}: NavigationMapProps
) => {

	const [isBrowser, setIsBrowser] = React.useState(false);
	React.useEffect(() => {
		setIsBrowser(true);
	}, []);




	const dispatch: any = useAppDispatch();
	

	React.useEffect(() => {
		dispatch(getNavigation({ start: "G1", goal: "C1" }))

	}, [dispatch]);


	const [currentPosition, setCurrentPosition] = useState<[number, number]>([17.189578289590823, 104.090411954494540]); // initialize with dummy values
	useEffect(() => {
		navigator.geolocation.getCurrentPosition(
			position => setCurrentPosition([position.coords.latitude, position.coords.longitude]),
			error => console.log(error)
		);
	}, []);


	// React.useEffect(() => {
	// 	let counter = 0;
	// 	const intervalId = setInterval(() => {
	// 		setCurrentPosition([coordinates[counter][0], coordinates[counter][1]]);
	// 		counter = (counter + 1) % coordinates.length;
	// 	}, 1000);

	// 	return () => clearInterval(intervalId);
	// }, [coordinates]);



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
	const fromStart = currentPosition.length ? [currentPosition[0], currentPosition[1]] : [0, 0];

	// // This is the goal (it can be any point in the navigation array)
	const toGoal = [navigation[navigation.length - 1].lat, navigation[navigation.length - 1].lng];

	// This is the closest point in the navigation array to the starting point
	const closestPoint = findClosestPoint(fromStart[0], fromStart[1]);

	// This is the path from the starting point to the goal
	const path: LatLngExpression[] = [
		new LatLng(fromStart[0], fromStart[1]),
		new LatLng(parseFloat(closestPoint.lat), parseFloat(closestPoint.lng)),
		new LatLng(parseFloat(toGoal[0]), parseFloat(toGoal[1]))
	];

	const _path: LatLngExpression[] = coordinates as LatLngExpression[]


	if (!isBrowser) {
		return null;
	}


	return (
		<MapContainer center={[fromStart[0], fromStart[1]]} zoom={20} style={{ height: '100vh' }}>
			<TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
			<h1>{fromStart[0]}</h1>
			<div>
				<Marker position={[fromStart[0], fromStart[1]]}>
					<Popup>Your current location.</Popup>
				</Marker>
				<Marker position={[parseFloat(toGoal[0]), parseFloat(toGoal[1])]}>
					<Popup>Your goal location.</Popup>
				</Marker>
				<Polyline pathOptions={{ color: 'blue', dashArray: '10, 10' }} positions={path} />
				<Polyline pathOptions={{ color: 'red' }} positions={_path} />
			</div>
		</MapContainer>
	);

}

export default CustomNavigationMap;

