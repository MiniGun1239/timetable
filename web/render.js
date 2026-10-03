import { config } from "./store.js"
import { schedule } from "./data.js"

const panel = document.getElementById("timetablesPanel");
let picked = "";
let view = "class";

export function renderTimetables(){
    let names = Object.keys(schedule);
    if (!picked && names.length) picked = names[0];

    let options = names.map(function (n){
        return `<option ${n === picked ? "selected" : ""}>${n}</option>`;
    }).join("");

    panel.innerHTML = `
    <h2>Timetables</h2>

    <label>View
        <select id="viewPick">
            <option value="class" ${view === "class" ? "selected" : ""}>Class timetable</option>
            <option value="teacher" ${view === "teacher" ? "selected" : ""}>Teacher timetable</option>
            <option value="all" ${view === "all" ? "selected" : ""}>All classes</option>
        </select>
    </label>

    <label id="classPicker">Class <select id="classPick">${options}</select></label>
    <button type="button" id="printTimetable">Print / Save as PDF</button>
    <div id="gridBox"></div>
    `;

    document.getElementById("classPick").addEventListener("change", function (e){
        picked = e.target.value;
        renderGrid();
    })

    document.getElementById("viewPick").addEventListener("change", function(e){
        view = e.target.value;
        showView()
    })

    document.getElementById("printTimetable").addEventListener("click", function(){
        window.print();
    })
        showView();
}

function showView(){
    let classPicker = document.getElementById("classPicker")
    let printButton = document.getElementById("printTimetable")

    if (view === "class"){
        classPicker.hidden = false;
        printButton.hidden = false;
        renderGrid();
        return;
    }

    classPicker.hidden = true;
    printButton.hidden = true;

    let message = view === "teacher" ? 
    "going to make this soon" : "going to make this soon";

    document.getElementById("gridBox").innerHTML = `<p>${message}</p>`
}

// lowk i am thinking of creating some art for this
function renderGrid(){
    let box = document.getElementById("gridBox");
    if (!picked){
        box.innerHTML = "<p>No timetable yet</p>"
        return;
    }

        box.innerHTML = grid(picked);

}

function subjectName(id){
    let found = config.subjects.find(function (s){
        return s.id === id;
    })
    return found ? found.name : id;
}

function teacherName(id){
    let found = config.teachers.find(function (t){
            return t.id === id
    })
    return found ? found.name : id;
}


    function grid(className){
        let periods = config.periodsPerDay;
        let breakAfter = {};
        config.breaks.forEach(function (b) {
            breakAfter[b.after] = b.label;
        })

        let header =  `<tr><th>Class</th>`;
        config.days.forEach(function (d){
            header += `<th>${d}</th>`;
        })

            header += "</tr>";

        let rows = "";
        for (let p = 1; p <= periods; p++){
            rows += `<tr><th>P${p}</th>`;
            config.days.forEach(function (d){
                let entry = schedule[className][`${d} P${p}`];
                let subject = entry ? subjectName(entry.subject) : "";
                let teacher = entry ? teacherName(entry.teacher) : "";
                rows += `<td><b>${subject}</b><small>${teacher}</small></td>`;

            })
            rows += "</tr>";

            if (breakAfter[p]){
              rows += `<tr class="breakRow"><td colspan="${config.days.length + 1}">${breakAfter[p]}</td></tr>`
            }
        }

        return `<table class="grid">${header}${rows}</table>`
    }
