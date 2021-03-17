import React from 'react';
import ReactDOM from 'react-dom';
import App from "./App";
import {Router} from "react-router";

// ========================================

ReactDOM.render(<Router basename={process.env.PUBLIC_URL}><App /></Router>,document.getElementById('root'));
