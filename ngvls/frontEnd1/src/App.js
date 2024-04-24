// App.js

import { useState } from 'react';
import { Form } from './Component/Form';
import { Youtube } from './Component/Youtube';
import './Component/Form.css';
import {Showqn} from './Component/Showqn';
 

function App() {
  const [youtubeLink, setYoutubeLink]=useState(null);
  const [input, setInput] = useState('');
  const [selectedLanguage, setSelectedLanguage] = useState('English');
  const [keyword, setKeyword] = useState('');

  const handleVideoSubmit = (e) => {
    e.preventDefault();
    setYoutubeLink(input);
    setInput('');
  };

  const handleLanguageChange = (e) => {
    setSelectedLanguage(e.target.value);
    // You can perform actions based on the selected language here
  };

  // Handle submit Here
  return (
    <div className="container">
      <Form setYoutubeLink={setYoutubeLink} />
      <br></br>
      <Youtube youtubeLink={youtubeLink}/>
      {/* <h1>Here ok</h1> */}
      <div className='form-container'> 
      <Notes/>
      {/* Here */}
      <Showqn></Showqn>
      </div>
    </div>
  );
}

export default App;



function Notes() {
  const [notes, setNotes] = useState(''); // State for notes
  const handleNotesChange = (e) => {
    setNotes(e.target.value);
  };

  // Function to download notes as a text file
  const downloadNotes = () => {
    const element = document.createElement("a");
    const file = new Blob([notes], { type: 'text/plain' });
    element.href = URL.createObjectURL(file);
    element.download = "notes.txt";
    document.body.appendChild(element);
    element.click();
  };

  return <div className='notes-section'>
  <h1>Notes</h1>
  <textarea
  rows={10}
  cols={80}
    className='custom-textarea'
    placeholder='Enter your notes here'
    onChange={handleNotesChange}
    value={notes}
  />
  <button onClick={downloadNotes} className='custom-button2'>
    Download
  </button>
</div>
}