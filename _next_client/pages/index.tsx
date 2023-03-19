import React from 'react'
import dynamic from "next/dynamic";
import { useEffect, useState } from 'react';
import * as navigationService from "@/services/navigationService"
import { Button, Container, Grid, Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import { GetStaticProps } from 'next';
import ModalList from '@/components/ModalList';
import { LatLngBoundsExpression, LatLngExpression } from 'leaflet';
import { BuildingPayload } from '@/models/building.model';
import Image from 'next/image';
import { BUILDING_IMAGE_ROUTE, ENDPOINT } from '@/utils/constant.util';
import Footer from '@/components/Footer';
import { Box } from '@mui/material';
import { useMediaQuery } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import Layout from "@/components/Layouts/Layout";
import MyLocationIcon from '@mui/icons-material/MyLocation';
import NavigationIcon from '@mui/icons-material/Navigation';
import PlaceIcon from '@mui/icons-material/Place';
import PersonIcon from '@mui/icons-material/Person';

const MapContainer = dynamic(() => import('react-leaflet').then((mod) => mod.MapContainer), {
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


type Props = {
  nodes: string[];
  buildings: BuildingPayload[]
}



function Navigation({ nodes, buildings }: Props) {



  const center: LatLngExpression = [17.188552015996446, 104.08972433221602]; // Centered on Sakon Nakhon Province
  const zoom: number = 16;

  const bounds: LatLngBoundsExpression = [
    [17.18355011514967, 104.08249309701569], // Southwest corner of Sakon Nakhon Province
    [17.19193437239573, 104.09560373412965] // Northeast corner of Sakon Nakhon Province
  ];

  const [modalOpen, setModalOpen] = useState(false);
  const [selectedNode, setSelectedNode] = useState(null);

  const handleModalOpen = () => {
    setModalOpen(true);
  };

  const handleModalClose = () => {
    setModalOpen(false);
  };

  const handleNodeSelect = (node: any) => {
    setSelectedNode(node);
    setModalOpen(false);
  };

  const [payload, setPayload] = useState({
    best_path: [],
    coordinates: [],
    distance: 0,
    from_start: "",
    navigation: [],
    to_goal: "",
  });

  const handleFetchData = async () => {
    if (selectedNode) {
      const response = await navigationService.getNavigation({ start: currentPosition, goal: selectedNode });
      setPayload(response.payload);
    }
  };

  const [currentPosition, setCurrentPosition] = useState<[number, number]>([17.189578289590823, 104.090411954494540]); // initialize with dummy values
  useEffect(() => {
    const intervalId = setInterval(() => {
      navigator.geolocation.getCurrentPosition(
        position => setCurrentPosition([position.coords.latitude, position.coords.longitude]),
        error => console.log(error)
      );
    }, 3000);

    return () => clearInterval(intervalId);
  }, []);
  const hadnleCurrentLocation = async () => {
    navigator.geolocation.getCurrentPosition(
      position => setCurrentPosition([position.coords.latitude, position.coords.longitude]),
      error => console.log(error)
    );
  }

  const Map = React.useMemo(() => dynamic(
    () => import('../components/MapComponent'), // replace '@components/map' with your component's location
    {
      loading: () => <p>A map is loading</p>,
      ssr: false // This line is important. It's what prevents server-side render
    }


  ), [/* list variables which should trigger a re-render here */

  ])

  const theme = useTheme();
  const isSmallerScreen = useMediaQuery(theme.breakpoints.down('sm'));

  return (
       <Box>

      <Container style={{
        marginTop: "20px"
      }}>
        <Grid container style={{
          marginBottom: "20px",
          justifyContent: "center",
        }}>
          <Grid item style={{ margin: isSmallerScreen ? "10px 0" : "0 10px" }}>
            <Button variant="contained" color="primary" onClick={hadnleCurrentLocation}>
             <MyLocationIcon /> ตำแหน่งปัจจุบัน
            </Button>
          </Grid>
          <Grid item style={{ margin: isSmallerScreen ? "10px 0" : "0 10px" }}>
            <Button variant="contained" color="primary" onClick={handleModalOpen}>
             <PlaceIcon /> เลือกปลายทาง
            </Button>
            <ModalList open={modalOpen} onClose={handleModalClose} onSelect={handleNodeSelect} nodes={buildings} />
          </Grid>
          <Grid item style={{ margin: isSmallerScreen ? "10px 0" : "0 10px" }}>
            <Button variant="contained" color="primary" onClick={handleFetchData}>
             <NavigationIcon /> เริ่มต้นนำทาง
            </Button>
          </Grid>

        </Grid>
        <Box marginBottom={1}>
          {selectedNode && (
            <>
              <Typography variant="h5" gutterBottom>
                ปลายทาง
              </Typography>
              <Box marginTop={1}>
                {buildings
                  .filter(({ bid }) => bid === selectedNode)
                  .map((building) => (
                    <Box key={building.id}>
                      <Typography> Building ID: {building.bid}</Typography>
                      <Typography> Name: {building.name}</Typography>
                    </Box>
                  ))}
              </Box>
            </>
          )}
        </Box>

        {payload.best_path.length > 0 ? (
          <Map
            bestPath={payload.best_path}
            coordinates={payload.coordinates}
            navigation={payload.navigation}
          />
        ) : (
          <MapContainer
            center={center}
            zoom={zoom}
            bounds={bounds}
            scrollWheelZoom={true}
            style={{
              height: "100vh",
              width: "100%",
              marginBottom: "20px"
            }}

          >
            <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
            <Marker position={currentPosition} autoPanOnFocus autoPan>
              <Popup>
                <div>
                  <h3>ตำแหน่งปัจจุบันของคุณ</h3>
                </div>
              </Popup>
            </Marker>

            {buildings.map(({ bid, name, desc, lat, lng, image }) => (
              <Marker key={bid} position={[parseFloat(lat), parseFloat(lng)]}>
                <Popup>
                  <div>
                    <h3>{bid}</h3>
                    <h3>{name}</h3>
                    <p>{desc}</p>
                    <Image
                      src={`${BUILDING_IMAGE_ROUTE}/${image}`}
                      alt="My Image"
                      width={100}
                      height={100}
                    />
                  </div>
                </Popup>
              </Marker>
            ))}
          </MapContainer>
        )
        }
      </Container>

      <Footer />
    </Box>

  )
}

export const getStaticProps: GetStaticProps<Props> = async () => {

  const nodeResponse = await navigationService.getNode();
  const buildingsResponse = await navigationService.getBuildings();
  const nodes = nodeResponse.payload[0];
  const buildings = buildingsResponse.payload;

  return {
    props: {
      nodes,
      buildings
    }
  };
};


export default Navigation
