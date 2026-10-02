import { renderSetup } from "./setup.js";
import { renderTimetables } from "./render.js";

renderSetup();
renderTimetables();

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