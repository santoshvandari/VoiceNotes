(() => {
    const VoiceRecordBtn = document.getElementById("VoiceNoteBtn");
    const NoteContent = document.getElementById("NoteContent");
    const RecordingStatus = document.getElementById("RecordingStatus");
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.interimResults = true; // Enable interim results for more responsive feedback
    recognition.continuous = true; // Continue recognition even after pauses
    let finalTranscript = ''; // Store final transcript
    let isRecognizing = false;

    recognition.onstart = () => {
        RecordingStatus.textContent = "Listening...";
        VoiceRecordBtn.innerHTML = "Stop";
        isRecognizing = true;
    };

    recognition.onresult = (event) => {
        let interimTranscript = '';
        for (let i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                finalTranscript += event.results[i][0].transcript.trim() + '. ';
            } else {
                interimTranscript += event.results[i][0].transcript;
            }
        }
        NoteContent.value = finalTranscript + interimTranscript;
    };

    recognition.onend = () => {
        RecordingStatus.textContent = "";
        VoiceRecordBtn.innerHTML = "Start";
        isRecognizing = false;
    };

    VoiceRecordBtn.addEventListener('click', () => {
        if (isRecognizing) {
            recognition.stop();
        } else {
            finalTranscript = NoteContent.value;
            recognition.start();
        }
    });
})();
