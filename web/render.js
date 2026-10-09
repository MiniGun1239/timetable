import { config } from "./store.js"
import { schedule, setSchedule } from "./data.js"

const panel = document.getElementById("timetablesPanel");
let picked = "";
let view = "class";
let pickedTeacher = "";
let teacherIds = [];
let substituteDay = "";
let absentTeacher = "";
let substituteChoices = {};

export function displayGeneratedSchedule(scheduleData){
    setSchedule(scheduleData);
    picked = "";
    pickedTeacher = "";
    renderTimetables();
}

export function renderTimetables(){
    let names = Object.keys(schedule);
    if (!picked && names.length) picked = names[0];

    let options = names.map(function (n){
        return `<option ${n === picked ? "selected" : ""}>${n}</option>`;
    }).join("");

     teacherIds = config.teachers.map(function(teacher){
        return teacher.id;
     })

    Object.keys(schedule).forEach(function (className){
        Object.values(schedule[className]).forEach(function(entry){
            if (entry && !teacherIds.includes(entry.teacher)){
                teacherIds.push(entry.teacher);
            }
        })
    })

    if(!pickedTeacher && teacherIds.length){
        pickedTeacher =teacherIds[0];
    }

    let teacherOptions = teacherIds.map(function(id){
return `<option value="${id}" ${id === pickedTeacher ? "selected" : ""}>${teacherName(id)}</option>`;    
    }).join("");

let dayOptions = config.days.map(function(day){
    return `<option value="${day}">${day}</option>`;
}).join("");

let periodOptions = "";

for (let p = 1; p <= config.periodsPerDay; p++){
    periodOptions += `<option value="${p}">P${p}</option>`
}

    panel.innerHTML = `
    <h2>Timetables</h2>
    <label>View
        <select id="viewPick">
            <option value="class" ${view === "class" ? "selected" : ""}>Class timetable</option>
            <option value="teacher" ${view === "teacher" ? "selected" : ""}>Teacher timetable</option>
            <option value="workload" ${view === "workload" ? "selected" : ""}>Teacher workload</option>
            <option value="all" ${view === "all" ? "selected" : ""}>All classes</option>
            <option value="substitutions" ${view == "substitutions" ? "selected" : ""}>Substitution planner</option> 
        </select>
    </label>

    <label id="classPicker">Class <select id="classPick">${options}</select></label>
    <label id="teacherPicker" hidden> Teacher <select id="teacherPick">${teacherOptions}</select></label>
<section class="freeTeacherFinder">
    <h3>Find a free teacher</h3>
    <p>Choose a day and period to see which teachers are available :D</p>
    <div class="freeTeacherControls">
        <label>Day <select id="freeDay">${dayOptions}</select></label>
        <label>Period <select id="freePeriod">${periodOptions}</select></label>
    </div>
    <div id="freeResults" aria-live="polite"></div>
</section>
    <section>
        <h3>Teacher conflict check</h3>
        <div id="conflictResults"></div>
    </section>
        <button type="button" id="printTimetable">Print / Save as PDF</button>
        <button type="button" id="downloadJson">Download JSON</button>
        <div id="gridBox"></div>
    `;

    document.getElementById("classPick").addEventListener("change", function (e){
        picked = e.target.value;
        renderGrid();
    })

    document.getElementById("teacherPick").addEventListener("change", function (e){
        pickedTeacher = e.target.value;
        renderTeacherGrid();
    })

    document.getElementById("freeDay").addEventListener("change", renderFreeTeachers);
    document.getElementById("freePeriod").addEventListener("change", renderFreeTeachers);

    document.getElementById("viewPick").addEventListener("change", function(e){
        view = e.target.value;
        showView()
    })

    document.getElementById("printTimetable").addEventListener("click", function(){
        window.print();
    })

    document.getElementById("downloadJson").addEventListener("click", function(){
        let file = new Blob([JSON.stringify(schedule, null, 2)], {
            type: "application/json"
        })

        let link = document.createElement("a");
        link.href = URL.createObjectURL(file);
        link.download = "timetable.json"
        link.click();
    })

        renderFreeTeachers()
        renderConflicts()
        showView();
}

function showView(){
    let classPicker = document.getElementById("classPicker")
    let teacherPicker = document.getElementById("teacherPicker")
    let printButton = document.getElementById("printTimetable")

    classPicker.hidden = view !== "class";
    teacherPicker.hidden = view !== "teacher";
    printButton.hidden = view === "all" || view === "workload";

    if (view === "class"){
        renderGrid();
    }
    else if (view === "teacher"){
        renderTeacherGrid();
    }
    else if (view === "workload"){
    renderWorkload();
    }
    else if (view === "substitutions"){
        renderSubstitutionPlanner()
    }
    else {
             renderAllClasses();
    }
}

function renderAllClasses(){
    let box = document.getElementById("gridBox")
    let classNames = Object.keys(schedule)

    if (classNames.length === 0){
        box.innerHTML = "<p>No timetables yet</p>"
        return
    }

    box.innerHTML = classNames.map(function(className){
        return `<h3>${className}</h3>${grid(className)}`;
    }).join("");

}
// lowk i am thinking of creating some art for this
function renderGrid(){
    let box = document.getElementById("gridBox");
    if (!picked){
        box.innerHTML = "<p>No timetable yet</p>"
        return;
    }
        box.innerHTML = "<p>Click a timetable cell to edit it</p>" + grid(picked);

        box.querySelectorAll(".editCell").forEach(function(cell){
            cell.addEventListener("click", function(){
                let slot = cell.dataset.slot;
                let current = schedule[picked][slot] || { subject: "", teacher: ""};

                let subject = prompt("Enter subject ID:", current.subject);
                if (subject == null) return;

                let teacher = prompt("Enter teacher ID:", current.teacher);
                if (teacher == null) return;
                
                if (!subject.trim() || !teacher.trim()){
                    alert("Enter subject ID and a teacher ID")
                    return;
                }
                schedule[picked][slot] = {
                    subject: subject.trim(),
                    teacher: teacher.trim()
                }
                renderTimetables();
            })
        })
}

function renderTeacherGrid(){
    let box = document.getElementById("gridBox")

    if(!pickedTeacher){
        box.innerHTML = "<p>No teachers found in the schedule</p>"
        return;
    }
    box.innerHTML = teacherGrid(pickedTeacher)
}

function renderFreeTeachers(){
    let box = document.getElementById("freeResults");
    let day = document.getElementById("freeDay").value;
    let period = document.getElementById("freePeriod").value;
    let slot = `${day} P${period}`;
    let busyTeachers = [];

    Object.keys(schedule).forEach(function(className){
        let entry= schedule[className][slot];

        if (entry && !busyTeachers.includes(entry.teacher)){
            busyTeachers.push(entry.teacher);
        }
    })

    let freeTeachers = teacherIds.filter(function(id){
        return !busyTeachers.includes(id);
    })

    if (freeTeachers.length === 0){
        box.innerHTML = `<p>No free teachers on ${day}, P${period}</p>`
        return;
    }

    let names = freeTeachers.map(function(id){
        return `<li>${teacherName(id)}</li>`
    }).join("");

    box.innerHTML = `<h3>Free teachers on ${day}, P${period}</h3><ul>${names}</ul>`
}

// idk how is this gonna work aaah

function renderSubstitutionPlanner(){
    let box = document.getElementById("gridBox");

    if (!config.days.length || !teacherIds.length){
        box.innerHTML = "<p>Add teaching days and teachers first</p>"
        return;
    }

    if (!substituteDay) substituteDay = config.days[0];
    if  (!absentTeacher) absentTeacher = teacherIds[0];

    let dayOptions = config.days.map(function(day){
return `<option value="${day}">${day}</option>`;
    }).join("");

    let teacherOptions = teacherIds.map(function(id){
        return `<option value="${id}">${teacherName(id)}</option>`
    }).join("")

    box.innerHTML = `
        <h3>Substitution planner</h3>
        <label>Day <select id="subDay">${dayOptions}</select></label>
        <label>Absent teacher <select id="absentTeacher">${teacherOptions}</select></label>
        <div id="coverList"></div>
    `

    document.getElementById("subDay").value = substituteDay;
    document.getElementById("absentTeacher").value = absentTeacher;

    document.getElementById("subDay").addEventListener("change", function(event){
        substituteDay = event.target.value;
        renderSubstitutionPlanner()
    })

    document.getElementById("absentTeacher").addEventListener("change", function(event){
        absentTeacher = event.target.value;
        renderSubstitutionPlanner()
    })

    let lessons = [];

    Object.keys(schedule).forEach(function(className){
        Object.entries(schedule[className]).forEach(function([slot, entry]){
            if (entry && slot.startsWith(substituteDay + " ") && entry.teacher === absentTeacher){
                lessons.push({className: className, slot: slot,entry: entry})
            }
        })
    })

    let coverList = document.getElementById("coverList")

    if (!lessons.length){
        coverList.innerHTML = `<p>This teacher has no lectures that day</p>`
        return;
    }

    coverList.innerHTML = lessons.map(function(lesson){
        let available = teacherIds.filter(function(id){
            if (id === absentTeacher) 
                return false;

            return !Object.keys(schedule).some(function(className){
                let entry = schedule[className][lesson.slot]
                return entry && entry.teacher === id;
            })
        })

        let key = lesson.className + "|" + lesson.slot;
        let options = available.map(function(id){
            return `<option value="${id}" ${substituteChoices[key] === id ? "selected" : ""}>${teacherName(id)}</option>`
        }).join("")

        return `
        <p> ${lesson.slot} ${lesson.className}: ${subjectName(lesson.entry.subject)}
            <select data-cover="${key}"> 
            <option value="">Choose a substitute</option> 
            ${options}
            </select>
        </p>
        `
    }).join("")

coverList.querySelectorAll("[data-cover]").forEach(function(select){
        select.addEventListener("change",function(event){
            substituteChoices[event.target.dataset.cover] = event.target.value;
        } )
    })

}

// so this might be a part of python, but ill do it as a seperate feature too lol

function renderConflicts(){
    let box = document.getElementById("conflictResults");
    let conflicts = [];

    config.days.forEach(function(day){
        for (let p = 1; p <= config.periodsPerDay; p++){
            let teachersHere = {};

            Object.keys(schedule).forEach(function(className){
                let entry = schedule[className][`${day} P${p}`]

                if (entry) {
                    if (!teachersHere[entry.teacher]){
                        teachersHere[entry.teacher] = [];
                    }
                    teachersHere[entry.teacher].push(className);
                }
            })
            Object.keys(teachersHere).forEach(function(teacherId){
                if (teachersHere[teacherId].length > 1){
                    conflicts.push(
                        teacherName(teacherId) + " is assigned to " + teachersHere[teacherId].join(" and ") + " on " + day + ", P" + p
                    )
                }
            })
        }
    })
    if (conflicts.length === 0){
        box.innerHTML = `<p class="validationMessage success">No teacher conflicts found</p>`
    }
    else {
        box.innerHTML = `<p class="validationMessage error">Teacher conflicts found:</p><ul>` + conflicts.map(function(conflict){
return "<li>" + conflict + "</li>";
        }).join("") + "</ul>"
    }
}


// gonna add this cause why not lol
function renderWorkload(){

        let box = document.getElementById("gridBox");

    if (!teacherIds.length){
        box.innerHTML = "<p>No teachers found.</p>";
        return;
    
    }

        let cards = teacherIds.map(function(id){
        let total = 0;
        let daily = {};

        Object.keys(schedule).forEach(function(className){
            Object.entries(schedule[className]).forEach(function([slot, entry]){
            if (!entry || entry.teacher !== id) return;

                            let day = slot.split(" ")[0];
                total++;
                daily[day] = (daily[day] || 0) + 1;
            });
        });

        let teacher = config.teachers.find(function(item){
            return item.id === id;
        });

        let limit = teacher ? teacher.maxPerDay : config.periodsPerDay;
        let overloadedDays = Object.keys(daily).filter(function(day){
            return daily[day] > limit;
        });

        let status = overloadedDays.length ? "Over daily limit: " + overloadedDays.map(function(day){
                return day + " (" + daily[day] + ")";
            }).join(", ") : "Within daily limit";

                    let percent = Math.min(
            100,
            Math.round(total / Math.max(1, config.days.length * limit) * 100)
        );

                return `
            <article class="workloadCard">
                <h3>${teacherName(id)}</h3>
                <p><strong>${total}</strong> periods this week</p>
                <div class="workloadTrack">
                    <div class="workloadFill" style="width: ${percent}%"></div>
                </div>
                <p>Daily limit: ${limit} periods</p>
                <p class="${overloadedDays.length ? "error" : "success"}">${status}</p>
            </article>
            `;
        }).join("");

            box.innerHTML = `<div class="workloadGrid">${cards}</div>`;

} 

function teacherGrid(teacherId){
    let breakAfter = {};

    config.breaks.forEach(function(b){
        breakAfter[b.after] = b.label;
    })

    let header = "<tr><th>Period</th>";
    config.days.forEach(function(day){
        header += `<th>${day}</th>`
    })

    header += "</tr>"

    let rows = "";

for (let p = 1; p <= config.periodsPerDay; p++){
        rows +=  `<tr><th>P${p}</th>`;

        config.days.forEach(function(day){
            let slot = `${day} P${p}`;

            let classes = Object.keys(schedule).filter(function(className){
                let entry = schedule[className][slot];
                return entry && entry.teacher === teacherId;
            })

    let cells = classes.map(function(className){                let entry = schedule[className][slot]
                return `<b>${className}</b><small>${subjectName(entry.subject)}</small>`;
            }).join("");

            rows += `<td>${cells || "<small>Free</small>"}</td>`;
        })
        rows += "</tr>";

        if (breakAfter[p]){
            rows += `<tr class ="breakRow"><td colspan=${config.days.length +1}>${breakAfter[p]}</td></tr>`
        }
    }
    return `<table class="grid">${header}${rows}</table>`;

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
                let slot = `${d} P${p}`;
                // cleaner lol
                let entry = schedule[className][slot];
                let subject = entry ? subjectName(entry.subject) : "";
                let teacher = entry ? teacherName(entry.teacher) : "";
                // looks clean right?
                rows += `<td class="editCell" data-slot="${slot}"><b>${subject}</b><small>${teacher}</small></td>`;

            })
            rows += "</tr>";

            if (breakAfter[p]){
              rows += `<tr class="breakRow"><td colspan="${config.days.length + 1}">${breakAfter[p]}</td></tr>`
            }
        }

        return `<table class="grid">${header}${rows}</table>`
    }
    