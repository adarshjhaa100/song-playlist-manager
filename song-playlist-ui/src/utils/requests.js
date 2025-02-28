export const getSongs = async ()=>{
    const res = await fetch("http://localhost:8000/songs/");
    const songList = await res.json();
    return songList;
}

export const getSong = async (title)=>{
    const res = await fetch(`http://localhost:8000/song/${title}/`, { method: 'GET'  });
    console.log(res);
    const song = await res.json();
    console.log(song);
    
    return song;
}




