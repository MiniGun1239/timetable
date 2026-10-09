import { displayGeneratedSchedule, renderTimetables } from "./render.js";
import {config} from "./store.js"
import { renderSetup } from "./setup.js";

renderSetup();
renderTimetables();

// the generate page now

let generatePanel = document.getElementById("generatePanel");

// aaaaaaaaaaaah not this shi
generatePanel.innerHTML = `
    <h2>Generate timetable</h2>
    <button id="makeTimetable">Generate</button>
    <p id="generateMessage"></p>
`;

document.getElementById("makeTimetable").addEventListener("click", async function() {
    let message = document.getElementById("generateMessage");
    message.textContent = "wait a sec"


//lowk i could have used node js 
// but python se yeahhh
try {
    let response = await fetch("/api/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json"},
        body: JSON.stringify(config)
    })

    if (!response.ok){
        throw new Error("Something's wrong with the server")
    }

    let schedule = await response.json();
    displayGeneratedSchedule(schedule);
    message.textContent = "Worked! Open timetables to see it"
}

catch (error){
    message.textContent = error.message;
}
});


const tabNames = ["setup", "generate", "timetables"];

// holy functions
tabNames.forEach(function(name){
    let button = document.getElementById(name);
    let panel = document.getElementById(name + "Panel");

    button.addEventListener("click", function (){
        tabNames.forEach(function (other){
            document.getElementById(other).classList.remove("active");
            document.getElementById(other + "Panel").classList.remove("active");
        });
        button.classList.add("active");
        panel.classList.add("active");

        if (name === "timetables"){
            renderTimetables();
        }
    })
}) 