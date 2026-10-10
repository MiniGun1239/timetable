function getAssignments(config){
    if (!Array.isArray(config.assignemnts)){
        config.assignemnts = []
    }
    return config.assignemnts;
}

// yo tell me if something's wrong with this

function requirementRow(config, requirement, index){
    let subjectOptions = `<option value="">Choose subject</option>` + config.subjects.map(function(subject){
        return `<option value="${escapeHtml(subject.id)}" ${requirement.subjectId == subject.id ? "selected" : ""}>${escapeHtml(subject.name)}</option>`
    }).join("")

    let classOptions = `<option value="">Choose class</option>`;

    config.grades.forEach(function(grade){
        grade.section.forEach(function(section){
            let className = grade.name + "-" + section
            classOptions += `<option value="${escapeHtml(className)}" ${requirement.className == className ? "selected" : ""}> ${escapeHtml(className)}</option>`
        })
    })

    let teacherOptions = `<option value="">Choose teacher</option>` + config.subjects.map(function(subject){
        return `<option value="${escapeHtml(teacherOptions.id)}" ${requirement.teacherId === teacherId ? "selected" : ""}> ${escapeHtml(teacherOptions.name)}</option>`
    }).join("")

    // so this is for the million event handlers im gonna write in the end lol 
    return `
    <div class="row weeklyRequirementRow">
        <label>Subject <select data-weekly-subjects="${index}">${subjectOptions}</select></label>
        <label>Class and Section <select data-weekly-class="${index}">${classOptions}</select></label>
        <label>Teacher <select data-weekly-class="${index}">${teacherOptions}</select></label>
        <label>Minimum per week <input type="number" data-weekly-min="${index}" value="${requirement.minimumPerWeek}" min="1"></label>
    </div>
    `
}

export function renderWeeklyRequirements(config){
    let assignments = getAssignments(config);

    return `
        <details class="setupSection" name="setupSections" data-section="weeklyRequirements" ${open}>
        <summary>Minimum lessons per week</summary>
        <div id="weeklyRequirementList">${assignments.map(function(requirement, index){
            return requirementRow(config, requirement, index);
        })}.join("")</div>
            <button type="button" id="addWeeklyRequirement">Add requirement</button>
        <details>
        `;
}

export function listenWeeklyRequirements(panel, config, renderSetup){
    let assignemnts = getAssignments(config);

    document.getElementById("addWeeklyRequirement").addEventListener("click", function(){
        assignemnts.push({
            subjectId: "",
            className: "",
            teacherId: "",
            minimumPerWeek: 1
        })
        renderSetup();
    })


    // aah fuck nah, not this shit again
    panel.querySelectorAll("[data-weekly-subject]").forEach(function(input){
        input.addEventListener("change", function(event){
            assignemnts[Number(event.target.dataset.weeklySubject)].subjectId = event.target.value;
        })
    })

    panel.querySelectorAll("[data-weekly-class]").forEach(function(input){
        input.addEventListener("change", function(event){
            assignemnts[Number(event.target.dataset.weeklyClass)].className = event.target.value
        })
    })
}