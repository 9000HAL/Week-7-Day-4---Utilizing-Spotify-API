// spotify API creds


// getToken function

////////////////////////see main.js ------------------------


// verify that we get our token
// getToken()

// use getToken function, to get a song



// getSong Function
const getSong = async (track, artist) => {
    const token = await getToken()
    const response = await fetch(` `)



}

// verify that we get the song data
// ============= getSong('Golden Hour', 'JVKE')




// clickedSong function

const clickedSong = async (divId) => {
   //get all tracks first
   const allTracks = document.getElementsByClassName              

//get all artists
const allArtists = 
//get specific artist
const artist = allArtists[divId.slice(-1)].innerText


const song = await getSong(track, artist)
console.log(song)

playSong(song)

}


let audio = ''
// handles playing the audio
const playSong = (url) => {
    if (audio)

}

// handles pausing the audio

