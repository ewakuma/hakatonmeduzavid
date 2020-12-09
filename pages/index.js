

api_url = "http://localhost:5000/api/";
playlist = document.getElementById('playlist');


navigator.geolocation.getCurrentPosition(function(position) {
    let lat = position.coords.latitude;
    let lon = position.coords.longitude;
    fetch(
        api_url + "get_music/",
        {
            method: 'POST', // *GET, POST, PUT, DELETE, etc.
            body: JSON.stringify({"lat": lat, "lon": lon})
        },
    ).then((res)=>{
        return res.json();
    }).then((json)=>{
        music = json.music
        console.log(music);
        music.forEach(async element => {
            let music_block = `<div class="music">
                <h3>${element['title']}</h3>
                <audio controls>
                    <source src="${element['url']}">
                </audio>
            </div>`
            playlist.innerHTML += music_block;
        });            
    }).catch(err => {
        console.log(err);
    })

    fetch(
        `https://wft-geo-db.p.rapidapi.com/v1/geo/locations/${lat}%2B${lon}/nearbyCities?limit=1&radius=100`, 
        { 
            method: 'GET', 
            headers: new Headers({ 'x-rapidapi-key': '242f704af1msh4e0272c9beafbc6p160660jsn45c65ce74808', 'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com'}) 
        }
    ).then((res) => {
        return res.json();
    }).then((data)=>{
        let city = document.getElementById('city');
        city.innerHTML = data['data'][0]['city'];
    }).catch(err => {
        console.log(err);
    });
});