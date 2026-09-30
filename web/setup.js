import { config, newId } from "./store.js";

const panel = document.getElementById("setupPanel");

function esc(text){
    return String(text)
}

function breakRow(b, i){
        return `
            <div class="row">
                <label>After period <input type="number" data-after="${b.after}" min="1"></label>
                <label> Label <input type="text" data-label="${i}" value="${esc(b.label)}"></label>
                <label> Minutes <input type="number" data-minutes="${i}" value="${b.minutes}" min="0"></label>
                <button type="button" data-remove="${i}">Remove</button>
        `;
}

function teacherRow(t, i){
    // aaaaaaaaaaaaaaa not the html again
    return `
        <div class="row">
            <label>Name <input type="text" data-tname="${i}" value="${esc(t.name)}"> </label>
            <label>Max per day <input type="number" data-tmax="${i}" value="${t.maxPerDay}" min="0" max="20"> </label>
            <button type="button" data-remove-t="${i}">Remove</button>
        </div>
    `
}

export function renderSetup(){
    let dayBoxes = ["Mon", "Tue", "Wed", "Thu", "Fri"].map(function (d){
        let on = config.days.includes(d) ? "checked" : "";
        return `<label><input type="checkbox" data-days="${d}" ${on}> ${d}</label>`;
    }).join("");

    // aaah so much html

    panel.innerHTML = `
    <h2>School Setup</h2>

    <label>School name <input id="schoolName" value="${esc(config.school)}"> </label>

    <label>Periods per day <input type="number" id="periodsPerDay" value="${config.periodsPerDay}" min="1"> </label>

    <label>Period length (minutes) <input type="number" id="periodMinutes" value="${config.periodMinutes}" min="1"> </label>

    <h3>Teaching days </h3>
    ${dayBoxes}

    <h3>Breaks</h3>

    <div id="breakList"> ${config.breaks.map(breakRow).join("")}
        </div>

        <button type="button" id="addBreak">Add break</button>

        <h3>Teachers</h3>

        <div id="teacherList"> ${config.teachers.map(teacherRow).join("")}
        </div>

        <button type="button" id="addTeacher">Add teacher</button>
    `;

    listen();
}

// aaah boring repetitive ahh shi

function listen(){
    document.getElementById("schoolName").addEventListener("input", function (e) {
        config.school = e.target.value;
    });

    document.getElementById("periodsPerDay").addEventListener("input", function (e){
        config.periodsPerDay = Number(e.target.value);
    })

    document.getElementById("periodMinutes").addEventListener("input", function (e){
        config.periodMinutes = Number(e.target.value);
    })

    panel.querySelectorAll("[data-after]").forEach(function (input) {
        input.addEventListener("input", function (e){
            config.breaks[Number(e.target.dataset.after)].after = Number(e.target.value);
        });
    });
    
    panel.querySelectorAll("[data-label]").forEach(function (input) {
        input.addEventListener("input", function (e){
            config.breaks[Number(e.target.dataset.label)].label = e.target.value;
        })
    })

    panel.querySelectorAll("[data-minutes]").forEach(function (input) {
        input.addEventListener("input", function (e){
            config.breaks[Number(e.target.dataset.minutes)].minutes = Number(e.target.value);
        })
    })

    panel.querySelectorAll("[data-remove]").forEach(function (btn){
        btn.addEventListener("click", function (e){
            config.breaks.splice(Number(e.target.dataset.remove), 1);
            renderSetup();
        })
    })

    panel.querySelectorAll("[data-days]").forEach(function (box){
        box.addEventListener("change", function(){
            config.days = panel.querySelectorAll("[data-days]:checked")
            .map(function (c) {return c.dataset.days})
        })
    })

    document.getElementById("addBreak").addEventListener("click", function (){
        config.breaks.push({after: 1, label: "Break", minutes: 15});
        renderSetup();
    })

    panel.querySelectorAll("[data-tname]").forEach(function (input){
        input.addEventListener("input", function (e){
            config.teachers[Number(e.target.dataset.tname)].name = e.target.value;
        })
    })

    panel.querySelectorAll("[data-tmax]").forEach(function(input){
        input.addEventListener("input", function (e){
            config.teachers[Number(e.target.dataset.tmax)].maxPerDay = Number(e.target.value);
        })
    })

    panel.querySelectorAll("[data-remove-t]").forEach(function (btn){
        btn.addEventListener("click", function (e){
            config.teachers.splice(Number(e.target.dataset.removeT), 1);
            renderSetup();
        })
    })

    document.getElementById("addTeacher").addEventListener("click", function(){
        config.teachers.push({id: newId("t"), name: "", maxPerDay: 6});
        renderSetup();
    })
}
