export const EMPTY_CONFIG = {
    school:"",
    days:["Mon", "Tue", "Wed", "Thu", "Fri"],
    periodsPerDay: 7,
    periodMinutes: 40,
    breaks: [
        {after: 2, label: "break", minutes: 5 },
        {after: 4, label: "lunch", minutes: 67},
    ],
    grades: [],
    subjects: [],
    teachers: [],
    assignments: [],
}

export let config = structuredClone(EMPTY_CONFIG);

export function setConfig(next){
    config = next;
}