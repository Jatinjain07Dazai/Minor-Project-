const dropArea = document.querySelector(".drag-area"),
dragText = dropArea.querySelector("header"),
button = dropArea.querySelector("button"),
textbox = dropArea.querySelector("textarea"),
input = dropArea.querySelector("input[type=file]"),
submit = dropArea.querySelector("input[type=submit]"),
but1 = dropArea.querySelector(".upl"),
b = document.querySelector("body");
let file; 


b.addEventListener('click', () =>{
  if(!textbox.value){
    button.innerHTML = "Upload Files";
  }
});


input.addEventListener("change", handleFileSelect, false /*function(){
  file = this.files[0];
  dropArea.classList.add("active");
  showFile(); 
}*/);



but1.addEventListener('click', () => {
  if(!textbox.value){
    input.click();
  }
});


textbox.addEventListener("input", () =>{
  button.innerHTML = "Submit"
});


dropArea.addEventListener("dragover", (event)=>{
  event.preventDefault(); 
  dropArea.classList.add("active");
  dragText.textContent = "Release to Upload File";
});


dropArea.addEventListener("dragleave", (event)=>{
  event.preventDefault();
  dropArea.classList.remove("active");
  dragText.textContent = "Drag here to Upload File";
});


dropArea.addEventListener("drop", (event)=>{
  event.preventDefault();
  file = event.dataTransfer.files[0];
  showFile(); 
});



function handleFileSelect(evt) {
    let files = evt.target.files; // FileList object

    // use the 1st file from the list
    let f = files[0];
    
    let reader = new FileReader();

    // Closure to capture the file information.
    reader.onload = (function(theFile) {
        return function(e) {
          
        console.log(e.target.result)
        textbox.value = val(e.target.result);
        };
      })(f);

      // Read in the image file as a data URL.
      reader.readAsText(f);
  }


function showFile(){
  let fileType = file.type; 
  console.log(fileType)
  let validExtensions = ["text/plain", "application/msword"]; 
  if(validExtensions.includes(fileType)){ 
    dragText.innerHTML = "Your file is of valid formate and ready to be scaned"
    button.innerHTML = "Submit"
  
  }else{
    alert("This is not an proper File!");
    dropArea.classList.remove("active");
    dragText.textContent = "Drag & Drop to Upload File";
  }
}