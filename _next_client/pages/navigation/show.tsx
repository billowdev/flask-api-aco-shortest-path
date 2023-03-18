import React from 'react'
import dynamic from "next/dynamic";
import { useEffect, useState } from 'react';
import * as navigationService from "@/services/navigationService"
import { Button, Grid } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import { GetStaticProps } from 'next';
import axios from 'axios';
import { ENDPOINT } from '@/common/constants/common.constant';
import ModalList from '@/components/ModalList';

type Props = {
  nodes: string[];
}

const useStyles = makeStyles({
  root: {
    margin: "20px",
  },
});

function ShowMap({ nodes }: Props) {
  console.log('====================================');
  console.log(nodes);
  console.log('====================================');

  const classes = useStyles();

  const [modalOpen, setModalOpen] = useState(false);
  const [selectedNode, setSelectedNode] = useState(null);

  const handleModalOpen = () => {
    setModalOpen(true);
  };

  const handleModalClose = () => {
    setModalOpen(false);
  };

  const handleNodeSelect = (node:any) => {
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
    if(selectedNode){
      const response = await navigationService.getNavigation({ start: "G1", goal:selectedNode });
      setPayload(response.payload);
    }else{
      const response = await navigationService.getNavigation({ start: "G1", goal:"C1" });
      setPayload(response.payload);
    }
  };

  const hadnleCurrentLocation = async () => {

  }

  const Map = React.useMemo(() => dynamic(
    () => import('../../components/MapComponent'), // replace '@components/map' with your component's location
    {
      loading: () => <p>A map is loading</p>,
      ssr: false // This line is important. It's what prevents server-side render
    }
  ), [/* list variables which should trigger a re-render here */

  ])
  return (
    <div className={classes.root}>
      <Grid container spacing={2}>
        <Grid item>
          <Button variant="contained" color="primary" onClick={hadnleCurrentLocation}>
            ตำแหน่งปัจจุบัน
          </Button>
        </Grid>

        <Grid item>
          <Button variant="contained" color="primary" onClick={handleModalOpen}>
          เลือกปลายทาง
          </Button>
          <ModalList open={modalOpen} onClose={handleModalClose} onSelect={handleNodeSelect} nodes={nodes} />
        </Grid>
        
        <Grid item>
          <Button variant="contained" color="primary" onClick={handleFetchData}>
            เริ่มต้นนำทาง
          </Button>
        </Grid>

        <Grid item>
        {selectedNode && (
            <h5>ปลายทาง: {selectedNode}</h5>
          )}
        </Grid>

  
      </Grid>
      {payload.best_path.length > 0 && (
        <Map
          bestPath={payload.best_path}
          coordinates={payload.coordinates}
          navigation={payload.navigation}
        />
      )}
    </div>
  )
}

export const getStaticProps: GetStaticProps<Props> = async () => {

  const data = await navigationService.getNode();
  const nodes = data.payload[0];
  return {
    props: {
      nodes
    }
  };
};

export default ShowMap

