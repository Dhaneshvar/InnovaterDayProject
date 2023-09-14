import React from "react";
import ReactPlayer from 'react-player/youtube'
import { useState } from "react";
import {Translate} from "./Translate"

export const Youtube=({youtubeLink})=>{

    const [enableTranslate, setEnableTranslate] = useState(false);
    const setTrans = () =>
    {
        setEnableTranslate(true);
    }
    return(
        <div className="yt-section">

        <ReactPlayer url={youtubeLink} controls={true}
        width="800px"
        height="450px"  />
            <br></br>
        <button onClick={setTrans} style={{height:100, width:200, borderRadius:40, paddingRight:'2rem'}}>Start Translate</button>
        { enableTranslate ? <Translate youtubeLink = {youtubeLink}></Translate> : ""}
        </div>
    )
}