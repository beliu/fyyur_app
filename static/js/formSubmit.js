// Submit a New Venue
function deleteVenue(e) {
    e.preventDefault();
    const venueID = e.target.dataset.venue_id;
    fetch(`/venues/${venueID}`, {
        method: 'DELETE',
        body: JSON.stringify({
            'id': venueID
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        window.location.href = '/';
    })
    .catch(function(e) {
        console.log(e);
    }

    )
}

document.getElementById('delete-venue').onsubmit = function(e) {
    deleteVenue(e);
}
