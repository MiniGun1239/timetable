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

    // oops i forgot there are like 2 more of these, fuhh

    panel.querySelectorAll("[data-weekly-teacher]").forEach(function(input){
        input.addEventListener("change", function(event){
            assignemnts[Number(event.target.dataset.weeklyTeacher)].teacherId = event.target.value;
        })
    })

    panel.querySelectorAll("data-weekly-min").forEach(function(input){
        input.addEventListener("change", function(event){
            assignemnts[Number(event.target.weeklyMin)].minimumPerWeek = Number(event.target.value);
        })
    })

    panel.querySelectorAll("[data-remove-weekly]").forEach(function(button){
        button.addEventListener("click", function(event){
            assignemnts.splice(Number(event.target.dataset.removeWeekly), 1);
            renderSetup()
        })
    })
}

export function weeklyRequirementErrors(config){
    let errors = [];
    let assignemnts = getAssignments(config);
    let classNames = [];

    config.grades.forEach(function(grade){
        grade.sections.forEach(function(grade){
            classNames.push(grade.name + "-" + section)
        })
    })

    assignemnts.forEach(function(requirement, index){
        let subjectExists = config.subjects.some(function(subject){
            return subject.id == requirement.subjectId
        })

        let teacherExists = config.teachers.some(function(teacher){
            return teacher.id == requirement.teacherId
        })


        // umm the stupid add errors, why do you even need these lol
        if (!subjectExists || !classNames.includes(requirement.className) || !teacherExists){
            errors.push("Requirement " + (index + 1) + ": choose a subject, class, and teacher")
        }

        if (!Number.isInteger(requirement.minimumPerWeek) || requirement.minimumPerWeek < 1){
            errors.push("Requirement " + (index + 1 + ": minimum lessons must be positive bruhh"))
        }

        if (config.days.length > 0 && Number.isInteger(config.periodsPerDay) && 
            requirement.minimumPerWeek > config.days.length * config.periodsPerDay){
            errors.push("Requirement " + (index + 1) + ": weekly minumum cant be larger than available periods");
        }
})

return errors;
    
}