import * as React from "react";
import { styled, useTheme, Theme, CSSObject } from "@mui/material/styles";
import MuiDrawer from "@mui/material/Drawer";
import List from "@mui/material/List";
import Divider from "@mui/material/Divider";
import IconButton from "@mui/material/IconButton";
import ChevronLeftIcon from "@mui/icons-material/ChevronLeft";
import ChevronRightIcon from "@mui/icons-material/ChevronRight";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import { blue } from "@mui/material/colors";
import { Box, ListItem, Stack } from "@mui/material";
import Link from "next/link";
import Image from "next/image";
import { Layers, BarChart, Person } from "@mui/icons-material";
import { useRouter } from "next/router";
import GroupsIcon from "@mui/icons-material/Groups";
import HistoryIcon from "@mui/icons-material/History";
import Timer10Icon from "@mui/icons-material/Timer10";
const drawerWidth = 240;
import TimerIcon from "@mui/icons-material/Timer";
import { userSelector } from "@/store/slices/userSlice";
import { useSelector } from "react-redux";
import LoginIcon from '@mui/icons-material/Login';
import MyLocationIcon from '@mui/icons-material/MyLocation';
import NavigationIcon from '@mui/icons-material/Navigation';
import PlaceIcon from '@mui/icons-material/Place';
import PersonIcon from '@mui/icons-material/Person';
const openedMixin = (theme: Theme): CSSObject => ({
  width: drawerWidth,
  transition: theme.transitions.create("width", {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.enteringScreen,
  }),
  overflowX: "hidden",
});

const closedMixin = (theme: Theme): CSSObject => ({
  transition: theme.transitions.create("width", {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  overflowX: "hidden",
  width: `calc(${theme.spacing(7)} + 1px)`,
  [theme.breakpoints.up("sm")]: {
    width: `calc(${theme.spacing(8)} + 1px)`,
  },
});

const DrawerHeader = styled("div")(({ theme }) => ({
  display: "flex",
  alignItems: "center",
  justifyContent: "flex-end",
  padding: theme.spacing(0, 1),
  // necessary for content to be below app bar
  ...theme.mixins.toolbar,
}));

const Drawer = styled(MuiDrawer, {
  shouldForwardProp: (prop) => prop !== "open",
})(({ theme, open }) => ({
  width: drawerWidth,
  flexShrink: 0,
  whiteSpace: "nowrap",
  boxSizing: "border-box",
  ...(open && {
    ...openedMixin(theme),
    "& .MuiDrawer-paper": openedMixin(theme),
  }),
  ...(!open && {
    ...closedMixin(theme),
    "& .MuiDrawer-paper": closedMixin(theme),
  }),
}));

type MenuProp = {
  open: boolean;
  onDrawerClose: () => void;
};

export default function Menu({ open, onDrawerClose }: MenuProp) {
  const theme = useTheme();
  const router = useRouter();
  const userData = useSelector(userSelector);

  return (
    <Drawer variant="permanent" open={open}>
      <DrawerHeader>
        <Stack
          direction="row"
          alignItems="center"
          sx={{ backgroundColor: blue }}
        >
          <Image
            // src="/static/img/logo-horizontal.png"
            src="/static/img/logo-h.png"
            
            width={200}
            height={40}
            alt="logo"
          />
          <IconButton onClick={onDrawerClose}>
            {theme.direction === "ltr" ? (
              <ChevronLeftIcon />
            ) : (
              <ChevronRightIcon />
            )}
          </IconButton>
        </Stack>
      </DrawerHeader>

      <Divider />
      <List>
              <Link href="/panel/buildings" passHref>
          <ListItem
            button
            className={router.pathname === "/panel/buildings" ? "Mui-selected" : ""}
          >
            <ListItemIcon>
              <PlaceIcon />
            </ListItemIcon>
            <ListItemText primary="จัดการข้อมูลอาคาร" />
          </ListItem>
        </Link>
        
        <Link href="/panel/users" passHref>
          <ListItem
            button
            className={router.pathname === "/panel/users" ? "Mui-selected" : ""}
          >
            <ListItemIcon>
              <PersonIcon />
            </ListItemIcon>
            <ListItemText primary="จัดการข้อมูลสมาชิก" />
          </ListItem>
        </Link>

        <Divider />

<Link href="/timer" passHref>
          <ListItem
            className={router.pathname === "/" ? "Mui-selected" : ""}
          >
            <ListItemIcon>
              <NavigationIcon />
            </ListItemIcon>
            <ListItemText primary="ระบบนำทาง" />
          </ListItem>
        </Link>


      </List>
    </Drawer>
  );
}
