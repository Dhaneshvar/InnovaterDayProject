// Form.js

import React, { useState } from 'react';
import './Form.css';

export const Form = ({ setYoutubeLink, setSearchKeyword }) => {
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

  const handleKeywordSubmit = (e) => {
    e.preventDefault();
    setSearchKeyword(keyword);
    setKeyword('');
  };

  // Function to handle notes input
  
  return (
    <div className="form-container">
      <form className='custom-form' onSubmit={handleVideoSubmit}>
        <div className='left-section'>
          <div className='input-with-dropdown' style={{gap:"10em"}}>
          <label className='form-label'>Video Link</label>
            <input
              type='text'
              className='custom-input'
              required
              placeholder='Enter your Youtube Link'
              onChange={(e) => setInput(e.target.value)}
              value={input || ''}
            />
            <div className='language-dropdown'>
              <label className='form-label'>Language</label>
              <select
                value={selectedLanguage}
                onChange={handleLanguageChange}
                className='custom-input'
              >
                <option value='English'>English</option>
                <option value='Spanish'>Spanish</option>
                <option value='French'>French</option>
                {/* Add more language options */}
              </select>
            </div>
        <button type='submit' className='custom-button'>
          Play
        </button>
          </div>
        </div>

      </form>

      {/* Right-side form for searching a keyword */}
      

      {/* Textarea for notes */}
      {/* <div className='notes-container'>
        <label className='form-label'>Notes</label>
        <textarea
          className='custom-textarea'
          placeholder='Enter your notes here'
          onChange={handleNotesChange}
          value={notes}
        />
        <button onClick={downloadNotes} className='custom-button2'>
          Download Notes
        </button>
      </div> */}
    </div>
  );
};
