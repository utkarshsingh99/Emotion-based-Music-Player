// const tracksTemplateSource = document.getElementById('tracks-template').innerHTML;
$(document).ready(function () {
    const data = $('#song')
    var value = data.text();
    playSong(value)
})

$('#unlike').on('click', (e) => {
    let user_id = $('#user_id').text()
    let song_id = $('#song_id').text()
    let mood = $('#mood').text()
    $.post('/unlike', {user_id, song_id, mood}, (response) => {
        console.log(response)
        if(response != '' && response != undefined && response != null) {
            let songname = response;
            playSong(songname)
            $('#song').text(songname)
            $('#anotherSongName').text(songname)
        }
    })
})

const playSong = (value) => {
    if(value == undefined || value == '' || value == null)
        return ;
    value = value.trim()
    value = value.replace(new RegExp(' ', 'g'), '%20')
    const getTopTracks = $.get('https://api.napster.com/v2.2/search?apikey=YTE3NWVjMzEtMzJlNy00MTFhLWJmNjEtMjMxMmFhOGIyNDVk&type=track&query=' + value);

    getTopTracks.then((response) => {
            var track = response.search.data.tracks[0]
            console.log(track)
            var string = `
                <div data-track-id="${track.albumId}" style="background-image:url(http://direct.rhapsody.com/imageserver/v2/albums/${track.albumId}/images/300x300.jpg)" class="cover">
                <div class=content-name>${track.name}</div>
                <audio controls class= "audio" autoplay>
                <source src="${track.previewURL}" type="audio/mpeg">
                </audio>
                </div>
                `
            $('#tracks-container').html(string);
        });
} 