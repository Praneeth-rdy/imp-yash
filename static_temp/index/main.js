const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const snap = document.getElementById('snap');
const submit = document.getElementById('submit');
const errorMsgElement = document.getElementById('span#ErrorMsg');


const constraints = {
    audio: false,
    video: {

    }
};

async function init() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia(constraints);
        handleSuccess(stream);
    } catch (error) {
        errorMsgElement.innerHTML = `navigator.getUserMedia.error: ${error.toString()}`;
    }
}



function handleSuccess(stream) {
    window.stream = stream;
    video.srcObject = stream;
}

init();

var context = canvas.getContext('2d');
var width = 640;
height = 480;
snap.addEventListener('click', () => {
    context.drawImage(video, 0, 0, 640, 480);
});


submit.addEventListener('click', () => {
    const data = canvas.toDataURL('image/jpeg');
    const options = {
        method: 'POST',
        body: JSON.stringify(data)
    }
    fetch('/', options)
        .then((res) => res.json())
        .then((resData) => console.log(resData))
        .catch((err)=>console.log(err));

});



