// let saveNoteBtn=document.getElementById('SaveNoteBtn');
// let noteTitle=document.getElementById('NoteTitle');
// let noteContent=document.getElementById('NoteContent');
// console.log("Hello")
// saveNoteBtn.addEventListener('click',function(){
//     let title=noteTitle.value;
//     let content=noteContent.value;
//     console.log(title,content);
//     // make the post request to /
//     fetch('/save-note',{
//         method:'POST',
//         headers:{
//             'Content-Type':'application/json'
//         },
//         body:JSON.stringify({
//             title:title,
//             content:content
//         })
//     }).then((response)=>{
//         return response.json();
//     }).then((data)=>{
//         console.log(data);
//         if(data.status=='success'){
//             alert('Note Saved Successfully');
//             noteTitle.value='';
//             noteContent.value='';
//         }
//     })
    
// })

var speech = true; 
        window.SpeechRecognition = window.SpeechRecognition 
                        || window.webkitSpeechRecognition; 
  
        const recognition = new SpeechRecognition(); 
        recognition.interimResults = true; 
        // const words = document.querySelector('.words'); 
        // words.appendChild(p); 
        // console.log(p)
  
        recognition.addEventListener('result', e => { 
            const transcript = Array.from(e.results) 
                .map(result => result[0]) 
                .map(result => result.transcript) 
                .join('') 
  
            // document.getElementById("p").innerHTML = transcript; 
            console.log(transcript); 
        }); 
          
        if (speech == true) { 
            recognition.start(); 
            recognition.addEventListener('end', recognition.start); 
        } 