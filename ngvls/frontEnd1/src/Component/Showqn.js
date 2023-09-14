import './Form.css';
import { useState, useEffect } from 'react';



export function Showqn ()
{
    const [keyword, setKeyword] = useState('');
    const [searchContent, setSearchContent] = useState(false);
    const [output, setOutput] = useState("");

    const handleKeywordSubmit = async  (e) => {
        e.preventDefault();
        // setSearchKeyword(keyword);
        setKeyword(''); 
        setSearchContent(true)
      
    //   useEffect(()=>{
    //     qa();
    // },[searchContent]);

    // const qa = async () =>{
        try{
          const response = await fetch(`http://127.0.0.1:5000/questionanswer/${keyword}`);
          const jsonData= await response.json();
          console.log(jsonData);
          setOutput(jsonData);
    
        }
        catch(error)
        {
          console.log("Error", error);
        }
      };

    return(
    <form className='custom-form' onSubmit={handleKeywordSubmit}>
            <div className='right-section'>
            <label className='form-label'>Search Keyword</label>
            <input
                type='text'
                className='custom-input'
                placeholder='Enter your keyword'
                required
                onChange={(e) => setKeyword(e.target.value)}
                value={keyword || ''}
            />
            {keyword}
            <button type='submit' className='custom-button1'>
            Search
            </button>
            <textarea  placeholder='Result'  value = {output}/>

            </div>

        </form>
    );
}