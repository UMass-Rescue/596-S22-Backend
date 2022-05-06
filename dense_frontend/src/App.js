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

var index = 0;
var index1 = 0;

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
  const [open6, setOpen6] = useState(false);
  const [open7, setOpen7] = useState(false);
  const [open8, setOpen8] = useState(false);
  const [open9, setOpen9] = useState(false);
  const [open10, setOpen10] = useState(false);

  const [imageRaw, setImageRaw] = useState(null);
  const [image, setImage] = useState(null);
  const [imageName, setImageName] = useState('');
  const [imageID, setImageID] = useState(null);
  const [inputed_name, setInputedName] = useState('');
  const [inputed_keyword, setInputedKeyword] = useState('');
  const [keywordImages, setKeywordImages] = useState([]);

  //const [index, setIndex] = useState(0);

  function handleNext(){
    //setIndex(newIndex);
    index += 4;
    submitGet();
  }

  function handlePrevious(){
    if(index != 0){
      //setIndex(newIndex);
      index -= 4;
    }
    submitGet();
  }

  function handleNext1(){
    index1 += 4;
    submitKeyword();
  }

  function handlePrevious1(){
    if(index1 != 0){
      index1 -= 4;
    }
    submitKeyword();
  }

  function submitImage(){
    var url_image = "http://localhost:8000/denseCaptionUploadImages"
    
    const formData = new FormData();
    formData.append("image", imageRaw);
    try{
      const response = axios({
        method: "post",
        url: url_image,
        data: formData,
        headers: { "Content-Type": "multipart/form-data"},
      });
    } catch(error) {
      console.log(error)
    }
  }

  function submitKeyword(){
    setKeywordImages([]);
    var url_keyword = "http://localhost:8000/denseCaptionGetimages/" + inputed_keyword

    axios
        .get(url_keyword)
        .then((response) => {
          setKeywordImages(response.data.temp);
        });
  };

  function submitGet(){
    setID([]);
    setScore([]);
    setCaption([]);
    setBoundingx([]);
    setBoundingy([]);
    setBoundingw([]);
    setBoundingh([]);
    
    var url_parent = "http://localhost:8000/denseCaptionGetParents/" + inputed_name
    
    axios
        .get(url_parent)
        .then((response) => {
          setImageID(response.data.parents[0].id);
        });
    var url_children = 'http://localhost:8000/denseCaptionGet/' + imageID + '/child'
    axios
        .get(url_children, { params: { skip: 0 } })
        .then((response) => {
          setChild(JSON.stringify(response.data.children[index]));
          setID(id => [...id, JSON.stringify(response.data.children[index].id)]);
          setCaption(caption => [...caption, JSON.stringify(response.data.children[index].caption)]);
          setScore(score => [...score, JSON.stringify(response.data.children[index].score)]);
          setBoundingx(boundingx => [...boundingx, JSON.stringify(response.data.children[index].bounding_x)]);
          setBoundingy(boundingy => [...boundingy, JSON.stringify(response.data.children[index].bounding_y)]);
          setBoundingw(boundingw => [...boundingw, JSON.stringify(response.data.children[index].bounding_w)]);
          setBoundingh(boundingh => [...boundingh, JSON.stringify(response.data.children[index].bounding_h)]);
          setID(id => [...id, JSON.stringify(response.data.children[index+1].id)]);
          setCaption(caption => [...caption, JSON.stringify(response.data.children[index+1].caption)]);
          setScore(score => [...score, JSON.stringify(response.data.children[index+1].score)]);
          setBoundingx(boundingx => [...boundingx, JSON.stringify(response.data.children[index+1].bounding_x)]);
          setBoundingy(boundingy => [...boundingy, JSON.stringify(response.data.children[index+1].bounding_y)]);
          setBoundingw(boundingw => [...boundingw, JSON.stringify(response.data.children[index+1].bounding_w)]);
          setBoundingh(boundingh => [...boundingh, JSON.stringify(response.data.children[index+1].bounding_h)]);
          setID(id => [...id, JSON.stringify(response.data.children[index+2].id)]);
          setCaption(caption => [...caption, JSON.stringify(response.data.children[index+2].caption)]);
          setScore(score => [...score, JSON.stringify(response.data.children[index+2].score)]);
          setBoundingx(boundingx => [...boundingx, JSON.stringify(response.data.children[index+2].bounding_x)]);
          setBoundingy(boundingy => [...boundingy, JSON.stringify(response.data.children[index+2].bounding_y)]);
          setBoundingw(boundingw => [...boundingw, JSON.stringify(response.data.children[index+2].bounding_w)]);
          setBoundingh(boundingh => [...boundingh, JSON.stringify(response.data.children[index+2].bounding_h)]);
          setID(id => [...id, JSON.stringify(response.data.children[index+3].id)]);
          setCaption(caption => [...caption, JSON.stringify(response.data.children[index+3].caption)]);
          setScore(score => [...score, JSON.stringify(response.data.children[index+3].score)]);
          setBoundingx(boundingx => [...boundingx, JSON.stringify(response.data.children[index+3].bounding_x)]);
          setBoundingy(boundingy => [...boundingy, JSON.stringify(response.data.children[index+3].bounding_y)]);
          setBoundingw(boundingw => [...boundingw, JSON.stringify(response.data.children[index+3].bounding_w)]);
          setBoundingh(boundingh => [...boundingh, JSON.stringify(response.data.children[index+3].bounding_h)]);
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

  function handleClick6(){
    setOpen6(!open6);

  }
  function handleClick7(){
    setOpen7(!open7);

  }
  function handleClick8(){
    setOpen8(!open8);

  }
  function handleClick9(){
    setOpen9(!open9);

  }
  function handleClick10(){
    setOpen10(!open10);

  }

  
  const onChangeImage = e => {
    setImage(null);
    setImageName('');
    if (e.target.files[0]){
      setImageRaw(e.target.files[0]);
      setImage(URL.createObjectURL(e.target.files[0]));
      console.log('image: ', image);
      console.log('files: ', e.target.files);
      setImageName(e.target.files[0].name);
    }

  };


  return (
    <div className="App">
      <header className="App-header">
        <form>
          <p>
            Image Upload:
          </p>
          <img src={image} width="300" hieght="300" ></img>
          <br/>
          <Input className="App-textbox" id="image_upload" type="file" onChange={onChangeImage}>
          </Input>
        </form>
        <Button variant='contained' onClick = {() => {submitImage()}}>
            Submit
        </Button>
        <br/>
        <br/>
        <p>
            Image Search (by name):
        </p>
        
        <TextField className="App-textbox" id="inputed_name" label="Image name" variant="standard" onChange={event => setInputedName(event.target.value)}></TextField>
        <Button variant='contained' onClick = {() => {submitGet()}}>
            Submit
        </Button>
        <br/>
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
                  caption: {caption[0]}
                </ListItemText>
              </ListItemButton>
              <Collapse in={open2} timeout="auto" unmountOnExit>
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
                  caption: {caption[1]} 
                </ListItemText>
              </ListItemButton>
              <Collapse in={open3} timeout="auto" unmountOnExit>
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
                  caption: {caption[2]} 
                </ListItemText>
              </ListItemButton>
              <Collapse in={open4} timeout="auto" unmountOnExit>
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
                  caption: {caption[3]} 
                </ListItemText>
              </ListItemButton>
              <Collapse in={open5} timeout="auto" unmountOnExit>
                
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
        <div class='buttons'>
          <div class ='action_btn'>
            <Button variant='contained' onClick = {() => {handlePrevious()}}>
              Previous
            </Button>
            
            <Button variant='contained' onClick = {() => {handleNext()}}>
              Next
            </Button>
          </div>
        </div>
        
        
        <br/>
        <br/>
        <p>
            Keyword Search:
        </p>
        
        <TextField className="App-textbox" id="inputed_name" label="Keyword" variant="standard" onChange={event => setInputedKeyword(event.target.value)}></TextField>
        <Button variant='contained' onClick = {() => {submitKeyword()}}>
            Submit
        </Button>
        
        <br/>

        <List
      sx={{ width: '100%', maxWidth: 360,}}
      className="App-textbox"
      component="nav"
      aria-labelledby="nested-list-subheader"
      
        >
          <ListItemButton onClick = {() => {handleClick6()}}>
            <ListItemText primary="Results"/>
          </ListItemButton>
          <Collapse in={open6} timeout="auto" unmountOnExit>
            <ListItemText> 
                {index1+1}: {keywordImages[index1]} 
            </ListItemText>
            <ListItemText> 
                {index1+2}: {keywordImages[index1+1]} 
            </ListItemText>
            <ListItemText> 
                {index1+3}:{keywordImages[index1+2]} 
            </ListItemText>
            <ListItemText> 
                {index1+4}:{keywordImages[index1+3]} 
            </ListItemText>

          </Collapse>

        </List>
        <div class='buttons'>
          <div class ='action_btn'>
            <Button variant='contained' onClick = {() => {handlePrevious1()}}>
              Previous
            </Button>
            
            <Button variant='contained' onClick = {() => {handleNext1()}}>
              Next
            </Button>
          </div>
        </div>
        <br/>
        <br/>

      </header>
    </div>
  );
}

export default App;
