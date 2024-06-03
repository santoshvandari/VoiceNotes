(()=>{
    let VoiceRecordBtn = document.getElementById("VoiceNoteBtn");
    let NoteTitle=document.getElementById("NoteTitle");
    let NoteContent = document.getElementById("NoteContent");
    let RecordingStatus = document.getElementById("RecordingStatus");
    let SaveNoteBtn = document.getElementById("SaveNoteBtn");
    let ErrorOpt=document.querySelector("div.error p");
    console.log(VoiceRecordBtn,NoteContent);
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.onstart = () => {
            console.log('Listening...');
            RecordingStatus.textContent= "Listening...";
            VoiceRecordBtn.innerHTML = "Stop";
        };
    recognition.onresult = (event) => {
            console.log("Hello World")
            const transcript = event.results[0][0].transcript;
            NoteContent.value += transcript;
            console.log(transcript);
        };
    recognition.onend = () => {
        console.log('Stopped listening');
        RecordingStatus.textContent= "";
        VoiceRecordBtn.innerHTML = "Start";
    };
    
    VoiceRecordBtn.addEventListener('click', () => {
        if (VoiceRecordBtn.innerHTML == "Stop") {
            recognition.stop();
            RecordingStatus.textContent= "";
            VoiceRecordBtn.innerHTML = "Start";
            return;
        }
        console.log("Start")
        recognition.start();
    });
    let SaveNotes=()=>{
        SaveNoteBtn.addEventListener('click',(e)=>{
            e.preventDefault();
            let Title = NoteTitle.value;
            let Content = NoteContent.value;
            if(Title=="" || Content==""){
                ErrorOpt.textContent="* Please Fill the Title and Content";
                return;
            }
            e.submit();
        });
    }
    SaveNotes();

    }
)();
