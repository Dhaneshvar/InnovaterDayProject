import React, { useEffect, useState } from 'react'
import {LocalVideo} from './LocalVideo';

export const Translate = ({youtubeLink}) => {

    const [lin, setlin] = useState(youtubeLink);
    const [output, setOutput] = useState("");
    // useEffect(()=>
    // {
    //     tra();
    // },[]);

    // const tra = async () =>{
    //     try{
    //       const response = await fetch(`http://127.0.0.1:5000/convertYtFinalOutput/${lin}`);
    //       const jsonData= await response.json();
    //       console.log(jsonData);
    //       setOutput(jsonData);
    
    //     }
    //     catch(error)
    //     {
    //       console.log("Error", error);
    //     }
    // }
  return (
    <div>
    {/* {output} */}
    {output === "" ? (<LocalVideo></LocalVideo>):""}
    </div>
  )
}
