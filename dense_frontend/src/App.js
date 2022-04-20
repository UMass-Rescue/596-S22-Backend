import './App.css';
import React, {useState} from 'react';
import axios from 'axios';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import ListSubheader from '@mui/material/ListSubheader';
import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Collapse from '@mui/material/Collapse';
import Input from '@mui/material/Input';

function App() {

  const [child, setChild] = useState('');
  const [id, setID] = useState([]);
  const [caption, setCaption] = useState([]);
  const [score, setScore] = useState([]);
  const [boundingx, setBoundingx] = useState([]);
  const [boundingy, setBoundingy] = useState([]);
  const [boundingw, setBoundingw] = useState([]);
  const [boundingh, setBoundingh] = useState([]);
  const [open, setOpen] = useState(false);
  const [open2, setOpen2] = useState(false);
  const [open3, setOpen3] = useState(false);
  const [open4, setOpen4] = useState(false);
  const [open5, setOpen5] = useState(false);
  function submitGet(){
    setID([]);
    setScore([]);
    setCaption([]);
    setBoundingx([]);
    setBoundingy([]);
    setBoundingw([]);
    setBoundingh([]);
    axios
        .get('http://localhost:8000/denseCaptionGet/35/child?skip=0&limit=100')
        .then((response) => {
          setChild(JSON.stringify(response.data.children[0]));
          setID(id => [...id, JSON.stringify(response.data.children[0].id)]);
          setCaption(caption => [...caption, JSON.stringify(response.data.children[0].caption)]);
          setScore(score => [...score, JSON.stringify(response.data.children[0].score)]);
          setBoundingx(boundingx => [...boundingx, JSON.stringify(response.data.children[0].bounding_x)]);
          setBoundingy(boundingy => [...boundingy, JSON.stringify(response.data.children[0].bounding_y)]);
          setBoundingw(boundingw => [...boundingw, JSON.stringify(response.data.children[0].bounding_w)]);
          setBoundingh(boundingh => [...boundingh, JSON.stringify(response.data.children[0].bounding_h)]);
          setID(id => [...id, JSON.stringify(response.data.children[1].id)]);
          setCaption(caption => [...caption, JSON.stringify(response.data.children[1].caption)]);
          setScore(score => [...score, JSON.stringify(response.data.children[1].score)]);
          setBoundingx(boundingx => [...boundingx, JSON.stringify(response.data.children[1].bounding_x)]);
          setBoundingy(boundingy => [...boundingy, JSON.stringify(response.data.children[1].bounding_y)]);
          setBoundingw(boundingw => [...boundingw, JSON.stringify(response.data.children[1].bounding_w)]);
          setBoundingh(boundingh => [...boundingh, JSON.stringify(response.data.children[1].bounding_h)]);
          setID(id => [...id, JSON.stringify(response.data.children[2].id)]);
          setCaption(caption => [...caption, JSON.stringify(response.data.children[2].caption)]);
          setScore(score => [...score, JSON.stringify(response.data.children[2].score)]);
          setBoundingx(boundingx => [...boundingx, JSON.stringify(response.data.children[2].bounding_x)]);
          setBoundingy(boundingy => [...boundingy, JSON.stringify(response.data.children[2].bounding_y)]);
          setBoundingw(boundingw => [...boundingw, JSON.stringify(response.data.children[2].bounding_w)]);
          setBoundingh(boundingh => [...boundingh, JSON.stringify(response.data.children[2].bounding_h)]);
          setID(id => [...id, JSON.stringify(response.data.children[3].id)]);
          setCaption(caption => [...caption, JSON.stringify(response.data.children[3].caption)]);
          setScore(score => [...score, JSON.stringify(response.data.children[3].score)]);
          setBoundingx(boundingx => [...boundingx, JSON.stringify(response.data.children[3].bounding_x)]);
          setBoundingy(boundingy => [...boundingy, JSON.stringify(response.data.children[3].bounding_y)]);
          setBoundingw(boundingw => [...boundingw, JSON.stringify(response.data.children[3].bounding_w)]);
          setBoundingh(boundingh => [...boundingh, JSON.stringify(response.data.children[3].bounding_h)]);
        });
  
    };
  function handleClick1(){
    setOpen(!open);

  }
  function handleClick2(){
    setOpen2(!open2);

  }
  function handleClick3(){
    setOpen3(!open3);

  }
  function handleClick4(){
    setOpen4(!open4);

  }
  function handleClick5(){
    setOpen5(!open5);

  }

  return (
    <div className="App">
      <header className="App-header">
        <form>
          <p>
            Please Select Image
          </p>
          <Input className="App-textbox" id="file" type="file">
          </Input>
        </form>
        <br></br>

       
        <List
      sx={{ width: '100%', maxWidth: 360,}}
      className="App-textbox"
      component="nav"
      aria-labelledby="nested-list-subheader"
      
        >
          <ListItemButton onClick = {() => {handleClick1()}}>
            <ListItemText primary="Results"/>
          </ListItemButton>
          <Collapse in={open} timeout="auto" unmountOnExit>




            <List component="div" disablePadding>
              <ListItemButton onClick = {() => {handleClick2()}}>
                <ListItemText> 
                    id #: {id[0]} 
                </ListItemText>
              </ListItemButton>
              <Collapse in={open2} timeout="auto" unmountOnExit>
                <ListItemText> 
                  caption: {caption[0]} 
                </ListItemText>
                <ListItemText> 
                  score: {score[0]} 
                </ListItemText>
                <ListItemText> 
                  Bounding x: {boundingx[0]} 
                </ListItemText>
                <ListItemText> 
                  Bounding y: {boundingy[0]} 
                </ListItemText>
                <ListItemText> 
                  Bounding width: {boundingw[0]} 
                </ListItemText>
                <ListItemText> 
                  Bounding height: {boundingh[0]} 
                </ListItemText>
              </Collapse>
            </List>



            <List component="div" disablePadding>
              <ListItemButton onClick = {() => {handleClick3()}}>
                <ListItemText> 
                    id #: {id[1]} 
                </ListItemText>
              </ListItemButton>
              <Collapse in={open3} timeout="auto" unmountOnExit>
                <ListItemText> 
                  caption: {caption[1]} 
                </ListItemText>
                <ListItemText> 
                  score: {score[1]} 
                </ListItemText>
                <ListItemText> 
                  Bounding x: {boundingx[1]} 
                </ListItemText>
                <ListItemText> 
                  Bounding y: {boundingy[1]} 
                </ListItemText>
                <ListItemText> 
                  Bounding width: {boundingw[1]} 
                </ListItemText>
                <ListItemText> 
                  Bounding height: {boundingh[1]} 
                </ListItemText>
              </Collapse>
            </List>




            <List component="div" disablePadding>
              <ListItemButton onClick = {() => {handleClick4()}}>
                <ListItemText> 
                    id #: {id[2]} 
                </ListItemText>
              </ListItemButton>
              <Collapse in={open4} timeout="auto" unmountOnExit>
                <ListItemText> 
                  caption: {caption[2]} 
                </ListItemText>
                <ListItemText> 
                  score: {score[2]} 
                </ListItemText>
                <ListItemText> 
                  Bounding x: {boundingx[2]} 
                </ListItemText>
                <ListItemText> 
                  Bounding y: {boundingy[2]} 
                </ListItemText>
                <ListItemText> 
                  Bounding width: {boundingw[2]} 
                </ListItemText>
                <ListItemText> 
                  Bounding height: {boundingh[2]} 
                </ListItemText>
              </Collapse>
            </List>




            <List component="div" disablePadding>
              <ListItemButton onClick = {() => {handleClick5()}}>
                <ListItemText> 
                    id #: {id[3]} 
                </ListItemText>
              </ListItemButton>
              <Collapse in={open5} timeout="auto" unmountOnExit>
                <ListItemText> 
                  caption: {caption[3]} 
                </ListItemText>
                <ListItemText> 
                  score: {score[3]} 
                </ListItemText>
                <ListItemText> 
                  Bounding x: {boundingx[3]} 
                </ListItemText>
                <ListItemText> 
                  Bounding y: {boundingy[3]} 
                </ListItemText>
                <ListItemText> 
                  Bounding width: {boundingw[3]} 
                </ListItemText>
                <ListItemText> 
                  Bounding height: {boundingh[3]} 
                </ListItemText>
              </Collapse>
            </List>
            




          </Collapse>

        </List>

        <br></br>
        <Button variant='contained' onClick = {() => {submitGet()}}>
            Submit
        </Button>
      </header>
    </div>
  );
}

export default App;
