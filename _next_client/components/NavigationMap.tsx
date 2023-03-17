import { useEffect, useRef, useState } from "react";
import { Loader, LoaderOptions } from "@googlemaps/js-api-loader";

interface NavigationMapProps {
  bestPath: string[];
  coordinates: [number, number][];
  navigation: {
    bid: string;
    is_node: boolean;
    lat: string;
    lng: string;
  }[];
  options?: LoaderOptions;
}

const myAPIKey = process.env.NEXT_PUBLIC_GOOGLE_MAPS_API_KEY!;

export default function NavigationMap({
  bestPath,
  coordinates,
  navigation,
  options,
}: NavigationMapProps) {
  const mapRef = useRef<HTMLDivElement>(null);
  const [currentPosition, setCurrentPosition] = useState<[number, number] | null>(null);

  useEffect(() => {
    navigator.geolocation.getCurrentPosition(
      (position) => setCurrentPosition([position.coords.latitude, position.coords.longitude]),
      (error) => console.log(error)
    );
  }, []);

  useEffect(() => {
    if (!currentPosition) return;

    const loader = new Loader({
      apiKey: myAPIKey,
      version: "weekly",
      ...options,
    });

    loader.load().then(() => {
      const map = new google.maps.Map(mapRef.current!, {
        center: new google.maps.LatLng(coordinates[0][0], coordinates[0][1]),
        zoom: 18,
      });

      // Add a marker for each coordinate
      coordinates.forEach(([lat, lng]) => {
        new google.maps.Marker({
          position: { lat, lng },
          map,
        });
      });

      // Create a polyline to connect the coordinates in the best path
      const path = new google.maps.Polyline({
        path: bestPath.map((node) => {
          const index = parseInt(node.slice(1)) - 1;
          return { lat: coordinates[index][0], lng: coordinates[index][1] };
        }),
        strokeColor: "#FF0000",
        strokeOpacity: 1.0,
        strokeWeight: 3,
      });
      path.setMap(map);

      // Navigate from start to goal
      let currentIndex = 0;
      let currentLocation = new google.maps.LatLng(
        parseFloat(navigation[currentIndex].lat),
        parseFloat(navigation[currentIndex].lng)
      );
      const goalIndex = navigation.findIndex(
        (node) => node.bid === navigation[navigation.length - 1].bid
      );
      const goalLocation = new google.maps.LatLng(
        parseFloat(navigation[goalIndex].lat),
        parseFloat(navigation[goalIndex].lng)
      );
      const marker = new google.maps.Marker({
        position: currentLocation,
        map,
      });
      const step = () => {
        currentIndex++;
        if (currentIndex <= goalIndex) {
          const nextLocation = new google.maps.LatLng(
            parseFloat(navigation[currentIndex].lat),
            parseFloat(navigation[currentIndex].lng)
          );
          marker.setPosition(nextLocation);
          setTimeout(step, 1000);
        }
      };
      setTimeout(step, 1000);
    });
  }, [bestPath, coordinates, navigation, options, currentPosition]);

  return <div ref={mapRef} style={{ height: "100vh" }} />;
}
