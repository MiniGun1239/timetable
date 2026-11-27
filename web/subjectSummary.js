export function subjectSummary(classSlots, getSubjectName){
 
    let counts = {};

    Object.values(classSlots || {}).forEach(function(lesson){
        if (!lesson) return;

        counts[lesson.subject] = (counts[lesson.subject] || 0) + 1;
    });

    let rows = Object.keys(counts).map(function(subjectId){
        return `<li>
            <span>${getSubjectName(subjectId)}</span>
            <strong>${counts[subjectId]} lessons</strong>
        </li>`;
    }).join("");

    if (!rows) return "";

    return `
    <section class="subjectSummary">
        <h3>Lessons this week</h3>
        <ul>${rows}</ul>
    </section>`;
}