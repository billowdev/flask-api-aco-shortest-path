import React from 'react'
import dynamic from "next/dynamic";
import { LatLng, LatLngExpression } from 'leaflet';
import { useEffect, useState } from 'react';
import { getNavigation, navigationSelector } from "../../store/slices/navigationSlice";
import { useSelector } from "react-redux";
import { MapContainer, TileLayer, Marker, Polyline, Popup, } from 'react-leaflet';
import { GetServerSideProps } from 'next';
// import { useAppDispatch, useAppSelector } from '../store';
import { useAppDispatch } from '@/store/store';


const Map = dynamic(() => import("./map"), { ssr: false });
type Props = {}



function HomePage({ }: Props) {
	// const dispatch: any = useAppDispatch();
	// const navigationList: any = useSelector(navigationSelector);

	// React.useEffect(() => {
	// 	dispatch(getNavigation({ start: "G1", goal: "C1" }));
	// }, [dispatch]);

	// const [currentPosition, setCurrentPosition] = useState<[number, number]>([17.189578289590823, 104.090411954494540]); // initialize with dummy values
	// // This function is called when the component mounts, and it gets the current location from the browser
	// // useEffect(() => {
	// // 	navigator.geolocation.getCurrentPosition(
	// // 		position => setCurrentPosition([position.coords.latitude, position.coords.longitude]),
	// // 		error => console.log(error)
	// // 	);
	// // }, []);


	// React.useEffect(() => {

	// 	let counter = 0;
	// 	const intervalId = setInterval(() => {
	// 		setCurrentPosition([navigationList.coordinates[counter][0], navigationList.coordinates[counter][1]]);
	// 		counter = (counter + 1) % navigationList.coordinates.length;
	// 	}, 1000);

	// 	return () => clearInterval(intervalId);
	// }, []);



	// // This function calculates the distance between two points using the Haversine formula
	// const calculateDistance = (lat1: number, lon1: number, lat2: number, lon2: number) => {
	// 	const R = 6371; // Radius of the earth in km
	// 	const dLat = (lat2 - lat1) * Math.PI / 180; // deg2rad below
	// 	const dLon = (lon2 - lon1) * Math.PI / 180;
	// 	const a =
	// 		Math.sin(dLat / 2) * Math.sin(dLat / 2) +
	// 		Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
	// 		Math.sin(dLon / 2) * Math.sin(dLon / 2);
	// 	const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
	// 	const d = R * c; // Distance in km
	// 	return d;
	// }
	// // This function finds the closest point in the navigation array to the current position
	// const findClosestPoint = (lat: number, lng: number) => {
	// 	let closestPoint = navigationList.navigation[0];

	// 	let closestDistance = calculateDistance(lat, lng, parseFloat(closestPoint.lat), parseFloat(closestPoint.lng));
	// 	for (let i = 1; i < navigationList.navigation.length; i++) {
	// 		const distance = calculateDistance(lat, lng, parseFloat(navigationList.navigation[i].lat), parseFloat(navigationList.navigation[i].lng));
	// 		if (distance < closestDistance) {
	// 			closestPoint = navigationList.navigation[i];
	// 			closestDistance = distance;
	// 		}
	// 	}
	// 	return closestPoint;
	// }


	// // This is the starting point (it can be replaced with the current position from GPS)
	// const from_start = currentPosition.length ? [currentPosition[0], currentPosition[1]] : [0, 0];

	// // This is the goal (it can be any point in the navigation array)
	// const goal = [navigationList.navigation[navigationList.navigation.length - 1].lat, navigationList.navigation[navigationList.navigation.length - 1].lng];

	// // This is the closest point in the navigation array to the starting point
	// const closestPoint = findClosestPoint(from_start[0], from_start[1]);

	// // This is the path from the starting point to the goal
	// const path: LatLngExpression[] = [
	// 	new LatLng(from_start[0], from_start[1]),
	// 	new LatLng(parseFloat(closestPoint.lat), parseFloat(closestPoint.lng)),
	// 	new LatLng(parseFloat(goal[0]), parseFloat(goal[1]))
	// ];

	// const _path: LatLngExpression[] = navigationList.coordinates as LatLngExpression[]

  return (
      <Map 
	//   navigation={navigationList.navigation} fromStart={from_start} toGoal={goal} path={path} _path={_path} 
	  />


  )
}

export default HomePage

// export const getServerSideProps: GetServerSideProps = async (context) => {
// 	const { store } = context;
// 	await store.dispatch(getNavigation({ start: "G1", goal: "C1" }));
// 	const navigationList = navigationSelector(store.getState());

// 	return {
// 		props: {
// 			navigationList,
// 		},
// 	};
// };