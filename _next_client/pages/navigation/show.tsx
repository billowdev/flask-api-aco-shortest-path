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


// const Map = dynamic(() => import("./map"), { ssr: false });
type Props = {}



function ShowMap({ }: Props) {
  const Map = React.useMemo(() => dynamic(
    () => import('./map'), // replace '@components/map' with your component's location
    { 
      loading: () => <p>A map is loading</p>,
      ssr: false // This line is important. It's what prevents server-side render
    }
  ), [/* list variables which should trigger a re-render here */])
  return <Map />
}

export default ShowMap

