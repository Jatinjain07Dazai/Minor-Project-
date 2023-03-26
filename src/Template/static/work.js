const dropArea = document.querySelector(".drag-area"),
dragText = dropArea.querySelector("header"),
button = dropArea.querySelector("button"),
input = dropArea.querySelector("input"),
submit = document.querySelector("#jick"),
textbox = dropArea.querySelector("textarea");
let file; 


button.onclick = ()=>{
  if(textbox.value == "")
    input.click();
  else{
    console.log("sick")
    submit.click();
  } 
}

input.addEventListener("change", function(){
  file = this.files[0];
  dropArea.classList.add("active");
  showFile(); 
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



function showFile(){
  let fileType = file.type; 
  console.log(fileType)
  let validExtensions = ["text/plain", "application/msword"]; 
  if(validExtensions.includes(fileType)){ 
    submit.click()

    
  }else{
    alert("This is not an proper File!");
    dropArea.classList.remove("active");
    dragText.textContent = "Drag & Drop to Upload File";
  }
}