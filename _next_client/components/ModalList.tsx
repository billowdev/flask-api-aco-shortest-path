import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Modal, Backdrop, Fade, List, ListItem, ListItemText } from '@material-ui/core';

type Props = {
  open: boolean;
  onClose: () => void;
  nodes: string[];
  onSelect: (node: string) => void;
};

const useStyles = makeStyles((theme) => ({
  modal: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  paper: {
    backgroundColor: theme.palette.background.paper,
    borderRadius: '4px',
    boxShadow: theme.shadows[5],
    padding: theme.spacing(2, 4, 3),
  },
}));

function ModalList({ open, onClose, nodes, onSelect }: Props) {
  const classes = useStyles();

  const handleListItemClick = (node: string) => {
    onSelect(node);
    onClose();
  };

  return (
    <Modal
      className={classes.modal}
      open={open}
      onClose={onClose}
      closeAfterTransition
      BackdropComponent={Backdrop}
      BackdropProps={{
        timeout: 500,
      }}
    >
      <Fade in={open}>
        <div className={classes.paper}>
          <h2>Select a node</h2>
          <List component="nav">
            {nodes.map((node, index) => (
              <ListItem button key={index} onClick={() => handleListItemClick(node)}>
                <ListItemText primary={node} />
              </ListItem>
            ))}
          </List>
        </div>
      </Fade>
    </Modal>
  );
}

export default ModalList;
