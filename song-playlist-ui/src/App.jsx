import { useState, useEffect } from 'react';
import './App.css'
import TableView from './components/TableView';
import { getSongs } from './utils/requests';

function App() {
  const [data, setData] = useState([]);

  const columns = [
    { key: "id", label: "ID", type: "string" },
    { key: "title", label: "Title", type: "string" },
    { key: "danceability", label: "Danceability", type: "number" },
    { key: "energy", label: "Energy", type: "number" },
    { key: "mode", label: "Mode", type: "number" },
    { key: "acousticness", label: "Acousticness" , type: "number"},
    { key: "tempo", label: "Tempo", type: "number" },
    { key: "duration_ms", label: "Duration(ms)", type: "number" },
    { key: "num_sections", label: "Num Sections" , type: "number"},
    { key: "num_segments", label: "Num Segments" , type: "number"},
    // { key: "star_rating", label: "Stars", },
  ];

  useEffect(()=>{
    async function fetchData(){
      const songList = await getSongs();
      console.log(songList[0]);
      setData(songList);
    }
    fetchData();
  },[]);

  return (
    <div style={{ padding: "20px" }}>
      <h3>Song Playlist</h3>
      <TableView data={data} columns={columns} />
    </div>
  );
}

export default App
