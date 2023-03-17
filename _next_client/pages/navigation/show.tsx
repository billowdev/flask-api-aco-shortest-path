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
import * as navigationService from "@/services/navigationService"


// const Map = dynamic(() => import("./map"), { ssr: false });
type Props = {}



function ShowMap({ }: Props) {
  const [payload, setPayload] = useState({
    best_path: [],
    coordinates: [],
    distance: 0,
    from_start: "",
    navigation: [],
    to_goal: "",
  });

  const handleFetchData = async () => {
    const response = await navigationService.getNavigation({ start: "G1", goal: "A9" });
    console.log('====================================');
    console.log(response.payload);
    console.log('====================================');
    setPayload(response.payload);
  };

  const Map = React.useMemo(() => dynamic(
    () => import('./map'), // replace '@components/map' with your component's location
    {
      loading: () => <p>A map is loading</p>,
      ssr: false // This line is important. It's what prevents server-side render
    }
  ), [/* list variables which should trigger a re-render here */
    payload
])
  return <div>
    <button onClick={handleFetchData}>Fetch Data</button>
    {payload.best_path.length > 0 && (
      <Map
        bestPath={payload.best_path}
        coordinates={payload.coordinates} navigation={payload.navigation} />
    )}
  </div>
}

export default ShowMap

