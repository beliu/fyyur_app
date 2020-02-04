// Submit a New Venue
function addVenue(e) {
    e.preventDefault();
    // console.log(e);
    // fetch('/venues/create', {
    //     method: 'POST',
    //     body: JSON.stringify({
    //         'venueName': 'Test'
    //     }),
    //     headers: {
    //         'Content-Type': 'application/json'
    //     }
    // })
    // .then(response => {
    //     return response.json()
    // }) 
}

document.getElementById('new-venue-form').onsubmit = function(e) {
    addVenue(e);
}
