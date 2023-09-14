// index.js or App.js

import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'; // Include your main application's CSS
import App from './App'; // Import your App component
 // Include the YoutubeVideoPlayer component's CSS

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

