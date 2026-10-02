import { config, newId, saveConfig } from "./store.js";

const panel = document.getElementById("setupPanel");

panel.addEventListener("input", saveConfig);
panel.addEventListener("change", saveConfig);
panel.addEventListener("click", saveConfig);

function esc(text){
    return String(text)
}

function breakRow(b, i){
        return `
            <div class="row">
                <label>After period <input type="number" data-after="${i}" value="${b.after}" min="1"></label>
                <label> Label <input type="text" data-label="${i}" value="${esc(b.label)}"></label>
                <label> Minutes <input type="number" data-minutes="${i}" value="${b.minutes}" min="0"></label>
                <button type="button" data-remove="${i}">Remove</button>
                </div>
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

function subjectRow(s, i){
    return `
        <div class="row">
            <label>Name <input type="text" data-sname="${i}" value="${esc(s.name)}"> </label>
            <label><input type="checkbox" data-snobb="${i}" ${s.noBackToBack ? "checked" : ""}> No back to back</label>
            <button type="button" data-remove-s="${i}">Remove</button>
            </div>
    `
}

function gradeBlock(g, gi){
    let section = g.sections.map(function (name, si){
        return `
            <div class="row">
                <label>Section <input type="text" data-sec="${gi}" data-si="${si}" value="${esc(name)}"> </label>
                <button type="button" data-remove-sec="${gi}" data-si="${si}">Remove</button>
            </div>`;
    }).join("");

    return `
        <div class="block">
            <div class="row">
            <label>Grade <input type="text" data-gname="${gi}" value="${esc(g.name)}"></label>
            <button type="button" data-add-sec="${gi}">Add section</button>
             <button type="button" data-remove-g="${gi}">Remove grade</button>
             </div>
             <div class="rows">${section}</div>
        </div>`;
}

export function renderSetup(){
    let dayBoxes = ["Mon", "Tue", "Wed", "Thu", "Fri"].map(function (d){
        let on = config.days.includes(d) ? "checked" : "";
        return `<label><input type="checkbox" data-days="${d}" ${on}> ${d}</label>`;
    }).join("");

    // aaah so much htmls

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

        <h3>Subjects</h3>

        <div id="subjectList"> ${config.subjects.map(subjectRow).join("")}
        </div>

        <button type="button" id="addSubject">Add subject</button>

        <h3>Grades and Sections</h3>

        <div id="gradeList"> ${config.grades.map(gradeBlock).join("")}
        </div>

        <button type="button" id="addGrade">Add grade</button>

        <button type="button" id="checkSetup">Check setup</button>
        <p id="setupMessage"></p>
    `;

    listen();
}

// aaah boring repetitive ahh shi

// so i aint changing it
//aaaaaaaaaaaa
// i dont want to throw all those efforts to waste
// im js gonna copy paste a million time
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
            config.days = Array.from(
                panel.querySelectorAll("[data-days]:checked")).map(function (c){
                    return c.dataset.days;
                }
            )
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
    // omfg there must be some way of not writing all this 
    panel.querySelectorAll("[data-sname]").forEach(function (input){
        input.addEventListener("input", function (e){
        config.subjects[Number(e.target.dataset.sname)].name = e.target.value;
        })
    })

    panel.querySelectorAll("[data-snobb]").forEach(function (box){
        box.addEventListener("change", function (e){
        config.subjects[Number(e.target.dataset.snobb)].noBackToBack = e.target.checked;
        })
    })

    panel.querySelectorAll("[data-remove-s]").forEach(function(btn){
        btn.addEventListener("click", function (e){
        config.subjects.splice(Number(e.target.dataset.removeS), 1);
        renderSetup();
        })
    })

    document.getElementById("addSubject").addEventListener("click", function(){
        config.subjects.push({id: newId("s"), name: "", noBackToBack: false});
        renderSetup();
        })

    panel.querySelectorAll("[data-gname]").forEach(function (input){
        input.addEventListener("input", function (e){
            config.grades[Number(e.target.dataset.gname)].name = e.target.value;
        })
    })

    panel.querySelectorAll("[data-sec]").forEach(function (input){
        input.addEventListener("input", function(e){
            let gi = Number(e.target.dataset.sec);
            let si = Number(e.target.dataset.si);
            config.grades[gi].sections[si] = e.target.value;
        })
    })

    panel.querySelectorAll("[data-add-sec]").forEach(function (btn){
        btn.addEventListener("click", function (e){
            config.grades[Number(e.target.dataset.addSec)].sections.push("");
            renderSetup();
        })
    })

    panel.querySelectorAll("[data-remove-sec]").forEach(function (btn){
        btn.addEventListener("click", function (e){
            let gi = Number(e.target.dataset.removeSec);
            let si = Number(e.target.dataset.si);
            config.grades[gi].sections.splice(si, 1);
            renderSetup();
        })
    })

    panel.querySelectorAll("[data-remove-g]").forEach(function(btn){
        btn.addEventListener("click", function(e){
            config.grades.splice(Number(e.target.dataset.removeG), 1);
            renderSetup();
        })
    })

    // aaaah im lowk so bored of this shi
    document.getElementById("addGrade").addEventListener("click", function (){
        config.grades.push({ id: newId("g"), name: "", sections: [] });
        renderSetup();
    })

    // oh non on oon nnono nnot this again aaaaahaaaa

    document.getElementById("checkSetup").addEventListener("click", function (){
        let errors = [];

        if (!config.school.trim()){
            errors.push("Enter a school name")
        }

        if (!Number.isInteger(config.periodsPerDay) || config.periodsPerDay < 1){
            errors.push("Periods per day must be a positive whole number")
        }

        if (!Number.isInteger(config.periodMinutes) || config.periodMinutes < 1){
            errors.push("Period length must be a positive number")
        }

        if (config.days.length === 0){
            errors.push("Choose atleast one teaching day")
        }

        config.breaks.forEach(function(breakItem){
            if(breakItem.after < 1 || breakItem.after > config.periodsPerDay){
                errors.push("Each break must be after a period")
            }
        });

        let message = document.getElementById("setupMessage");

        if(errors.length){
            message.textContent = errors.join(" ");
        }

        else {
            message.textContent = "Setup looks good";
        }
    })
}
