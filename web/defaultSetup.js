
// real simple shi
export function createDefaultSetup(){
    return {
        school: "Some School",
        days: ["Mon", "Tue", "Wed", "Thu", "Fri"],
        periodsPerDay: 6,
        periodMinutes: 40,
        breaks: [{after: 2, label: "Break", minutes: 15}],
        subjects: [
            {id: "s-math", name: "Maths", noBackToBack: false},
            {id: "s-english", name: "English", noBackToBack: false},
            {id: "s-science", name: "Science", noBackToBack: false}
        ],
        teachers: [
            {id: "t-math", name: "Mr.Maths", maxPerDay: 6, subjectIds: ["s-math"]},
            {id: "t-english", name: "Mr.English", maxPerDay: 6, subjectIds: ["s-english"]},
            {id: "t-science", name: "Mr.Science", maxPerDay: 6, subjectIds: ["s-science"]}
        ],
        grades: [{id: "g-default", name: "10", sections: ["A"]}],
        assignments: [
            {className: "10-A", subjectId: "s-math", teacherId: "t-math", minimumPerWeek: 5},
            {className: "10-A", subjectId: "s-english", teacherId: "t-english", minimumPerWeek: 5},
            {className: "10-A", subjectId: "s-science", teacherId: "t-science", minimumPerWeek: 5}
        ]
    };
}
