import React from "react";
import { AppBar, Toolbar, Typography, Grid, Link, Box, Button } from "@material-ui/core";
import { Info, Security } from "@mui/icons-material";

const Footer = () => (
  <Box>
    <AppBar position="static" elevation={0} component="footer" color="primary" >
      <Toolbar style={{ justifyContent: "center" }}>
        <Typography variant="caption">
          <a href="https://github.com/billowdev">©2023 Billowdev</a>
        </Typography>
        <Box sx={{ flexGrow: 1 }} />
        <Button color="inherit" href="/panel/login">
          Login
        </Button>
      </Toolbar>
    </AppBar>
  </Box>
);

export default Footer;
