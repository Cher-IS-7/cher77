if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({
        video: true
    })
    .then(function(stream) {
        const video = document.getElementById('you');
        video.srcObject = stream
    })
    .catch(function(error) {
        console.error("Can't access camera")
    });
}   else {
    console.error("User media not supported")
}
