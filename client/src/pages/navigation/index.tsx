
import { LatLng, LatLngExpression, LatLngTuple } from "leaflet";
import React, { useEffect, useState } from "react";
import {
  MapContainer,
  TileLayer,
  Marker,
  Popup,
  Polyline,
} from "react-leaflet";

type NavigationArrayType = {
  bid: string;
  lat: string;
  lng: string;
}[];

const NavigationPage = () => {
  const from_start = "A7";
  const navigation: NavigationArrayType = [
    {
      bid: "A7",
      lat: "17.191058760990806",
      lng: "104.089470842039700",
    },
    {
      bid: "A6",
      lat: "17.190970159860075",
      lng: "104.088489024228820",
    },
    {
      bid: "A9",
      lat: "17.190634027635916",
      lng: "104.090406832360340",
    },
    {
      bid: "C1",
      lat: "17.189578289590823",
      lng: "104.090411954494540",
    },
    {
      bid: "C5",
      lat: "17.188738469975437",
      lng: "104.091374063713420",
    },
    {
      bid: "C4",
      lat: "17.189400286942945",
      lng: "104.091741718379720",
    },
  ];

  const to_goal: string = "C1";

  const [position, setPosition] = useState<LatLngExpression>([
    parseFloat(navigation[0].lat),
    parseFloat(navigation[0].lng),
  ]);

  useEffect(() => {
    const lastPosition = navigation[navigation.length - 1];
    setPosition([parseFloat(lastPosition.lat), parseFloat(lastPosition.lng)]);
  }, [navigation]);

  useEffect(() => {
    if (navigator.geolocation) {
      navigator.geolocation.watchPosition((position) => {
        setPosition([position.coords.latitude, position.coords.longitude]);
      });
    }
  }, []);

  const currentLocation: LatLngExpression = [
    parseFloat(navigation[0].lat),
    parseFloat(navigation[0].lng),
  ];

  const positionList = navigation.map((nav) => {
    return new LatLng(parseFloat(nav.lat), parseFloat(nav.lng));
  });

  const center: LatLngTuple = [17.1634, 104.1476];

  return (
    <MapContainer center={center} zoom={13}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
      <Marker position={currentLocation}>
        <Popup>{to_goal}</Popup>
      </Marker>
      <Polyline pathOptions={{ color: "blue" }} positions={positionList} />
    </MapContainer>
  );
};

export default NavigationPage;
