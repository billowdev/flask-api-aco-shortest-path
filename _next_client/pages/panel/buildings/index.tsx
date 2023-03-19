import Layout from "@/components/Layouts/Layout";
import React from "react";
import {
  DataGrid,
  GridColDef,
  GridRenderCellParams,
  GridToolbarContainer,
  GridToolbarFilterButton,
  GridValueGetterParams,
} from "@mui/x-data-grid";
import { useAppDispatch } from "@/store/store";
import { deleteBuilding, getBuildings, buildingSelector } from "@/store/slices/buildingSlice";
import { useSelector } from "react-redux";
import {
  Box,
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  Fab,
  Grid,
  IconButton,
  Slide,
  Stack,
  TextField,
  Typography,
} from "@mui/material";
import NumberFormat from "react-number-format";
import Moment from "react-moment";
import router from "next/router";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";
import { TransitionProps } from "@mui/material/transitions";
import Link from "next/link";
// import Add from "./add";
import AddIcon from "@mui/icons-material/Add";
import PlayCircleFilledWhiteIcon from "@mui/icons-material/PlayCircleFilledWhite";
import { stringify } from "querystring";
import withAuth from "@/components/withAuth";
import { BuildingPayload } from "@/models/building.model";
const Transition = React.forwardRef(function Transition(
  props: TransitionProps & {
    children: React.ReactElement<any, any>;
  },
  ref: React.Ref<unknown>
) {
  return <Slide direction="up" ref={ref} {...props} />;
});

const CustomToolbar: React.FunctionComponent<{
  setFilterButtonEl: React.Dispatch<
    React.SetStateAction<HTMLButtonElement | null>
  >;
}> = ({ setFilterButtonEl }) => (
  <GridToolbarContainer>
    <GridToolbarFilterButton ref={setFilterButtonEl} />
    <Link href="/team/add" passHref>
      <Fab
        color="primary"
        aria-label="add"
        sx={{
          position: "absolute",
          top: 10,
          right: 10,
        }}
      >
        <AddIcon />
      </Fab>
    </Link>
  </GridToolbarContainer>
);

type Props = {};

const BuildingPage = ({ }: Props) => {
  const dispatch: any = useAppDispatch();
  const buildingsList: any = useSelector(buildingSelector);
  const [openDialog, setOpenDialog] = React.useState<boolean>(false);
  const [selectedBuilding, setSelectedBuilding] = React.useState<BuildingPayload | null>(null);

  const [filterButtonEl, setFilterButtonEl] =
    React.useState<HTMLButtonElement | null>(null);

  React.useEffect(() => {
    dispatch(getBuildings());
  }, [dispatch]);

  const showDialog = () => {
    if (selectedBuilding === null) {
      return;
    }

    return (
      <Dialog
        open={openDialog}
        keepMounted
        aria-labelledby="alert-dialog-slide-title"
        aria-describedby="alert-dialog-slide-description"
      >
        <DialogTitle id="alert-dialog-slide-title">
          <br />
          Confirm to delete the team? : {selectedBuilding.name}
        </DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-slide-description">
            You cannot restore deleted team.
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpenDialog(false)} color="info">
            Cancel
          </Button>
          <Button onClick={handleDeleteConfirm} color="primary">
            Delete
          </Button>
        </DialogActions>
      </Dialog>
    );
  };

  const handleDeleteConfirm = () => {
    if (selectedBuilding) {
      dispatch(deleteBuilding(String(selectedBuilding.id)));
      setOpenDialog(false);
    }
  };

  const columns: GridColDef[] = [
    // { field: "id", headerName: "ID", width: 280 },

    {
      field: "bid",
      // editable: true,
      headerName: "รหัสโหนด",
      width: 120,
    },
    {
      field: "name",
       editable: true,
      headerName: "ชื่อโหนด",
      width: 120,
    },
    {
      field: "desc",
       editable: true,
      headerName: "รายละเอียด",
      width: 180,
    },
    {
      field: "is_node",
      headerName: "สถานะโหนด",
      width: 100,
    },
    {
      field: "lat",
      headerName: "ละติจูด",
      width: 100,
    },
    {
      field: "lng",
      headerName: "ลองจิจูด",
      width: 100,
    },
    {
      field: "image",
      headerName: "รูปภาพ",
      width: 100,
    },
    {
      headerName: "การดำเนินการ",
      field: ".",
      width: 180,
      renderCell: ({ row }: GridRenderCellParams<any>) => (
        <Stack direction="row">
          <IconButton
            aria-label="delete"
            size="large"
            onClick={() => {
              setSelectedBuilding(row);
              setOpenDialog(true);
            }}
          >
            <DeleteIcon fontSize="inherit" />
          </IconButton>
          <IconButton
            aria-label="edit"
            size="large"
            onClick={() => router.push("/building/edit?id=" + row.id)}
          >
            <EditIcon fontSize="inherit" />
          </IconButton>
        
        </Stack>
      ),
    },
  ];

  return (
    <Layout>
      {/* Summary Icons */}
      <DataGrid
        sx={{ backgroundColor: "white", height: "100vh", width: "80vw" }}
        rows={buildingsList ?? []}
        columns={columns}
        // pageSize={25}
        // rowsPerPageOptions={[25]}
        components={{
          Toolbar: CustomToolbar,
        }}
        componentsProps={{
          panel: {
            anchorEl: filterButtonEl,
          },
          toolbar: {
            setFilterButtonEl,
          },
        }}
      />
      {showDialog()}
    </Layout>
  );
};

export default withAuth(BuildingPage);
