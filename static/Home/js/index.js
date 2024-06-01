(()=>{
    console.log("Hello World")
    let VoiceRecordBtn = document.getElementById("VoiceNoteBtn");
    let NoteContent = document.getElementById("NoteContent");
    console.log(VoiceRecordBtn,NoteContent);
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.onstart = () => {
            console.log('Listening...');
            VoiceRecordBtn.innerHTML = "Stop Recording";
        };
    recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            NoteContent.value += transcript;
            console.log(transcript);
        };
    recognition.onend = () => {
        console.log('Stopped listening');
        VoiceRecordBtn.innerHTML = "Start Recording";
    };
    
    VoiceRecordBtn.addEventListener('click', () => {
        if (VoiceRecordBtn.innerHTML == "Stop Recording") {
            recognition.stop();
            VoiceRecordBtn.innerHTML = "Start Recording";
            return;
        }
        console.log("Start Recording")
        recognition.start();
    });
    }
)();
