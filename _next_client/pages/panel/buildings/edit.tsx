import Layout from "@/components/Layouts/Layout";
import { BuildingPayload } from "@/models/building.model";
import { getBuilding, getBuildings } from "@/services/buildingService";
import dynamic from "next/dynamic";
import {
  Card,
  CardContent,
  Typography,
  CardActions,
  Button,
} from "@mui/material";
import { Field, Form, Formik, FormikProps } from "formik";
import { TextField } from "formik-material-ui";
import { GetServerSideProps, GetServerSidePropsContext } from "next";
import Link from "next/link";
import React, { useEffect } from "react";
import Image from "next/image";
import { Router, useRouter } from "next/router";
import { useAppDispatch } from "@/store/store";
import { updateBuilding } from "@/store/slices/buildingSlice";
import toast, { Toaster } from "react-hot-toast";
import withAuth from "@/components/withAuth";
import { LatLng, LatLngExpression } from 'leaflet';

export interface BuildingPayloadC {
	bid: string
	desc: string
	id: number
	is_node: boolean
	lat?: string
	lng?: string
	name: string
	image: string
  }
  

type Props = {
  building: BuildingPayload;
  allBuildings: BuildingPayload[]
  // building: BuildingPayloadC;
  // allBuildings: BuildingPayloadC[]
};


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



const Edit = ({ building, allBuildings }: Props) => {
  const [currentLatLng, setCurrentLatLng] = React.useState<[number, number]>([parseFloat(building.lat), parseFloat(building.lng)]);
  const center: LatLngExpression = [currentLatLng[0], currentLatLng[1]];
  const zoom: number = 16;

  const handleMarkerDragEnd = (event: any) => {
    console.log([parseFloat(event.target.getLatLng()['lat']), parseFloat(event.target.getLatLng()['lng'])])
    setCurrentLatLng([parseFloat(event.target.getLatLng()['lat']), parseFloat(event.target.getLatLng()['lng'])])
  }

  const router = useRouter();
  const dispatch = useAppDispatch();
  const showForm = ({
    values,
    setFieldValue,
    isValid,
  }: FormikProps<BuildingPayload>) => {
    return (
      <Form>
        <Card>
          <CardContent sx={{ padding: 4 }}>
            <Typography gutterBottom variant="h3">
              แก้ไขข้อมูลอาคาร
            </Typography>
            <Field
              style={{ marginTop: 16 }}
              fullWidth
              component={TextField}
              name="bid"
              type="text"
              label="รหัสอาคาร/โหนด"
            />
   

            <Field
              style={{ marginTop: 16 }}
              fullWidth
              component={TextField}
              name="name"
              type="text"
              label="ชื่ออาคาร"
            />
            <br />
            <Field
              style={{ marginTop: 16 }}
              fullWidth
              component={TextField}
              name="desc"
              type="text"
              label="รายละเอียด"
            />
            <br />
           <Field
              style={{ marginTop: 16 }}
              fullWidth
              component={TextField}
              onChange={(e: React.ChangeEvent<any>) => {
                e.preventDefault();
                setFieldValue("lat", currentLatLng[0].toString());
              }}
              name="lat"
              type="text"
              label="ละติจูด"
            />
            <br />
            <Field
              style={{ marginTop: 16 }}
              fullWidth
              onChange={(e: React.ChangeEvent<any>) => {
                e.preventDefault();
                setFieldValue("lng", currentLatLng[1].toString());
              }}
              component={TextField}
              name="lng"
              type="text"
              label="ลองจิจูด"
            />
            <br />
          </CardContent>
          <CardActions>
            <Button
              disabled={!isValid}
              fullWidth
              variant="contained"
              color="primary"
              type="submit"
              sx={{ marginRight: 1 }}
            >
              Edit
            </Button>
            <Link href="/panel/buildings" passHref>
              <Button variant="outlined" fullWidth>
                Cancl
              </Button>
            </Link>
          </CardActions>
        </Card>
      </Form>
    );
  };

  return (
    <Layout>
      <Formik
        validate={(values) => {
          let errors: any = {};
          if (!values.bid) errors.bid = "กรุณากรอกรหัสโหนด";
          if (!values.name) errors.name = "กรุณากรอกชื่ออาคาร";
          return errors;
        }}
        initialValues={{
          name: building.name,
          desc: building.desc,
          bid: building.bid,
          image: building.image,
          id: building.id,
          is_node: building.is_node,
          lat: building.lat,
          lng:building.lng
        }}
        onSubmit={async (values, { setSubmitting }) => {
          const newLat = (currentLatLng[0]).toString();
          const newLng = (currentLatLng[1]).toString() 
          const newUpdateLatLng = {
            ...values, 
            ...{lat:newLat}, 
            ...{lng:newLng}
          }
          const updateStatus = await dispatch(updateBuilding(newUpdateLatLng))
          // console.log(newUpdateLatLng)
          // console.log(newUpdateLatLng)
          // console.log("=================")
          if (updateStatus.meta.requestStatus === "fulfilled") {
            toast.success("แก้ไขข้อมูลอาคารสำเร็จ")
            router.push("/panel/buildings")
          }
          setSubmitting(false);
        }}
      >
        {(props) => showForm(props)}
      </Formik>

      <MapContainer center={center} zoom={zoom} style={{ height: "500px", width: "100%" }}>
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />

       <Marker position={center} draggable={true} eventHandlers={{
          dragend: handleMarkerDragEnd
        }}
        >     

          <Popup autoClose={false}>
        <span>โหนดที่กำลังแก้ไข</span>
      </Popup></Marker> 


      {/* {allBuildings.map(({ bid, name, desc, lat, lng, image }) => (
              <Marker key={bid} position={[parseFloat(lat), parseFloat(lng)]}>
                <Popup>
                  <div>
                    <h3>{bid}</h3>
                    <h3>{name}</h3>
                    <p>{desc}</p>
                  </div>
                </Popup>
              </Marker>
            ))} */}

      </MapContainer>

      

    </Layout>
  );
};

export default withAuth(Edit);

export const getServerSideProps: GetServerSideProps = async (
  context: GetServerSidePropsContext
) => {
  const { dataId }: any = context.query;
  if (dataId) {
    const building = await getBuilding(dataId);
    const allBuildings = await getBuildings();
    return {
      props: {
        building,
        allBuildings
      },
    };
  } else {
    return { props: {} };
  }
};
